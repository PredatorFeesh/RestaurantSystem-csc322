from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import LoginForm, RegisterForm
import flask_login as fl
from flask_login import current_user, login_user, logout_user

from app.models import User
from app.models import db

login_manager = fl.LoginManager()

@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()

login_manager.login_view = "login"

login_manager.init_app(app)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
def index():
    if current_user.is_authenticated:
        return "Welcome {}".format(current_user.username)
    return "Works!"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        # flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            # flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title="Sign In", form=form)