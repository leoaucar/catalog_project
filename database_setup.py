import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, Float, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


####################tables######################

class User(Base):

    __tablename__ = 'user'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    email = Column(String(80), nullable = False)
    create_date = Column(Date, nullable = False)


class Category(Base):

    __tablename__ = 'category'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(280))
    last_edit = Column(Date, nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    spotlight = Column(Boolean)

class Item(Base):

    __tablename__ = 'item'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(280))
    price = Column(Float(8))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    last_edit = Column(Date, nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    spotlight = Column(Boolean)


###############Json endpoint####################
    @property
    def serialize(self):

        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
        }


##############create database##################3
engine = create_engine('sqlite:///catalogproject.db')

Base.metadata.create_all(engine)
