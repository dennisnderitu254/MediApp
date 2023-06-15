from flask import Blueprint, redirect, request
from models.user_model import User

main = Blueprint('main', __name__)

# @main.route('/register')
# def register():
#     try:
#         email='test@example.com'
#         first_name='John'
#         last_name='Doe'
#         password='password'
#         role='doctor'

#         user = User(email=email, first_name=first_name, last_name=last_name, password=password, role=role)
#         storage.new(user)
#         storage.save()
#     except Exception as e:
#         print(f"Error: {str(e)}")

#     finally:
#         storage.close()
#     return render_template('index.html', url_for=url_for)

@main.route('/register', methods=['POST'])
def register():
    try:
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        email = request.form.get('email')
        role = request.form.get('role')
        password = request.form.get('password')

        # Create a new User object
        new_user = User(first_name=first_name, last_name=last_name, email=email, role=role, password=password)

        # Add the new_user to the database
        storage.new(new_user)
        storage.save()
    except Exception as e:
        print(f"Error: {str(e)}")

    return redirect('/product_page')

# @main.route('/success')
# def redirect_main():
#     return render_template('product_page.html')
