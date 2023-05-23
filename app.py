from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret1234'

admin_role = Role(name='admin')
doctor_role = Role(name='doctor')
patient_role = Role(name='patient')

db.session.add_all([admin_role, doctor_role, patient_role])
db.session.commit()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.patient_loader
def load_patient(patient_id):
    return Patient.query.get(int(patient_id))


@login_manager.doctor_loader
def load_doctor(doctor_id):
    return Doctor.query.get(int(doctor_id))


@login_manager.doctor_loader
def load_doctor(patient_id):
    return Doctor.query.get(int(patient_id))


class Patient(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), unique=True)
    last_name = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))


class Doctor(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), unique=True)
    last_name = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class Appointment(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, unique=True)
    doctor_id = db.Column(db.Integer, unique=True)
    date = db.Column(db.String(150), unique=True)
    time = db.Column(db.String(150), unique=True)
    reason = db.Column(db.String(150), unique=True)
    status = db.Column(db.String(150), unique=True)


class Prescription(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, unique=True)
    doctor_id = db.Column(db.Integer, unique=True)
    date = db.Column(db.String(150), unique=True)
    time = db.Column(db.String(150), unique=True)
    reason = db.Column(db.String(150), unique=True)
    status = db.Column(db.String(150), unique=True)
    prescription = db.Column(db.String(150), unique=True)


class MedicalHistory(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, unique=True)
    doctor_id = db.Column(db.Integer, unique=True)
    date = db.Column(db.String(150), unique=True)
    time = db.Column(db.String(150), unique=True)
    reason = db.Column(db.String(150), unique=True)
    status = db.Column(db.String(150), unique=True)
    prescription = db.Column(db.String(150), unique=True)
    medical_history = db.Column(db.String(150), unique=True)


class Payment(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, unique=True)
    doctor_id = db.Column(db.Integer, unique=True)
    date = db.Column(db.String(150), unique=True)
    time = db.Column(db.String(150), unique=True)
    reason = db.Column(db.String(150), unique=True)
    status = db.Column(db.String(150), unique=True)
    prescription = db.Column(db.String(150), unique=True)
    medical_history = db.Column(db.String(150), unique=True)
    payment = db.Column(db.String(150), unique=True)


class Message(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, unique=True)
    doctor_id = db.Column(db.Integer, unique=True)
    date = db.Column(db.String(150), unique=True)
    time = db.Column(db.String(150), unique=True)
    reason = db.Column(db.String(150), unique=True)
    status = db.Column(db.String(150), unique=True)
    prescription = db.Column(db.String(150), unique=True)
    medical_history = db.Column(db.String(150), unique=True)
    payment = db.Column(db.String(150), unique=True)
    message = db.Column(db.String(150), unique=True)


class Chat(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, unique=True)
    doctor_id = db.Column(db.Integer, unique=True)
    date = db.Column(db.String(150), unique=True)
    time = db.Column(db.String(150), unique=True)
    reason = db.Column(db.String(150), unique=True)
    status = db.Column(db.String(150), unique=True)
    prescription = db.Column(db.String(150), unique=True)
    medical_history = db.Column(db.String(150), unique=True)
    payment = db.Column(db.String(150), unique=True)
    message = db.Column(db.String(150), unique=True)
    chat = db.Column(db.String(150), unique=True)


class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login_patient():
    form = LoginForm()
    if form.validate_on_submit():
        user = Patient.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login_patient.html', form=form)


def login_doctor():
    form = LoginForm()
    if form.validate_on_submit():
        user = Doctor.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login_doctor.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def doctor_dashboard():
    return render_template('doctor_dashboard.html')


def patient_dashboard():
    return render_template('patient_dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/admin')
@login_required
def admin_route():
    if current_user.role.name == 'admin':
        # Admin route logic
        return 'Admin Route'
    else:
        return 'Unauthorized Access'


if __name__ == '__main__':
    app.run(debug=True)
