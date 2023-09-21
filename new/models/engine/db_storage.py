#!/usr/bin/python3
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
    
class DBStorage:
    __engine = None
    __session = None

    
    def __init__(self):
        """
        Initializes the DBStorage object and establishes 
        a connection to the MySQL database.
        """
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}",
            pool_pre_ping=True
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        bucket = {}
        classes_to_query = [User, State, City, Amenity, Place, Review]

        if cls:
            if isinstance(cls, str):
                cls = eval(cls)

            instances = self.__session.query(cls).all()
            for instance in instances:
                key = f"{instance.__class__.__name__}.{instance.id}"
                bucket[key] = instance

        else:
            for cls in classes_to_query:
                instances = self.__session.query(cls).all()
                for instance in instances:
                    key = f"{instance.__class__.__name__}.{instance.id}"
                    bucket[key] = instance

        return bucket

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
