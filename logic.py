""" Logic for account service execution """
import random
import string


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
    
    def login(self)-> bool:
        if self.email in self._database.get_user_credentials() and self._database.get_user_credentials() \
                [self.email]['password'] == self.password:
            return {
                'username' : self._email,
                'role' : self._database.get_user_credentials()[self._email]['role']
            } 
        else:
            return False
    
    def reset_password(self, email, current_password, new_password)-> bool:
        if email in self._database.get_user_credentials() and self._database.get_user_credentials()\
            [email]['password'] == current_password:
            self._database.get_user_credentials()[email]['password'] = new_password
            return True
        else: 
            return False
        

class Admin(Account):

    def __init__(self):
        super().__init__()
        self._admin_number = None 

    def login(self):
        if self.email in self._database.get_admin_credentials() and self._database.get_admin_credentials() \
          [self.email]['password'] == self.password:
            self._admin_number = self._database.admin_credentials[self.email]['admin_number']
            return {
                'username' : self._email,
                'role' : self._database.get_admin_credentials()[self._email]['role']
            }
        else:
            return False
        
    def reset_password(self, email, current_password, new_password):
        if email in self._database.get_admin_credentials() and self._database.get_admin_credentials()\
            [email]['password'] == current_password:
            self._database.get_admin_credentials()[email]['password'] = new_password
            print(self._database.get_admin_credentials())
            return True    
        else: 
            return False



class Membership:
    """ Create membership"""
    NORMAL_MEMBERSHIP_EXPIRY = 30 #in days
    USER_NUMBER = 1

    def __init__(self) -> None:
        self._user_database = None 
        self._number = None
        self._expiry_date = None 
        self._user_email = None 
        self._payment_status = None 

    @property
    def user_database(self):
        return self._user_database
    
    @user_database.setter
    def user_database(self, user_database):
        self._user_database = user_database


    def create_membership(self, user_email):
        """ set membership """
        if(self._helper_check_email_not_valid(user_email)):
            return "email not found"
        generate_mb_invoice = self.generate_booking_number()
        self._user_database.get_user_credentials()[user_email]['number'] = self.USER_NUMBER
        #update user number by 1
        self.USER_NUMBER += 1
        user_invoice = self._user_database.get_user_credentials()[user_email]['invoice'] = generate_mb_invoice
        self._user_database.get_user_credentials()[user_email]['expiry_date'] = self.NORMAL_MEMBERSHIP_EXPIRY
        return user_email, user_invoice

    def check_status_payment(self, user_email):
        if(self._helper_check_email_not_valid(user_email)):
            return "email not found"
        return self._user_database.get_user_credentials()[user_email]['payment_status']

    def update_status_membership(self, user_email, status):
        if(self._helper_check_email_not_valid(user_email)):
            return "email not found"
        self._user_database.get_user_credentials()[user_email]['payment_status'] = status

    def generate_booking_number(self):
        """ Generates token for purchasing membership"""
        prefix = "MB"
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        booking_number = prefix + random_part
        return booking_number

    def _helper_check_email_not_valid(self, user_email):
        """ Checking email validatition"""
        if user_email not in self._user_database.get_user_credentials().keys():
            return True


# test
from database import *

member = Membership()

member.user_database = DictDatabase()

payment_data = member.create_membership('sisan@gmail.com')
print(payment_data)

status = member.check_status_payment('siandsf@gmail.com')
print(status)

member.update_status_membership(status="Nunggak",user_email='sian@gmail.com')

status = member.check_status_payment('sian@gmail.com')
print(status)