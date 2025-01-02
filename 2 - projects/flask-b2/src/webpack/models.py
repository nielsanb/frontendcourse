from flask_login import UserMixin
from sqlalchemy.sql import func

from webpack import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #For 1-to-many, 1user-to-manynotes
    #Foreign keys point to the primary key of another table (and you always have to specify it when adding a note!)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    age = db.Column(db.Integer)
    notes = db.relationship('Note') #Capital, inconsistency
