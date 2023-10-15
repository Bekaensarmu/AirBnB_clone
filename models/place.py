#!/usr/bin/python3
"""
Place module
"""
from models.base_model import BaseModel

class Place(BaseModel):
    """
    Class Place
    """
    len_city_id = ""
    len_user_id = ""
    len_name = ""
    len_description = ""
    len_number_rooms = 0
    len_number_bathrooms = 0
    len_max_guest = 0
    len_price_by_night = 0
    len_latitude = 0.0
    len_longitude = 0.0
    len_amenity_ids = []
