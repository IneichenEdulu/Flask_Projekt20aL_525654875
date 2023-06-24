import os
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{}:{}@{}/{}'.format(
        os.getenv('DB_USER', 'user'),
        os.getenv('DB_PASSWORD', 'password'),
        os.getenv('DB_HOST', 'db_host'),
        os.getenv('DB_NAME', 'jobinserate')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
