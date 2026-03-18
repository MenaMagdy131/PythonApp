import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__, template_folder="templates")
    
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')
    
    # SQLAlchemy URI
    DB_USER = os.environ.get('MYSQL_USER', 'mena')
    DB_PASS = os.environ.get('MYSQL_PASSWORD', 'mena123')
    DB_HOST = os.environ.get('MYSQL_HOST', 'db')
    DB_NAME = os.environ.get('MYSQL_DATABASE', 'flaskapp')
    DB_PORT = os.environ.get('MYSQL_PORT', 3306)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    
    login_manager.login_view = "main.login"
    
    from .routes import main
    app.register_blueprint(main)
    
    return app