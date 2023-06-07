#!/usr/bin/python3

import re
from flask import Flask, render_template, request, redirect, url_for, session
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


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/loginp')
@app.route('/loginpatient')
def login_patient():
    message = 'Welcome User!'
    return render_template('patientlogin.html', message=message)


@app.route('/logind')
@app.route('/logindoctor')
def login_doctor():
    message = 'Welcome Doctor'
    return render_template('doctorlogin.html', message=message)


@app.route('/registerp')
@app.route('/registerpatient', methods=['GET', 'POST'])
def register_patient():
    message = 'Welcome Patient'
    return render_template('patientregister.html', message=message)


@app.route('/registerd')
@app.route('/registerdoctor', methods=['GET', 'POST'])
def register_doctor():
    message = 'Welcome Doctor'
    return render_template('doctorregister.html', message=message)


@app.route('/loginadmin')
@app.route('/admin')
def admin_login():
    message = 'Welcome Admin'
    return render_template('adminlogin.html', message=message)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('doctorid', None)
    session.pop('patientid', None)
    session.pop('email', None)
    return redirect(url_for('login'))
