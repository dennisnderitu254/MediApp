#!/usr/bin/python3

from models.basemodel import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Date
from sqlalchemy.orm import relationship

class Calendar(BaseModel):
    __tablename__ = 'calendar'

    doctor_id = Column(String(36), ForeignKey('doctors.id'), nullable=False)
    appointment_date = Column(Date, nullable=False)
    appointment_time = Column(String(255))

    doctor = relationship("Doctor", backref="calendar")

    def __init__(self, doctor_id, appointment_time, appointment_date):
        self.doctor_id = doctor_id
        self.appointment_datetime = appointment_datetime
