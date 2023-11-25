from flask import Flask, request, jsonify
from abc import abstractmethod, ABC

class Account:

    def __init__(self) -> None:
        self._email = None 
        self._password = None
        self._database = None
    
    @property
    def database(self):
        return self._database
    
    @database.setter
    def database(self, selection_database):
        self._database = selection_database
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, user_email):
        self._email = user_email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, user_password):
        self._password = user_password
      
    def login(self):
        pass

    def reset_password(self):
        pass


class User(Account):

    def __init__(self)-> None:
        super().__init__()
        self._membership_status = None
    
    def login(self):
        return {self.email : self._database.get_user_credentials() [self.email]} if self.email \
            in self._database.get_user_credentials() and self._database.get_user_credentials() \
                [self.email]['password'] == self.password else False
    
    def reset_password(self, email, new_password):
        if email in self._database.get_user_credentials():
            self._database.get_user_credentials()[email]['password']\
            = new_password
            print(self._database.get_user_credentials())
            return True
            
        else: 
            return False

    def register_membership(self):
        print("bayar")

    def is_member(self) -> bool:
        return True if self._database.get_user_credentials()[self.email]['membership_status']\
           != None else  False


class Admin(Account):

    def __init__(self):
        super().__init__()
        self._admin_number = None 

    def login(self):
        if self.email in self._database.get_admin_credentials() and self._database.get_admin_credentials() \
          [self.email]['password'] == self.password:
            self._admin_number = self._database.admin_credentials[self.email]['admin_number']
            return {self.email : self._database.get_admin_credentials()[self.email]}
        else:
            return False
        
    def reset_password(self, email, new_password):
        if email in self._database.get_admin_credentials():
            self._database.get_admin_credentials()[email]['password']\
            = new_password
            print(self._database.get_admin_credentials())
            return True    
        else: 
            return False


class Database(ABC):

    @abstractmethod
    def get_user_credentials(self):
        pass

    @abstractmethod
    def get_admin_credentials(self):
        pass


class DictDatabase(Database):
    """ Implementation using simpledict data type objects in python 3"""
    user_credentials = {
        'sian@gmail.com' : {
            'password' : 'akuganteng',
            'role' : 'user',
            'membership_status' : True,
            'number' : '001',
            'expiry_date' : None,
            'payment_status' : False
        },
        'nisa@gmail.com' : {
            'password' : 'qwery123',
            'role' : 'user',
            'membership_status' : None,
            'number' : '002',
            'expiry_date' : None,
            'payment_status' : 'belum'
        },
        'dicky@yahoo.com' : {
            'password' : 'husqivarna',
            'role' : 'user',
            'membership_status' : None ,
            'number' : '003',
            'expiry_date' : None,
            'payment_status' : False
        }
    }

    admin_credentials = {
        'evita@studio21.com' : {
            'password' : 'lexus231',
            'role' : 'admin',
            'admin_number' : '001',
        },
    }

    def get_user_credentials(self):
        return self.user_credentials
    
    def get_admin_credentials(self):
        return self.admin_credentials
    

app = Flask(__name__)
db = DictDatabase()  # Instantiate the database

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
    new_password = data['new_password']
    
    if user_service.reset_password(email, new_password):
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

if __name__ == '__main__':
    app.run(debug=True)
