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
from models import DBStorage
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine.dbstorage import db_storage


app = Flask(__name__)
# db = DBStorage()
# c = db.cursor()
app.config['SECRET_KEY'] = 'secretkey1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root1234@localhost/mediappnewdb'
db = SQLAlchemy(app)

# Configure MySQL connection
# mysql_host = 'localhost'
# mysql_user = 'root'
# mysql_password = 'root1234'
# mysql_database = 'mediappnewdb'


class LoginForm(FlaskForm):
    account_type = SelectField('Select Account Type', choices=[(
        'select', 'Select'), ('doctor', 'Doctor'), ('patient', 'Patient')], validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6)])


def validate_user_credentials(email, password, account_type):
    # Retrieve the user from the database based on email and account type
    user = User.query.filter_by(email=email, role=account_type).first()

    # Check if the user exists and the password matches
    if user and user.password == password:
        return True
    else:
        return False

############# ROUTING FUNCTIONS ###################


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        role = 'user'  # Set the default role

        # Create a new User instance
        user = User(email=email, first_name=first_name,
                    last_name=last_name, password=password, role=role)

        # Add the user to the database
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('registration_success'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        account_type = form.account_type.data
        email = form.email.data
        password = form.password.data

        # Validate the user's credentials against the MySQL database
        if validate_user_credentials(email, password, account_type):
            # Redirect to a success page or perform further actions
            return redirect('/success')
        else:
            # Handle failed login attempts
            error_message = 'Invalid email or password. Please try again.'
            return render_template('login.html', form=form, error_message=error_message)

    return render_template('login.html')


@app.route('/success')
def success():
    # Check if the user is logged in
    if 'account_type' in session:
        account_type = session['account_type']

        # Perform actions based on the account type
        if account_type == 'doctor':
            # Logic for doctor account
            return 'Doctor account'

        elif account_type == 'patient':
            # Logic for patient account
            return 'Patient account'

    # If the user is not logged in or the account type is not recognized, redirect to the login page
    return redirect('/login')


@app.route('/users')
def get_users():
    users = db_storage.get_all_users()
    return render_template('users.html', users=users)


@app.route('/docs_and_apps')
def get_docs_and_apps():
    docs_and_apps, length = db_storage.get_all_docs_and_apps()
    return render_template('docs_and_apps.html', docs_and_apps=docs_and_apps, length=length)


@app.route('/medical_history')
def get_medical_history():
    medical_history = db_storage.get_medical_history()
    return render_template('medical_history.html', medical_history=medical_history)


@app.route('/diagnoses')
def get_diagnoses():
    diagnoses = db_storage.get_diagnoses()
    return render_template('diagnoses.html', diagnoses=diagnoses)


@app.route('/medications')
def get_medications():
    medications = db_storage.get_medications()
    return render_template('medications.html', medications=medications)


@app.route('/previous_doctors')
def get_previous_doctors():
    prev_doctors = db_storage.get_previous_doctors()
    return render_template('previous_doctors.html', prev_doctors=prev_doctors)


@app.route('/calendar')
def get_calendar():
    calendar = db_storage.get_calendar()
    return render_template('calendar.html', calendar=calendar)


@app.route('/registration_success')
def registration_success():
    return 'User registered successfully'


@app.route('/patientdashboard')
def patientdashboard():
    return "patientdashboard"


@app.route('/doctordashboard')
def doctordashboard():
    return "doctordashboard"


if __name__ == '__main__':
    app.run(debug=True)
