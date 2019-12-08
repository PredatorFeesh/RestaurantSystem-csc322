from app import db
from app import models
db.create_all()

rest1 = models.Restaurant(
    name = "GoodPlace",
    description = "Important restaurant with stuff"
)

rest2 = models.Restaurant(
    name = "Bad Place",
    description = "Come get some bad food "
)

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

user = models.Customer(username="jason", email="jason@gmail.com")
user.set_password("jason")

db.session.add(user)

db.session.commit()
