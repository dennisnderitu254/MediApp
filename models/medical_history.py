#!/usr/bin/python3

from models.basemodel import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship

class MedicalHistory(BaseModel):
   __tablename__ = 'medical_history'

   patient_id = Column(String(36), ForeignKey('patients.id'))
   diagnosis = Column(String(255))
   hospital_of_diagnosis = Column(String(255))
   doctors_name = Column(String(255))
   medication = Column(String(255))
   date_of_diagnosis = Column(Date)

   patient = relationship("Patient", backref="medic_history")

   def __init__(self, patient_id, diagnosis, hospital_of_diagnosis, doctors_name, medication, date_of_diagnosis):
       self.patient_id = patient_id
       self.diagnosis = diagnosis
       self.hospital_of_diagnosis = hospital_of_diagnosis
       self.doctors_name = doctors_name
       self.medication = medication
       self.date_of_diagnosis = date_of_diagnosis
