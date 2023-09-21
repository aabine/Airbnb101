import os
from sqlalchemy.engine.url import URL
#!/usr/bin/python3
from os import getenv, environ
from typing import Dict, Optional, Type

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    __engine = None
    __session = None
    __class_mapping = [User, State, City, Amenity, Place, Review]

    def __init__(self) -> None:
        """
        Initializes the DBStorage object and establishes 
        a connection to the MySQL database.
        """
        user = environ['HBNB_MYSQL_USER']
        passwd = environ['HBNB_MYSQL_PWD']
        db = environ['HBNB_MYSQL_DB']
        url = URL(
            drivername='mysql+mysqldb',
            username=user,
            password=passwd,
            host='localhost',
            port=3306,
            database=db
        )
        self.__engine = create_engine(url, pool_pre_ping=True)
        if environ["HBNB_ENV"] == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls: Optional[Type] = None) -> Dict[str, object]:
        """
        Retrieves all instances of a specific class from the database.
        If no class is specified, retrieves all instances from all classes.
        """
        bucket = {}

        if cls:
            if isinstance(cls, str):
                cls = self.__class_mapping.get(cls)

            instances = self.__session.query(cls).all()
            for instance in instances:
                key = f"{instance.__class__.__name__}.{instance.id}"
                bucket[key] = instance

        else:
            for cls in self.__class_mapping:
                instances = self.__session.query(cls).all()
                for instance in instances:
                    key = f"{instance.__class__.__name__}.{instance.id}"
                    bucket[key] = instance

        return bucket

    def new(self, obj: object) -> None:
        """
        Adds a new instance to the database session.
        """
        self.__session.add(obj)

    def save(self) -> None:
        """
        Commits the changes made in the database session.
        """
        self.__session.commit()

    def delete(self, obj: object) -> None:
        """
        Deletes an instance from the database session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self) -> None:
        """
        Creates the database tables if they don't exist and creates a new session.
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self) -> None:
        """
        Closes the database session.
        """
        self.__session.close()
