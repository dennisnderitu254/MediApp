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


app = Flask(__name__)
# db = DBStorage()
# c = db.cursor()
app.config['SECRET_KEY'] = 'secretkey1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root1234@localhost/mediappnewdb'
db = SQLAlchemy(app)

# Configure MySQL connection
mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = 'root1234'
mysql_database = 'mediappnewdb'


# class LoginForm(FlaskForm):
#     account_type = StringField('Account Type', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])

class LoginForm(FlaskForm):
    account_type = SelectField('Select Account Type', choices=[(
        'select', 'Select'), ('doctor', 'Doctor'), ('patient', 'Patient')], validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6)])


def validate_user_credentials(email, password):
    try:
        # Establish connection to the MySQL database
        conn = sqlalchemy.create_engine(
            f'mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_database}'
        )

        # Execute a query to retrieve the user's credentials
        query = f"SELECT * FROM users WHERE email = '{email}'"
        result = conn.execute(query)

        # Fetch the user record
        user = result.fetchone()

        # Validate the user's credentials
        if user and password == user.password:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the database connection
        if conn:
            conn.dispose()


################## ROUTING FUNCTIONS #########################

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
        if validate_user_credentials(email, password):
            # Redirect to a success page or perform further actions
            return redirect('/success')
        else:
            # Handle failed login attempts
            error_message = 'Invalid email or password. Please try again.'
            return render_template('login.html', form=form, error_message=error_message)
    return render_template('login.html', form=form)


@app.route('/registration_success')
def registration_success():
    return 'User registered successfully'


@app.route('/success')
def success():
    return "Login successful!"


if __name__ == '__main__':
    app.run(debug=True)
