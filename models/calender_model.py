#!/usr/bin/python3

from basemodel import BaseModel
import sqlalchemy
from sqlalchemy import Columns, String, PrimaryKey, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Calendar(BaseModel):
    __tablename__ = 'calendar'

    doctor_id = Column(String(36), ForeignKey('doctors.id'), nullable=False)
    appointment_datetime = Column(DateTime, nullable=False)

    doctor = relationship("Doctor", backref="calendar")

    def __init__(self, doctor_id, appointment_datetime):
        self.doctor_id = doctor_id
        self.appointment_datetime = appointment_datetime
