class Local(object):
    ENV = 'development'
    DEBUG = True
    HOST = '127.0.0.1'
    PORT = 5000


class Prod(object):
    ENV = 'production'
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 8000
