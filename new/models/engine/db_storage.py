#!/usr/bin/python3
from os import getenv
from typing import Dict, Optional, Type

    
class DBStorage:
    __engine = None
    __session = None

    def __init__(self) -> None:
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

    def all(self, cls: Optional[Type] = None) -> Dict[str, object]:
        """
        Retrieves all instances of a specific class from the database.
        If no class is specified, retrieves all instances from all classes.
        """
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
