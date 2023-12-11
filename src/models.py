import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    user_name = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(20))

class Post(Base):
    __tablename__ = 'Posts'
    id = Column(Integer, primary_key=True)
    img_url = Column(String(500), nullable=False)
    title = Column(String(30), nullable=False)
    description = Column(String(2000))
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'Comments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('Posts.id'))
    post = relationship(Post)
    content = Column(String(1000), nullable=False)

class ReactionType(Base):
    __tablename__ = 'ReactionTypes'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    icon_url = Column(String(500), nullable=False)

class Reaction(Base):
    __tablename__ = 'Reactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('Posts.id'))
    post = relationship(Post)
    reaction_type_id = Column(Integer, ForeignKey('ReactionTypes.id'))
    reaction = relationship(ReactionType)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
