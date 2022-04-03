from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from .config import config
from flask_compress import Compress

new_config = config()
DB_NAME = new_config.get_dbname() 
db = SQLAlchemy()
compress = Compress()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = new_config.get_secret_key()
    app.config['SQLALCHEMY_DATABASE_URI'] = new_config.get_uri()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = new_config.get_track()

    db.init_app(app)

    from .views import views
    app.register_blueprint(views,url_prefix='/')
    
    from .models import UserInfo
    create_database(app)
    compress.init_app(app)

    return app

def create_database(app):
    if not path.exists('website/'+DB_NAME): 
        db.create_all(app=app)
