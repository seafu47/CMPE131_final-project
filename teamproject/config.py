import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    #secret-key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess please'

    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or 'guess please'
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or 'guess please'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
