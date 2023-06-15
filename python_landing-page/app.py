#!/usr/bin/python3
import os
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, Blueprint
from models import storage
from models.admin_model import Admin
from models.appointments_model import Appointment
from models.basemodel import Base, BaseModel
from models.calender_model import Calendar
from models.diagnosis_model import Diagnosis
from models.doctor_model import Doctor
from models.medical_history import MedicalHistory
from models.medication_model import Medication
from models.patient_model import Patient
from models.previous_doctor import PreviousDoctor
from models.user_model import User
from app_views import app_views
from main import main

load_dotenv()

app = Flask(__name__)

# Registering the app_views blueprint

app.register_blueprint(app_views)

# Registering the main blueprint

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
