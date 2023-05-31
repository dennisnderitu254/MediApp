#!/usr/bin/python3

from basemodel import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, PrimaryKey, ForeignKey
from sqlalchemy.orm import relationship


class Appointment(BaseModel):
    __tablename__ = 'appointments'

    patient_id = Column(String(36), ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(String(36), ForeignKey('doctors.id'), nullable=False)
    appointment_datetime = Column(DateTime, nullable=False)
    status = Column(String(20), nullable=False)
    feedback = Column(String(255), nullable=True)

    patient = relationship("Patient", backref="appointments")
    doctor = relationship("Doctor", backref="appointments")

    def __init__(self, patient_id, doctor_id, appointment_datetime, status,
                 feedback=None):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_datetime = appointment_datetime
        self.status = status
        self.feedback = feedback
