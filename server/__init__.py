import logging
import os
from logging.handlers import TimedRotatingFileHandler

from flask import Blueprint, Flask, make_response
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

from __version__ import __version__
from config.config import app_config
from server.api.resources.example import api as example_api

log = logging.getLogger('Unit_Spot')


def create_app(config_name):
    if config_name is None:
        config_name = 'production'
    app = Flask(__name__, instance_relative_config=True)
    blueprint = Blueprint('api', __name__, url_prefix='/api/1')
    app.config.SWAGGER_UI_REQUEST_DURATION = True
    app.config.from_object(app_config[config_name])
    # override above settings file if present
    app.config.from_pyfile('config.cfg', silent=True)
    app.log = init_logger(app)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    api = Api(blueprint,
              title='Unity / Spot API',
              version=__version__,
              description='Unity / Spot API v{}'.format(__version__),
              # security='Bearer Auth',
              # headers={'X-server-version': __version__},
              # authorizations=authorizations
              )
    # @api.representation('application/json')
    # def json(data, code, headers):
    #     resp = make_response(data, code)
    #     headers['X-API-Server-Version'] = __version__
    #     resp.headers.extend(headers)
    #     return resp

    app.register_blueprint(blueprint)
    CORS(app, resources={r"/*": {"origins": "*"}})

    with app.app_context():
        api.add_namespace(example_api)

    log.info('********** Unity / Spot API v{} **********'.format(__version__))
    # log.info('Using instance config: %s', app.config['INSTANCE'])
    log.info('Using configuration: %s', config_name)
    # log.info('Using data source: %s', app.config.get('DATABASE_URI'))
    return app


def init_logger(app):
    if not os.path.exists(app.config['LOG_PATH']):
        os.makedirs(app.config['LOG_PATH'])

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s]: %(message)s')
    formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
    handler = TimedRotatingFileHandler(app.config.get('LOG_FILE'),
                                       when="D",
                                       interval=1,
                                       backupCount=10,
                                       utc=True)
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    log.addHandler(handler)
    return log
