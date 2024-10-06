from application import db

class movies(db.Document):
    Movie_Id        =   db.IntField(unique = True)
    Year            =   db.IntField()
    Name            =   db.StringField(max_length = 255)
    Link            =   db.StringField(max_length = 255)