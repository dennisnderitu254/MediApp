#!/usr/bin/python3
import models
from models.admin_model import Admin
from models.appointment_model import Appointment
from models.basemodel import Base, BaseModel
from models.calender_model import Calender
from models.diagnosis_model import Diagnosis
from models.doctor_model import Doctor
from models.medical_history import MedicalHistory
from models.medication_model import Medication
from models.patient_model import Patient
from models.previous_doctor import PreviousDoctor
from models.user_model import User
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        user = "root"
        password = "123456"
        host = "localhost"
        database = "mediapp"
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                        format(user,
                                            password,
                                            host,
                                            database))
    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        self.session.delete(obj)

