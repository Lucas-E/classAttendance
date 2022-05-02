from msilib.schema import Class
from nturl2path import url2pathname
from re import sub
from flask import Blueprint, redirect, request, render_template, url_for, flash
from flask_login import login_required, current_user
from .models import ClassModel
from . import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return(render_template('index.html', authenticated=current_user.is_authenticated))

@main.route('/classes')
@login_required
def classes():
    classes = ClassModel.query.all()
    return(render_template('classes.html', user=current_user, classes=classes))

@main.route('/registerClass', methods=['POST'])
@login_required 
def registerClass():
    teacher = request.form.get('teacher')
    discipline = request.form.get('discipline')
    subject = request.form.get('subject')
    presentStudents = request.form.get('present-students')
    activities = request.form.get('activities')
    deliveredActivities = request.form.get('delivered-activities')
    notes = request.form.get('notes')
    date = request.form.get('date')
    new_date = datetime.strptime(date, "%Y-%m-%d")
    newClass = ClassModel(teacher = teacher, discipline=discipline, subject=subject, presentStudents=presentStudents, homeActivities=activities, date=new_date,activitiesDelivered=deliveredActivities, notes=notes)

    db.session.add(newClass)
    db.session.commit()

    flash('Class Registered Successfully!')
    return(redirect(url_for('main.classes')))

@main.route('/deleteClass/<int:id>', methods=['POST'])
@login_required
def deleteClass(id):
    classId = id 
    classQuery = ClassModel.query.filter_by(id=classId).first()
    db.session.delete(classQuery)
    db.session.commit()
    flash('Class Deleted Successfully!')
    return(redirect(url_for('main.classes')))