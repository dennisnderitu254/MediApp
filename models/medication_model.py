#!/usr/bin/python3

from models.basemodel import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Medication(BaseModel):
    __tablename__ = 'medications'

    patient_id = Column(String(36), ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(String(36), ForeignKey('doctors.id'), nullable=False)
    medication_details = Column(String(255), nullable=False)

    patient = relationship("Patient", backref="medications")
    doctor = relationship("Doctor", backref="medications")

    def __init__(self, patient_id, doctor_id, medication_details):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.medication_details = medication_details
