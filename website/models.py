## Database models

## From current package import db object
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime
import flask_uploads

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now)



class File(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String(100), nullable =True)
    date_uploaded = db.Column(db.DateTime(timezone = True), default = func.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable = False )
    
    def __repr__(self):
        return f"File('{self.filename}', '{self.date_uploaded}')"
    
    
class User(db.Model, UserMixin):
    #primary key for user object
    id = db.Column(db.Integer, primary_key=True)
    #email column with a max of 200 characters, must be unique
    email = db.Column(db.String(200), unique = True)
    password = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    # 'File' refers to the File class, 'owner' will be the attribute to use in File instances to refer back to the owner User
    files = db.relationship('File', backref='owner', lazy = True)

    def __repr__(self):
        return f"User('{self.email}', '{self.first_name}')"

class File(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String(100), nullable =True)
    date_uploaded = db.Column(db.DateTime(timezone = True), default = func.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable = False )
