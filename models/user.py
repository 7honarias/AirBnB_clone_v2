#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(string(128), nullable=False)
    password = Column(string(128), nullable=False)
    first_name = Column(string(128))
    last_name = Column(string(128))

    def __init__(self, *args, **kwargs):
        """ Initialitation """
        def super().__init__(*args, **kwargs)
