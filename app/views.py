from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import LoginForm, RegisterForm
import flask_login as fl
from flask_login import current_user, login_user, logout_user, login_required

from app.models import * # Actual users
from app import db # Our database

from app import customer, manager, cook, sales, deliverer # Login

@customer.user_loader
@cook.user_loader
@sales.user_loader
@manager.user_loader
@deliverer.user_loader
def load_user(id):
    id = str(id)
    print("Inside load_user: "+str(id))
    type = id[0]
    id = int(id[1:])
    if type == "1":
        return Customer.query.get(int(id))
    elif type == "2":
        return Manager.query.get(int(id))
    elif type == "3":
        return Cook.query.get(int(id))
    elif type == "4":
        return Sales.query.get(int(id))
    elif type == "5":
        return Deliverer.query.get(int(id))


def get_login(user_type, user_id):
    if type == "1":
        return Customer.query.get(int(id))
    elif type == "2":
        return Manager.query.get(int(id))
    elif type == "3":
        return Cook.query.get(int(id))
    elif type == "4":
        return Sales.query.get(int(id))
    elif type == "5":
        return Deliverer.query.get(int(id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
def index():
    if current_user.is_authenticated:
        return "Welcome {}".format(current_user.user_type)
        # return redirect(url_for("restaurants"))
    return render_template("index.html")

@app.route('/restaurants')
def restaurants():
    restaurants = Restaurant.query.paginate(1,20,False).items 
    print(restaurants)
    return render_template("restaurants.html", restaurants=restaurants)

@app.route('/restaurant/<int:id>')
def restaurant(id):
    menu_items = Restaurant.query.get(id).menu_items.all()
    print(menu_items)
    return render_template("restaurant.html",rest_id=id,menu_items=menu_items)

@app.route('/order', methods=["POST"])
def order():
    # We go over the ids to get amount
    print(str(request.form["rest_id"]))
    menu_items = Restaurant.query.get(int(request.form["rest_id"])).menu_items.all()
    if current_user.is_authenticated:
        print(current_user.get_id())
        cur_usr = Customer.query.get(int(str(current_user.get_id())[:-1] ))
    print(menu_items)
    #pretend correctly validated
    order = Order()
    db.session.add(order)
    db.session.commit()
    print("Order_id = "+str(order.id))
    
    items = 0
    
    for item in menu_items:
        amount = int(request.form[str(item.id)])
        if amount != 0:
            items += 1
            req_item = Order_Item(menu_item_id=item.id, order_id=order.id ,amount=amount)
            db.session.add(req_item)
            order.ordered_items.append(req_item)
    
    if items == 0:
        return "No orders!" 

    if current_user.is_authenticated:
        cur_usr.orders.append(order)

    db.session.commit()

    return "Successfully placed order! Waiting for approval."

@app.route('/my_orders')
@login_required
def my_orders():
    cur_usr = Customer.query.get(  int(  str(current_user.get_id())[:-1]  )  )
    orders = cur_usr.orders
    return render_template("my_orders.html", orders=orders)



# Customer
@app.route('/rc', methods=['GET', 'POST'])
def rc():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = Customer(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        # flash('Congratulations, you are now a registered user!')
        return redirect(url_for('lc'))
    
    return render_template('register.html', title='Register', form=form)

@app.route('/lc', methods=['GET','POST'])
def lc():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = Customer.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            # flash('Invalid username or password')
            return redirect(url_for('lc'))
        print("Inside LC: "+str(user))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title="Sign In", form=form)


# Manager
@app.route('/rm', methods=['GET', 'POST'])
def rm():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = Manager(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        # flash('Congratulations, you are now a registered user!')
        return redirect(url_for('lm'))
    
    return render_template('register.html', title='Register', form=form)

@app.route('/lm', methods=['GET','POST'])
def lm():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = Manager.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            # flash('Invalid username or password')
            return redirect(url_for('lm'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    
    return render_template('login.html', title="Sign In", form=form)


# Delivery
@app.route('/rd', methods=['GET', 'POST'])
def rd():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = Deliverer(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        # flash('Congratulations, you are now a registered user!')
        return redirect(url_for('ld'))
    
    return render_template('register.html', title='Register', form=form)

@app.route('/ld', methods=['GET','POST'])
def ld():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = Deliverer.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            # flash('Invalid username or password')
            return redirect(url_for('ld'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    
    return render_template('login.html', title="Sign In", form=form)


# Sales
@app.route('/rs', methods=['GET', 'POST'])
def rs():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = Sales(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        # flash('Congratulations, you are now a registered user!')
        return redirect(url_for('ls'))
    
    return render_template('register.html', title='Register', form=form)

@app.route('/ls', methods=['GET','POST'])
def ls():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = Sales.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            # flash('Invalid username or password')
            return redirect(url_for('ls'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    
    return render_template('login.html', title="Sign In", form=form)



# Cook
@app.route('/rco', methods=['GET', 'POST'])
def rco():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = Cook(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        # flash('Congratulations, you are now a registered user!')
        return redirect(url_for('lco'))
    
    return render_template('register.html', title='Register', form=form)

@app.route('/lco', methods=['GET','POST'])
def lco():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = Cook.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            # flash('Invalid username or password')
            return redirect(url_for('lco'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    
    return render_template('login.html', title="Sign In", form=form)



