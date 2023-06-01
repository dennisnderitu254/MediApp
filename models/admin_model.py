#!/usr/bin/python3

from models.basemodel import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Admin(BaseModel):
    __tablename__ = 'admins'

    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)

    user = relationship("User", backref="admin", uselist=False)

    def __init__(self, user_id):
        self.user_id = user_id
