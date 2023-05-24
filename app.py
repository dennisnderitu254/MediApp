from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'kenya1234'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root1234'
app.config['MYSQL_DB'] = 'mediappdb'

mysql = MySQL(app)


@app.route('/')
@app.route('/loginpatient', methods=['GET', 'POST'])
def login_patient():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM patient WHERE email = % s AND password = % s', (email, password, ))
        patient = cursor.fetchone()
        if patient:
            session['loggedin'] = True
            session['patientid'] = patient['patientid']
            session['name'] = patient['name']
            session['email'] = patient['email']
            mesage = 'Logged in successfully !'
            return render_template('user.html', mesage=mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage=mesage)


@app.route('/logindoctor', methods=['GET', 'POST'])
def login_doctor():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM doctor WHERE email = % s AND password = % s', (email, password, ))
        doctor = cursor.fetchone()
        if doctor:
            session['loggedin'] = True
            session['doctorid'] = doctor['doctorid']
            session['name'] = doctor['name']
            session['email'] = doctor['email']
            mesage = 'Logged in successfully !'
            return render_template('user.html', mesage=mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage=mesage)


@app.route('/registerpatient', methods=['GET', 'POST'])
def register_patient():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        dateofbirth = request.form['dateofbirth']
        gender = request.form['gender']
        phonenumber = request.form['phonenumber']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM patient WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not username or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute(
                'INSERT INTO patient VALUES (NULL, % s, % s, % s, %s, %s, %s, %s, %s)', (firstname, lastname, dateofbirth, gender, phonenumber, username, email, password, ))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage=mesage)


@app.route('/registerdoctor', methods=['GET', 'POST'])
def register_doctor():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        dateofbirth = request.form['dateofbirth']
        gender = request.form['gender']
        phonenumber = request.form['phonenumber']
        specialization = request.form['specialization']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM patient WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not username or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute(
                'INSERT INTO patient VALUES (NULL, % s, % s, % s, %s, %s, %s, %s, %s)', (firstname, lastname, dateofbirth, gender, phonenumber, specialization, username, email, password, ))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage=mesage)


if __name__ == "__main__":
    app.run()