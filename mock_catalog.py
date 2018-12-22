#this file creates temporary placeholder for the test environment of my aplication.

#Connects to the database
#IMPORTANT: make sure you have previously created the database with the database_setup.py file
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

import datetime

engine = create_engine('sqlite:///catalogproject.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#Create 3 fake users
user1 = User(name='Luma', email='luma@gmail.com', create_date=datetime.datetime.now())

session.add(user1)
session.commit()

user2 = User(name='Zezinho', email='zezinho@gmail.com', create_date=datetime.datetime.now())

session.add(user2)
session.commit()

user3 = User(name='Celia', email='celia@gmail.com', create_date=datetime.datetime.now())

session.add(user3)
session.commit()


#create 3 fake categories and its itens

category1 = Category(name='Cores', description='todas as cores do mundo', last_edit=datetime.datetime.now(), user=user1)

session.add(category1)
session.commit()

item1 = Item(name='Azul', description='da cor do mar', price=24.5, category=category1, last_edit=datetime.datetime.now(), user=category1.user)

session.add(item1)
session.commit()

item2 = Item(name='Verde', description='da cor da flores', price=29.5, category=category1, last_edit=datetime.datetime.now(), user=category1.user)

session.add(item2)
session.commit()

item3 = Item(name='Vermelho', description='da cor do coracao', price=39.9, category=category1, last_edit=datetime.datetime.now(), user=category1.user)

session.add(item3)
session.commit()

category2 = Category(name='Dias', description='da semana', last_edit=datetime.datetime.now(), user=user2)

session.add(category2)
session.commit()

item1_dia = Item(name='Segunda', description='Pior dia', price=9.99, category=category2, last_edit=datetime.datetime.now(), user=category2.user)

session.add(item1_dia)
session.commit()

item2_dia = Item(name='Domingo', description='Fantastico!', price=0.9, category=category1, last_edit=datetime.datetime.now(), user=category1.user)

session.add(item2_dia)
session.commit()

item3_dia = Item(name='Sexta', description='Dia da maldade', price=99.9, category=category1, last_edit=datetime.datetime.now(), user=category1.user)

session.add(item3_dia)
session.commit()
