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
from models import DBStorage, Admin


app = Flask(__name__)
db = DBStorage()


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/userreg')
def user_reg():
    return render_template('userregistration.html')


@app.route('/loginpage')
def loginpage1():
    return render_template('loginpage.html')

# User Login Page


@app.route('/userlogin', methods=['GET', 'POST'])
def userlogin():
    email = request.form['email']
    password = request.form['password']

    # Retrieve user from the database based on email and password
    user = db_session.query(User).filter_by(
        email=email, password=password).first()

    if user:
        # User login successful
        # Perform any additional actions or redirections
        return render_template('index.html', mess='User login successful.')
    else:
        # Invalid credentials
        return render_template('loginpage.html', err='Please enter correct credentials.')


# Functions for adding User
@app.route('/adduser', methods=['POST'])
def add_user():
    email = request.form['email']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    password = request.form['password']

    # Create a new User object
    user = User(email=email, first_name=firstname,
                last_name=lastname, password=password)

    # Add the User object to the session
    db_session.add(user)

    try:
        # Commit the changes to the database
        db_session.commit()

        return render_template('home.html', mess=f"User {firstname} {lastname} added successfully.")
    except sqlalchemy.exc.SQLAlchemyError as error:
        # Handle any database errors
        return render_template('home.html', mess='Error occurred while adding user.')


@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query the database for an admin with the provided username and password
        admin = db.session.query(Admin).join(Admin.user).filter(
            User.email == username,
            User.password == password
        ).first()

        if admin:
            # Admin login successful
            session['admin_id'] = admin.id
            return redirect(url_for('admin_dashboard'))
        else:
            # Invalid credentials
            return render_template('admin_login.html', error='Invalid username or password.')
    return render_template('admin_login.html')


@app.route('/admindashboard')
def admin_dashboard():
    # Check if admin is logged in
    if 'admin_id' in session:
        admin_id = session['admin_id']
        # Retrieve admin information from the database based on admin_id
        admin = db.session.query(Admin).get(admin_id)
        if admin:
            # Admin dashboard page
            return render_template('admin_dashboard.html', admin=admin)

    # Admin is not logged in, redirect to login page
    return redirect(url_for('adminlogin'))
