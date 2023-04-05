#!/usr/bin/python3
"""Returns all data"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class DBStorage:
    """Returns all data"""
    __engine = None
    __session = None

    tables = {
        'State': State,
        'City': City,
        'User': User,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        metadata = MetaData(bind=self.__engine)

        if os.getenv('HBNB_ENV') == "test":
            metadata.reflect(bind=self.__engine)
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns all data"""
        new_dict = {}
        if cls is not None:
            name = DBStorage.tables[cls]
            all_obj = self.__session.query(name).all()
            for obj in all_obj:
                index = obj.to_dict()['__class__'] + '.' + obj.id
                new_dict[index] = obj
        else:
            for elem in DBStorage.tables.values():
                all_obj = self.__session.query(elem).all()
                for obj in all_obj:
                    index = obj.to_dict()['__class__'] + '.' + obj.id
                    new_dict[index] = obj
        return new_dict

    def new(self, obj):
        """Returns all data"""
        self.__session.add(obj)

    def save(self):
        """Returns all data"""
        self.__session.commit()

    def delete(self, obj=None):
        """Returns all data"""
        if obj is not None:
            name = DBStorage.tables[obj.__class__.__name__]
            x = self.__session.query(name).filter(name.id == obj.id).first()
            self.__session.delete(x)
            self.save()

    def reload(self):
        """Returns all data"""
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
        Base.metadata.create_all(self.__engine)

    def close(self):
        """Close the sessions"""
        self.__session.remove()
