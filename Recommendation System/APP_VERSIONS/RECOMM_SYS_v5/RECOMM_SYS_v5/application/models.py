from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class movies(db.Document):
    Movie_Id        =   db.IntField(unique = True)
    Year            =   db.IntField()
    Name            =   db.StringField(max_length = 255)
    Link            =   db.StringField(max_length = 255)

class users(db.Document):
    Cust_Id     =   db.IntField(unique = True)
    First_Name  =   db.StringField(max_length = 200)
    Last_Name   =   db.StringField(max_length = 200)
    Email       =   db.StringField(max_length = 100, unique=True)
    Password    =   db.StringField( )

    def print_password(self, Password):
        print(generate_password_hash(Password))
    
    def get_password(self, Password):
        return check_password_hash(self.Password, Password)