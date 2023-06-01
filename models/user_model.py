#!/usr/bin/python3

from models.basemodel import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel):
    __tablename__ = 'users'

    email = Column(String(255), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)

    def __init__(self, email, first_name, last_name, password, role):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.role = role
