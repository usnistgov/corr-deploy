DEBUG = True

FLASK_ENV = 'development'

# Verify that your docker host is 172.17.0.1
# If not replace it in the mongodb_host field.
# Change the mongodb port here if needed.
# Warning: Make sure the docker-compose port matches.
MONGODB_SETTINGS = {
    'db': 'corr-integrate',
    'host': '172.17.0.1',
    'port': 27017
}

MODE = 'http'

ENVIRONMENT = 'development'

FILE_STORAGE = {
    'type': 'filesystem',
    'location': '/home/corradmin/',
    'name': 'corr-storage',
    'id': '',
    'key': ''
}

ACCOUNT_MANAGEMENT = {
    'type': 'api-token'
}

SECURITY_MANAGEMENT = {
    'account': 'True',
    'content': 'False'
}
