#!/usr/bin/python3
"""Defines a class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Class that defines properties of User """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of User.
        """
        super().__init__(*args, **kwargs)
