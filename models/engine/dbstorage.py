#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import models

from models.basemodel import Base, BaseModel
from models.user_model import User
from models.admin_model import Admin
from models.doctor_model import Doctor
from models.patient_model import Patient
from models.appointments_model import Appointment
from models.calender_model import Calendar
from models.diagnosis_model import Diagnosis
from models.medical_history import MedicalHistory
from models.medication_model import Medication
from models.previous_doctor import PreviousDoctor


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        user = "root"
        password = "root1234"
        host = "localhost"
        database = "mediappnewdb"
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

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def get_all_users(self):
        result = self.__session.execute("SELECT * FROM users")
        users = result.fetchall()
        return users

    def get_all_docs_and_apps(self):
        result = self.__session.execute("SELECT * FROM appointments")
        docs_and_apps = result.fetchall()
        l = len(docs_and_apps)
        return docs_and_apps, l

    def get_medical_history(self):
        result = self.__session.execute("SELECT * FROM medical_history")
        medical_history = result.fetchall()
        return medical_history

    def get_diagnoses(self):
        result = self.__session.execute("SELECT * FROM diagnoses")
        diagnoses = result.fetchall()
        return diagnoses

    def get_medications(self):
        result = self.__session.execute("SELECT * FROM medications")
        medications = result.fetchall()
        return medications

    def get_previous_doctors(self):
        result = self.__session.execute("SELECT * FROM previous_doctors")
        prev_doctors = result.fetchall()
        return prev_doctors

    def get_calendar(self):
        result = self.__session.execute("SELECT * FROM calendar")
        calendar = result.fetchall()
        return calendar


db_storage = DBStorage()
db_storage.reload()
