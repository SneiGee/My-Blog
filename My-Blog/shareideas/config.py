import os


class Config:
    SECRET_KEY = '38ef1201a26426878f45d6ba0572cbe9'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///shareideas.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
