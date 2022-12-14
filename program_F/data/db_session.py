from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    fname = db.Column(db.String(250), nullable=False)
    log = db.Column(db.String(250), nullable=False)
    password = db.Column(db.Integer)




