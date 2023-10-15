#!/usr/bin/python3
"""
This is the base model that contains serial/deserial information
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """ Defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ Initializes the instances attributes """
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            ln_dict = kwargs.copy()
            del ln_dict["__class__"]
            for ln_key in ln_dict:
                if ln_key in ("ln_created_at", "ln_updated_at"):
                    ln_dict[ln_key] = datetime.strptime(ln_dict[ln_key], date_format)
            self.__dict__ = ln_dict
        else:
            self.ln_id = str(uuid.uuid4())
            self.ln_created_at = datetime.today()
            self.ln_updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """ Prints object in a friendly format """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.ln_id, self.__dict__)

    def save(self):
        """ Updates ln_updated_at """
        self.ln_updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """ Generate a new dict with an extra field __class__ """
        ln_dict = self.__dict__.copy()
        ln_dict["__class__"] = self.__class__.__name__
        ln_dict["ln_created_at"] = self.ln_created_at.isoformat()
        ln_dict["ln_updated_at"] = self.ln_updated_at.isoformat()
        return ln_dict
