import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret')
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'mena')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'mena123')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', 'flaskapp')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False