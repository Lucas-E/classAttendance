from flask import Blueprint, redirect, request, render_template, url_for, flash
from .models import User, ClassModel
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_required, login_user, current_user, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/search/', methods=['POST'])
def search():
    discipline = request.form.get('search')
    classes = ClassModel.query.filter_by(discipline=discipline).all()
    return(render_template('classes.html', user=current_user, classes=classes))

@auth.route('/login')
def login():
    if current_user.is_authenticated:
        return(redirect(url_for('main.classes')))

    return(render_template('login.html'))

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user  = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('wrong Email or Password')
        return(redirect(url_for('auth.login')))
    
    login_user(user, remember=False)
    return(redirect(url_for('main.classes')))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return(redirect(url_for('main.index')))

@auth.route('/signup')
def signup():
    if current_user.is_authenticated:
        return(redirect(url_for('main.classes')))

    return(render_template('signup.html'))

@auth.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    role = request.form.get('role')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('The email already exists')
        return(redirect(url_for('auth.signup')))

    new_user = User(name=name, email=email, role=role, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return(redirect(url_for('auth.login')))