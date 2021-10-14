from book import db,login_manager



class Book(db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    author = db.Column(db.Text)
    price = db.Column(db.Integer)

    def __init__(self,name,author,price):
        self.name = name
        self.author = author
        self.price = price

    def __repr__(self):
        return (f"Name:{self.name}; Author:{self.author}; Price:{self.price}")

@login_manager.user_loader
def load_user(user_id):
    return Book.query.get(user_id)

"""class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique = True, index= True)
    username = db.Column(db.String(64), unique = True, index = True)
    password_hash = db.Column(db.String(128))


    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)"""

