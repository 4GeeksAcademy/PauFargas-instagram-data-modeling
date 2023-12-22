import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=True)
    email = Column(String(50), nullable=False, unique=True )


class Followers(Base):
    __tablename__= 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user'))
    user_to_id = Column(Integer, ForeignKey('user'))

    user_from = relationship(Users)
    user_to = relationship(Users)


class Posts(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    post_rel = relationship(Users)


class Media(Base):
    __tablename__='media'
    id = Column(Integer, primary_key=True)
    type_of_media = Column(String)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('post.user_id'))


class Coments(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String)
    author_id = Column(Integer, ForeignKey('user.id')) 
    post_id = Column(Integer, ForeignKey('post.id')) 

    authory = relationship(Users)
    post_comments = relationship(Posts)



'''class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}'''


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
