from flask import Flask, request, jsonify
from logic import User, Admin
from database import DictDatabase


""" Flask app"""
app = Flask(__name__)

# Initialize services
user_service = User()
admin_service = Admin()
database = DictDatabase()

# set database for user and admin
user_service.database = database
admin_service.database = database 

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    user_service.email = email
    user_service.password = password
    
    if user_service.login():
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid credentials'})

# Route for resetting user password
@app.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data['email']
    current_password = data['current_password']
    new_password = data['new_password']
    
    if user_service.reset_password(email,current_password, new_password):
        return jsonify({'message': 'Password reset successful'})
    else:
        return jsonify({'message': 'Failed to reset password'})

# Route for admin login
@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    admin_service.email = email
    admin_service.password = password
    
    if admin_service.login():
        return jsonify({'message': 'Admin login successful'})
    else:
        return jsonify({'message': 'Invalid admin credentials'})
    
# Route for admin reset password
@app.route('/admin/reset_password', methods=['POST'])
def admin_reset_password():
    data = request.get_json()
    email = data['email']
    current_password = data['current_password']
    new_password = data['new_password']
    
    if admin_service.reset_password(email,current_password, new_password):
        return jsonify({'message': 'Password reset successful'})
    else:
        return jsonify({'message': 'Failed to reset password'})



# start flask app
if __name__ == '__main__':
    app.run(debug=True)
