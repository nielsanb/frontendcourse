from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notetext = db.Column(db.String(1000))
    date_submitted = db.Column(db.DateTime(timezone=True), default=func.now())
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    firstname = db.Column(db.String(150))
    age = db.Column(db.Integer)
    password = db.Column(db.String(150))
    notes = db.relationship('Note')

    #Please note that the use of 'user.id' and 'Note' is very inconsistent in capitals
    #Please note that there is a 1:many relationship. 
    #   The many side has a column to the primary key of the other.
    #   The one side has a db.relationship to associate the users' notes to the users.