## Mediapp

This is a Detailed display of the MediApp Web Application

## Getting Started with Mediapp

Mediapp is an online web application that connects patients to doctors. The patient is able to access proper health care from doctors and the doctors are able to increase reach to patients in a wide geographical area as well as offer quality medical care online.

## Problem Statement

According to BMC Public Health, Access to primary healthcare is crucial for the delivery of Kenya’s universal health coverage policy. However, disparities in healthcare have proved to be the biggest challenge for implementing primary care in poor-urban resource settings.
Some Patients, Lack access to counsel from the best medical practitioners in the country, which leads to some people not getting the best medical attention from the best doctors in the country. The Doctors, on their Side, Not having the ability to offer medical counsel to patients, regardless of geographical location, this also affects the ability of the Doctor to offer his/her services to patients.

## Challenge Statement

The Mediapp is an online platform that will serve to connect patients to Healthcare from Doctors despite physical locations. Patients will have the ability to have virtual consultations with the doctors.

## Technology Stack

- Frontend – HTML and CSS
- Backend – Flask(Python)
- Database – mysql

## Users

Two main types of users

- Patient
- Doctor

Super User

- ADMIN

## User Authentication

The Frontend was done in HTML and CSS

The Backend was done in Python Flask

## MediApp User Stories

User Story: As a patient with a medical condition, I want to use a user-friendly web app to efficiently manage my appointments and access relevant information, ensuring a smooth experience during my medical visits.

Acceptance Criteria:

1. As a patient, I can create a secure account with my personal information, including name, contact details, and medical history.

2. Upon logging in, I am presented with a clear and intuitive dashboard that displays my upcoming appointments and relevant notifications.

3. I can easily schedule a new appointment by selecting a preferred date, time, and healthcare provider from a comprehensive list.

4. The web app should provide the user with timely reminders and notifications for upcoming appointments via email or SMS, allowing me to plan accordingly.

5. Within the app, I can access and review my medical records, including previous diagnoses, test results, and treatment plans, enabling me to stay informed and involved in my healthcare journey.

6. I have the ability to securely communicate with healthcare providers through a messaging feature, allowing me to ask questions, request prescription refills, or share relevant updates.

7. In case of any changes or cancellations to my scheduled appointments, I receive immediate notifications and can easily reschedule using the app.

8. The web app should be responsive and accessible across different devices, ensuring a seamless user experience on desktops, laptops, tablets, and smartphones.

9. The app prioritizes privacy and security, ensuring that my personal and medical information is encrypted and protected from unauthorized access.

10. The web app provides a support system or FAQ section, offering guidance and assistance for any technical issues or general inquiries I may have.

## Database Models

The method used here was the utilization of database models, build on python, that generated the tables for the database, using the flask web framework.

This allowed us to make sure all our data would fit into one place without having multiple files scattered

This Code is the engine that allowed database connection as well as data storage in the database

```
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

```

There's also the creation of class Models, that were pivotal in making the database

```
Admin Model

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


```

```
Appointments Model

#!/usr/bin/python3

from models.basemodel import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Date
from sqlalchemy.orm import relationship


class Appointment(BaseModel):
    __tablename__ = 'appointments'

    patient_id = Column(String(36), ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(String(36), ForeignKey('doctors.id'), nullable=False)
    appointment_datetime = Column(Date, nullable=False)
    status = Column(String(20), nullable=False)
    feedback = Column(String(255), nullable=True)

    patient = relationship("Patient", backref="appointments")
    doctor = relationship("Doctor", backref="appointments")

    def __init__(self, patient_id, doctor_id, appointment_datetime, status, feedback=None):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_datetime = appointment_datetime
        self.status = status
        self.feedback = feedback
```

```
Base Model

from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
```

```
Calendar Model

#!/usr/bin/python3

from models.basemodel import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Calendar(BaseModel):
    __tablename__ = 'calendar'

    doctor_id = Column(String(36), ForeignKey('doctors.id'), nullable=False)
    appointment_datetime = Column(DateTime, nullable=False)

    doctor = relationship("Doctor", backref="calendar")

    def __init__(self, doctor_id, appointment_datetime):
        self.doctor_id = doctor_id
        self.appointment_datetime = appointment_datetime
```

```
Class diagnosis

#!/usr/bin/python3

from models.basemodel import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Diagnosis(BaseModel):
    __tablename__ = 'diagnoses'

    appointment_id = Column(String(36), ForeignKey('appointments.id'), nullable=False)
    diagnosis_details = Column(String(255), nullable=False)

    appointment = relationship("Appointment", backref="diagnosis")

    def __init__(self, appointment_id, diagnosis_details):
        self.appointment_id = appointment_id
        self.diagnosis_details = diagnosis_details
```

```
Doctor Model

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
```

```
Class Medical History

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
```

```
Class Medication Model

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
```

```
Patient Model

#!/usr/bin/python3

from models.basemodel import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Patient(BaseModel):
    __tablename__ = 'patients'

    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    medical_history = Column(String(255), nullable=True)

    user = relationship("User", backref="patient", uselist=False)

    def __init__(self, user_id, medical_history=None):
        self.user_id = user_id
        self.medical_history = medical_history
```

```
Class Previous Doctor Model

#!/usr/bin/python3

from models.basemodel import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class PreviousDoctor(BaseModel):
    __tablename__ = 'previous_doctors'

    patient_id = Column(String(36), ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(String(36), ForeignKey('doctors.id'), nullable=False)

    patient = relationship("Patient", backref="previous_doctors")
    doctor = relationship("Doctor", backref="previous_patients")

    def __init__(self, patient_id, doctor_id):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
```

```
Class User Model

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
```
