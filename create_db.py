from app import db
from app import models
db.create_all()

# Restaurants

rest1 = models.Restaurant(
    name = "GoodPlace",
    description = "Important restaurant with stuff"
)

rest2 = models.Restaurant(
    name = "Bad Place",
    description = "Come get some bad food "
)

# Menu Items

mi11 = models.Menu_Item(
    name="Big Dish",
    description="Very big and tasty",
    price="23.0",
    restaurant_id=rest1.id
)

mi12 = models.Menu_Item(
    name="Small Dish",
    description="Very small and smelly",
    price="3.0",
    restaurant_id=rest1.id
)

mi21 = models.Menu_Item(
    name="Bad Dish",
    description="Very bad and nasty",
    price="23.0",
    restaurant_id=rest2.id
)

mi22 = models.Menu_Item(
    name="Small Baddy",
    description="Tiny portion",
    price="3.0",
    restaurant_id=rest2.id
)

rest1.menu_items.append(mi11)
rest1.menu_items.append(mi12)

rest2.menu_items.append(mi21)
rest2.menu_items.append(mi22)

db.session.add(rest1)
db.session.add(mi11)
db.session.add(mi12)

db.session.add(rest2)
db.session.add(mi21)
db.session.add(mi22)

user1 = models.Customer(username="jason", email="jason@gmail.com")
user1.set_password("jason")

user2 = models.Customer(username="paul", email="paul@gmail.com")
user2.set_password("paul")

db.session.add(user1)
db.session.add(user2)

# Managers

manager1 = models.Manager(username="pat", email="pat@gmail.com")
manager1.set_password("pat")

manager2 = models.Manager(username="sal", email="sal@gmail.com")
manager2.set_password("sal")

rest1.manager.append(manager1)
rest2.manager.append(manager2)

db.session.add(manager1)
db.session.add(manager2)

# Cooks

cook1 = models.Cook(username = "khan", email="khan@gmail.com")
cook1.set_password("khan")

cook2 = models.Cook(username = "sal", email="sal@gmail.com")
cook2.set_password("sal")

cook3 = models.Cook(username = "jason", email="jason@gmail.com")
cook3.set_password("jason")

cook4 = models.Cook(username = "abu", email="abu@gmail.com")
cook4.set_password("abu")

cook5 = models.Cook(username = "paul", email="paul@gmail.com")
cook5.set_password("paul")

cook6 = models.Cook(username = "pavlo", email="pavlo@gmail.com")
cook6.set_password("pavlo")


db.session.add(cook1)
db.session.add(cook2)
db.session.add(cook3)
db.session.add(cook4)
db.session.add(cook5)
db.session.add(cook6)


db.session.commit()
