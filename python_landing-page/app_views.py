from flask import Blueprint, render_template, url_for

app_views = Blueprint('app_views', __name__)


@app_views.route('/')
def index():
    return render_template('index.html', url_for=url_for)

@app_views.route('/register')
def display_reg_form():
    return render_template('registration-form.html')

@app_views.route('/product_page')
def display_product():
    return render_template('product_page.html')

@app_views.route('/doctor')
def doctor():
    return render_template('doc_dashboard.html')
