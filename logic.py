""" Logic for account service execution """
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


