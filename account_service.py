""" Main program """
from flask import Flask, request, jsonify
from logic import User, Admin, Membership
from database import DictDatabase

""" Flask app"""
app = Flask(__name__)

# Initialize services
user_service = User()
admin_service = Admin()
member = Membership()

user_database = DictDatabase()
admin_database = DictDatabase()

# set database for user and admin
user_service.database = user_database
admin_service.database = admin_database
member.user_database = user_database

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    user_service.email = email
    user_service.password = password

    user = user_service.login()
    if user:
        # Authorized  user
        response = jsonify(user)
        response.status_code = 200
    else:
        # Unauthorized user
        response = jsonify({'message': 'Invalid admin credentials'})
        response.status_code = 401
    return response

# Route for resetting user password
@app.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data['email']
    current_password = data['current_password']
    new_password = data['new_password']
    
    if user_service.reset_password(email,current_password, new_password):
        response = jsonify({'message': 'Password reset successful'})
        response.status_code = 200
    else:
        response = jsonify({'message': 'Failed to reset password'})
        response.status_code = 500
    return response

# Route for admin login
@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    admin_service.email = email
    admin_service.password = password
    
    admin = admin_service.login()
    if admin:
        # Authorized  user
        response = jsonify(admin)
        response.status_code = 200
    else:
        # Unauthorized user
        response = jsonify({'message': 'Invalid admin credentials'})
        response.status_code = 401
    return response

# Route for admin reset password
@app.route('/admin/reset_password', methods=['POST'])
def admin_reset_password():
    data = request.get_json()
    email = data['email']
    current_password = data['current_password']
    new_password = data['new_password']
    
    if admin_service.reset_password(email,current_password, new_password):
        response = jsonify({'message': 'Password reset successful'})
        response.status_code = 200
    else:
        response = jsonify({'message': 'Failed to reset password'})
        response.status_code = 500
    return response


# Route for create membership
@app.route('/register-membership', methods=['POST'])
def create_membership():
    data = request.get_json()
    email = data['email']
    
    membership_data = member.create_membership(email)
    if membership_data:
        response = jsonify({'user_email': membership_data[0],
                            'membership_invoice' : membership_data[1]})
        response.status_code = 200
    else:
        response = jsonify({'message': 'Email not found'})
        response.status_code = 404
    return response

# start flask app
if __name__ == '__main__':
    app.run(debug=True)
