import os


_user = os.environ.get('POSTGRES_USER')
_password = os.environ.get('POSTGRES_PASSWORD')
_host = os.environ.get('POSTGRES_HOST')
_database = os.environ.get('POSTGRES_DB')
_port = os.environ.get('POSTGRES_PORT')


class Config(object):
    """
        Main application config.
    """

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SESSION_TYPE = 'filesystem'
    SWAGGER = {
        'specs': [
            {
                'version': '0.0.1',
                'title': 'Simple Catalog',
                'endpoint': 'v1_spec',
                'route': '/v1/spec',
            }
        ],
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
        _user,
        _password,
        _host,
        _port,
        _database
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DATA_SOURCE_FILE = os.environ.get('DATA_SOURCE_FILE', None)
    DATA_SOURCE_URL = os.environ.get('DATA_SOURCE_URL', None)

    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
