from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_login as fl

app = Flask(__name__)
app.config.from_object('config')

# Database
db = SQLAlchemy(app)


manager = fl.LoginManager()
manager.init_app(app)



sales = fl.LoginManager()
sales.init_app(app)



cook = fl.LoginManager()
cook.init_app(app)




deliverer = fl.LoginManager()
deliverer.init_app(app)


customer = fl.LoginManager()
customer.init_app(app)

from app import views, models