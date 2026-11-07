from . import db
from flask_login import UserMixin

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(150))
    position = db.Column(db.String(150))
    status = db.Column(db.String(50), default='Applied')
    date_applied = db.Column(db.Date)
    link = db.Column(db.String(500))
    notes = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(250))
    firstName = db.Column(db.String(150))
    applications = db.relationship('Application')