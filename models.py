from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    role = db.Column(db.String(255))
    password = db.Column(db.String(255))

class ClassModel(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher = db.Column(db.String(255))
    discipline = db.Column(db.String(255))
    subject = db.Column(db.String(255))
    presentStudents = db.Column(db.String(255))
    homeActivities = db.Column(db.String(255))
    date = db.Column(db.DateTime)
    activitiesDelivered = db.Column(db.String(255))
    notes = db.Column(db.String(1000))