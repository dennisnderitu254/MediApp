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
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# db = DBStorage()
# c = db.cursor()
app.config['SECRET_KEY'] = 'secretkey1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root1234@localhost/mediappnewdb'
db = SQLAlchemy(app)


class LoginForm(FlaskForm):
    account_type = StringField('Account Type', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


################## ROUTING FUNCTIONS #########################

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
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

        return 'User registered successfully'

    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
