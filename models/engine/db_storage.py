#!/usr/bin/env/python3
"""DB storage"""


import json
import os
from app import db
from app.models import *
from datetime import datetime

class DBStorage:
    """This alters and modifies the database"""

    DATETIME_FORMAT = '%m/%d/%Y'
    def all(self, cls):
        """Generate all data on a particular class from the db"""
        objs = cls.query.all()
        return objs
    
    def to_json(self, obj):
        """To convert an objects attribute to json"""
        dict_obj = obj.__dict__
        for k, v in dict_obj.items():
            if type(v) == datetime:
                dict_obj[k] = datetime.strftime(DBStorage.DATETIME_FORMAT, v)
        del dict_obj['_sa_instance_state']
        del dict_obj['password_hash']
        return dict_obj

    def get(self, cls, parameter, arg):
        if cls is User:
            if parameter =="id":
                obj = cls.query.filter_by(id=arg).first()
            if parameter == 'email':
                obj = cls.query.filter_by(email=arg).first()
        return obj
    
    def delete(cls, obj):
        """To delete an object from the database"""
        objs = obj.associated()
        db.session.delete(obj)
        for obj in objs:
            db.session.delete(obj)
        db.session.commit()
    
    def save(self):
        """to save changes to the database"""
        db.session.commit()

    def reload(self):
        """reload the database"""
        pass