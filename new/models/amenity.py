#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel,Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


<<<<<<< HEAD

class Amenity(BaseModel, Base):
    """Amenity class"""
=======
class Amenity(BaseModel, Base):
>>>>>>> 2b52cc195d188878b4e5aa010ea371ccf8f195c7
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenity)
