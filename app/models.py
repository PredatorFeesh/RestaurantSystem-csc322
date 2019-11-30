from app import db
import flask_login
from werkzeug.security import generate_password_hash, check_password_hash

"""
customer 1 
manager 2
cook 3
sales 4
deliverer 5
"""


class Customer(db.Model, flask_login.UserMixin ):
    """
    The main user model for our software. This should include the user type and all
    its attributes.
    
    """
    __tablename__ = 'customer'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(255))
    user_type="1"
    


    authenticated = db.Column(db.Boolean, default=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        # We are encoding the tpye in the id
        return int(self.user_type+str(self.id))

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

class Manager(db.Model, flask_login.UserMixin ):
    """
    The main user model for our software. This should include the user type and all
    its attributes.
    
    """
    __tablename__ = 'manager'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(255))
    user_type="2"


    authenticated = db.Column(db.Boolean, default=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return int(self.user_type+str(self.id))

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

class Deliverer(db.Model, flask_login.UserMixin ):
    """
    The main user model for our software. This should include the user type and all
    its attributes.
    
    """
    __tablename__ = 'deliverer'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(255))
    user_type="5"


    authenticated = db.Column(db.Boolean, default=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return int(self.user_type+str(self.id))

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

class Cook(db.Model, flask_login.UserMixin ):
    """
    The main user model for our software. This should include the user type and all
    its attributes.
    
    """
    __tablename__ = 'cook'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(255))
    user_type = "3"


    authenticated = db.Column(db.Boolean, default=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return int(self.user_type+str(self.id))

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

class Sales(db.Model, flask_login.UserMixin ):
    """
    The main user model for our software. This should include the user type and all
    its attributes.
    
    """
    __tablename__ = 'sales'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(255))
    user_type = "4"


    authenticated = db.Column(db.Boolean, default=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return int(self.user_type+str(self.id))

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False



class Foods(db.Model):
    __tablename__ = 'foods'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

class Restaurant(db.Model):
    """
    The main user model for our software. This should include the user type and all
    its attributes.
    
    """
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    
    name = db.Column(db.String(100), index=True)

