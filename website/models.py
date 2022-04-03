from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class UserInfo(db.Model, UserMixin):
    id = db.Column(db.String(200), primary_key=True)
    task = db.Column(db.Integer)
    chance = db.Column(db.Integer)

