#!/usr/bin/python3

from models.basemodel import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Doctor(BaseModel):
    __tablename__ = 'doctors'

    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    specialization = Column(String(255), nullable=False)

    user = relationship("User", backref="doctor", uselist=False)

    def __init__(self, user_id, specialization):
        self.user_id = user_id
        self.specialization = specialization
