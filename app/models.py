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

class CustRestType(db.Model):
    __tablename__ = "custresttype"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cust_id = db.Column(db.Integer)
    rest_id = db.Column(db.Integer)

    # Could be: regular, registered, blacklisted
    relation_tye = db.Column(db.String(255))

order_restaurant_association = db.Table( 'order_restaurant_association', db.Model.metadata,
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id') ),
    db.Column('order_id', db.Integer, db.ForeignKey('order.id') )
)
order_menu_association = db.Table( 'order_menu_association', db.Model.metadata,
    db.Column('order_id', db.Integer, db.ForeignKey('order.id') ),
    db.Column('item_id', db.Integer, db.ForeignKey('order_item.id') )
)
ordered = db.Table('orders', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('customer.id')),
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'))
)

class Menu_Item(db.Model):
    __tablename__ = 'menu_item'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column( db.String(100) )
    description = db.Column( db.String(255) )
    price = db.Column( db.String(255) )

    restaurant_id = db.Column( db.Integer, db.ForeignKey('restaurant.id') )


class Order_Item(db.Model):
    __tablename__ = 'order_item'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    menu_item_id = db.Column(db.Integer)
    order_id = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    def get_menu_item(self):
        return Menu_Item.query.filter(Menu_Item.id==self.id).first()

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ordered_items = db.relationship(
        'Order_Item', secondary=order_menu_association,
        primaryjoin=(order_menu_association.c.order_id == id),
        secondaryjoin=(order_menu_association.c.item_id == Order_Item.menu_item_id),
        backref=db.backref('order_menu_association', lazy='dynamic'),lazy = 'dynamic'
    )
    approved = db.Column(db.Boolean,default=False)
    delivered = db.Column(db.Boolean,default=False)

class Restaurant(db.Model):
    """
    The main user model for our software. This should include the user type and all
    its attributes.
    
    """
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column( db.String(100) )
    description = db.Column( db.String(100) )

    menu_items = db.relationship('Menu_Item', backref=db.backref('restaurant'), lazy='dynamic' )

    orders = db.relationship(
        'Order', secondary=order_restaurant_association,
        primaryjoin=(order_restaurant_association.c.restaurant_id == id),
        secondaryjoin=(order_restaurant_association.c.order_id == Order.id),
        backref=db.backref('order_restaurant_association', lazy='dynamic'),lazy = 'dynamic'
    )

    manager = db.relationship("Manager", backref="restaurant")

    cook = db.relationship("Cook", backref="restaurant")


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
    
    orders = db.relationship("Order", secondary=ordered,
        primaryjoin=(ordered.c.user_id==id),
        secondaryjoin=(ordered.c.order_id==Order.id),
        backref=db.backref('ordered', lazy="dynamic"), lazy='dynamic'
    )


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

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))


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

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))


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

