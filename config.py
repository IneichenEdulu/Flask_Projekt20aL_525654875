class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:sml12345@localhost/jobinserate'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'm151'
    JWT_ERROR_MESSAGE_KEY = 'message'
