#!/usr/bin/python3
""" User Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """The user class, contains email and password"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
<<<<<<< HEAD
    places = relationship("Place", backref="user", cascade="all, delete")
    reviews = relationship("Review", backref="user", cascade="all, delete")
=======
    places = relationship("Place", backref="user", cascade="all, delete, delete_orphan")
    reviews = relationship("Review", backref="user", cascade="all, delete, delete_orphan")
>>>>>>> 2b52cc195d188878b4e5aa010ea371ccf8f195c7
