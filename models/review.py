#!/usr/bin/python3
"""
This is review class that represents new reviews
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """ Review subclass that inherits from BaseModel """
    len_place_id = ""
    len_user_id = ""
    len_text = ""
