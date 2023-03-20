#!/usr/bin/python3

import sqlalchemy
from sqlalchemy import (create_engine)
from models.base_model import BaseModel, Base
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER', default=None)
        pwd = os.getenv('HBNB_MYSQL_PWD', default=None)
        host = os.getenv('HBNB_MYSQL_HOST', default=None)
        db = os.getenv('HBNB_MYSQL_DB', default=None)
        print(user, pwd, host, db)
        return
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        metadata = MetaData(bind=self.__engine)

        if HBNB_ENV == "test":
            metadata.reflect(bind=self.__engine)
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        new_dict = {}
        print(cls)
        if cls != None:
            all_obj = self.__session.query(cls).fetchall()
        else:
            all_obj = self.__session.query().fetchall()
        for obj in all_obj:
            index = obj.to_dict()['__class__'] + '.' + obj.id
            new_dict[index] = obj
        return new_dict
