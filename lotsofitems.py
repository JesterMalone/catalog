from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Clean up DB before inserting:
session.query(Category).delete()
session.query(Item).delete()
session.query(User).delete()

# Create Main User:
User1 = User(name="Jester",
             email="jestermalone@gmail.com",
             picture='http://www.punjabigraphics.com/images/13/baby-face.jpg')
session.add(User1)
session.commit()


# Populate categories:
Category1 = Category(name="Tunes",
                     user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Vehicles",
                     user_id=1)
session.add(Category2)
session.commit

Category3 = Category(name="Weapons",
                     user_id=1)
session.add(Category3)
session.commit()


# Populate Items:
Item1 = Item(name="Isn't It Time - The Alchemical Banditos",
             date=datetime.datetime.now(),
             description="Nothing short of stellar, music.",
             picture="http://mythologian.net/wp-content/uploads/2017/12" +
                     "/Philosophers-Stone-As-An-Alchemy-Symbol-Alchemical" +
                     "-Symbols-And-Their-Meanings.jpg",
             category_id=1,
             user_id=1)
session.add(Item1)
session.commit()

Item2 = Item(name="Money, Drugs, and Sleep - The Politically Correct",
             date=datetime.datetime.now(),
             description="Filth from the cleanest source.",
             picture="https://www.asme.org/getmedia/bfde5e44-5c77-" +
                     "4484-a926-42340862bbd7/Shocking-Purity_hero" +
                     ".jpg.aspx?width=460",
             category_id=1,
             user_id=1)
session.add(Item2)
session.commit()

Item3 = Item(name="I am not a Walrus - The Ticks",
             date=datetime.datetime.now(),
             description="Not the Beatles, definitely not.",
             picture="https://media.wired.com/photos/593221939be5e55" +
                     "af6c234f2/master/w_1164,c_limit/TickTA_" +
                     "GettyImages-128107380.jpg",
             category_id=1,
             user_id=1)
session.add(Item3)
session.commit()

Item4 = Item(name="Electric Scooter",
             date=datetime.datetime.now(),
             description="Wheels, electricity, handlebars.",
             picture="https://www.maxiaids.com/Media/Thumbs/0018/" +
                     "0018048-ewheels-ew-08-fat-tire-electric-" +
                     "scooter-white-300.jpg",
             category_id=2,
             user_id=1)
session.add(Item4)
session.commit()

Item5 = Item(name="Gyro Copter",
             date=datetime.datetime.now(),
             description="Personal propeller system.",
             picture="http://www.buildagyrocopter.com/wp-content/uploads" +
                     "/2018/03/N40KB-Ken-Brock-Gyrocopter.jpg",
             category_id=2,
             user_id=1)
session.add(Item5)
session.commit()

Item6 = Item(name="Leaky Boat",
             date=datetime.datetime.now(),
             description="Probably gonna drown if you use this.",
             picture="https://www.activefisherman.com/wp-content/uploads" +
                     "/2015/01/leaking-boat.jpg",
             category_id=2,
             user_id=1)
session.add(Item6)
session.commit()

Item7 = Item(name="Stick with Duct Tape",
             date=datetime.datetime.now(),
             description="Sticky hit stick.",
             picture="https://cdn0.wideopenspaces.com/wp-content/uploads" +
                     "/2014/10/171.jpg",
             category_id=3,
             user_id=1)
session.add(Item7)
session.commit()

Item8 = Item(name="Shoe with nails",
             date=datetime.datetime.now(),
             description="Spiked Stomp, good for things on the ground.",
             picture="https://images.neimanmarcus.com/ca/2/product_assets" +
                     "/X/4/0/T/Z/NMX40TZ_mz.jpg",
             category_id=3,
             user_id=1)
session.add(Item8)
session.commit()

Item9 = Item(name="Fire glove",
             date=datetime.datetime.now(),
             description="Hot punch.",
             picture="https://ae01.alicdn.com/kf/HTB162UlFY5YBuNjSspoq" +
                     "6zeNFXaH/Free-Shipping-Fire-Magic-Tricks-Stage-Magic" +
                     "-Prop-Magic-Fire-Gloves-for-Magicians.jpg_640x640.jpg",
             category_id=3,
             user_id=1)
session.add(Item9)
session.commit()


print "All your data are belong to us."
