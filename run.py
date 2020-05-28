import datetime
import logging
import os
from logging.handlers import TimedRotatingFileHandler
from urllib.parse import urlparse

from flask import make_response, redirect, request, session

from __version__ import __version__
from server import create_app

log = logging.getLogger(__name__)

config_name = os.getenv('FLASK_ENV') or 'production'
print('Starting server with config: {}'.format(config_name))
app = create_app(config_name)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s]: %(message)s')
    formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
    handler = TimedRotatingFileHandler(app.config['LOG_FILE'],
                                       when="D",
                                       interval=1,
                                       backupCount=10,
                                       utc=True)
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)

    log = logging.getLogger(__name__)
    log.addHandler(handler)

    HOST = app.config['SERVER_HOST']
    PORT = app.config['SERVER_PORT']

    DEBUG = app.config['FLASK_DEBUG']
    # print(app.config)
    # for key, val in app.config.items():
    #     print(key, val)
    # print('debug:', DEBUG)

    if app.config['SSL_ENABLED']:
        SSL_CONTEXT = app.config['SSL_CONTEXT']
        try:
            app.run(HOST, PORT, threaded=True,
                    debug=DEBUG, ssl_context=SSL_CONTEXT)
        except Exception as e:
            log.error('Error: {}'.format(e))
            log.info('SSL Context: {}'.format(SSL_CONTEXT))
    else:
        app.run(HOST, PORT, threaded=True, debug=DEBUG)
