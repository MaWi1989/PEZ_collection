from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash
import secrets
from flask_login import UserMixin, LoginManager

from flask_marshmallow import Marshmallow


db = SQLAlchemy()


login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = False)
    last_name = db.Column(db.String(150), nullable = False)
    username = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), nullable = False)         
    password = db.Column(db.String(150), nullable = False)
    # address = db.Column(db.String(500), nullable = True)
    # phone_number = db.Column(db.String(20), nullable = False) 
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    PEZ = db.relationship('PEZ', backref = 'owner', lazy = True)
    # address = db.relationship('Address_Form()') 

    def __init__(self, first_name, last_name, username, email, password):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(16)  


    def set_token(self, length):
        return secrets.token_hex(length)
        

    def set_id(self):
        return str(uuid.uuid4())
    
    
    def set_password(self, password):
        return generate_password_hash(password)
         
    
    
    def __repr__(self):
        return f"User {self.username} has been added to the database!"



class PEZ(db.Model):
    __tablename__ = 'pez'
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150))
    series = db.Column(db.String(150))
    description = db.Column(db.String(200), nullable = True)
    price = db.Column(db.Numeric(precision=10,scale=2))
    value = db.Column(db.Numeric(precision=10,scale=2))
    year_introduced = db.Column(db.Integer)
    retired = db.Column(db.Boolean)
    original_package = db.Column(db.Boolean)
    random_fact = db.Column(db.String(200))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)


    def __init__(self, name, series, description, price, value, year_introduced, retired, original_package, random_fact, user_token, id = ''):
        self.id = self.set_id()
        self.name = name
        self.series = series
        self.description = description
        self.price = price
        self.value = value
        self.year_introduced = year_introduced
        self.retired = retired
        self.original_package = original_package
        self.random_fact = random_fact
        self.user_token = user_token


    def set_id(self):
        return str(uuid.uuid4())
    
    def __repr__(self):
        return f'The following PEZ has been added: {self.name}'



class PEZSchema(ma.Schema):
    class Meta:
        fields = ['ID', 'Name', 'Series', 'Description', 'Price', 'Value', 'Year Introduced', 'Retired?', 'Original Package?' ]


pez_schema = PEZSchema()
all_pez_schema = PEZSchema(many = True)