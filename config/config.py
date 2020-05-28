import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Parent configuration class."""
    AUTH_REQUIRED = True
    BASE_PATH = basedir
    CERT_FILE = ''
    CERT_KEY = ''
    CONFIG_PATH = os.path.join(BASE_PATH, 'config')
    CSRF_ENABLED = True
    FLASK_DEBUG = False
    INSTANCE = False
    LOG_PATH = os.path.join(BASE_PATH, '.logs')
    LOG_FILE = os.path.join(LOG_PATH, 'server.log')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 443
    SSL_CONTEXT = (CERT_FILE, CERT_KEY)
    SSL_ENABLED = True
    TESTING = False


class DevelopmentConfig(Config):
    """Configurations for Development."""
    AUTH_REQUIRED = False
    FLASK_DEBUG = True
    SERVER_PORT = 5000
    SSL_ENABLED = False
    SSL_CONTEXT = 'adhoc'
    SECRET_KEY = '6E8BA4132A7C84FD6A8E3A3F55F97'


class TestingConfig(Config):
    """Configurations for Testing."""
    AUTH_REQUIRED = False
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEST_PATH = os.path.join(BASE_PATH, 'tests')
    LOG_PATH = os.path.join(BASE_PATH, '.logs')
    LOG_FILE = os.path.join(LOG_PATH, 'test_server.log')
    TESTING = True
    FLASK_DEBUG = True
    SSL_CONTEXT = 'adhoc'
    SSL_ENABLED = False
    SERVER_PORT = 5000


class StagingConfig(Config):
    """Configurations for Staging."""
    FLASK_DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    FLASK_DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
