from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path
import os
from .config import config
from flask_compress import Compress

new_config = config()
db = SQLAlchemy()
compress = Compress()

def create_app():
    app = Flask(__name__)
    app.config["COMPRESS_REGISTER"] = False

    app.config['SECRET_KEY'] = new_config.get_secret_key()
    app.config['SQLALCHEMY_DATABASE_URI'] = new_config.get_RDSuri()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = new_config.get_track()

    migrate = Migrate(app,db)
    db.init_app(app)
    from .views import views
    app.register_blueprint(views,url_prefix='/')
    db.create_all(app=app)
    from .models import UserInfo
    create_database(app)
    compress.init_app(app)

    return app


