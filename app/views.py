from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
def index():
    return "Works!"


@app.route('/login', methods=["GET","POST "])
def login():
    form = LoginForm()
    return render_template('login.html', title="Sign In", form=form)