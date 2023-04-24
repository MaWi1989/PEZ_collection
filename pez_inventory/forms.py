from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, TextAreaField, IntegerField, BooleanField, Form, FormField
from wtforms.validators import DataRequired, Email

# class Adress_Form(Form):
#     street = StringField('Street', validators= [DataRequired()])
#     city_state = StringField('City, State', validators= [DataRequired()])
#     zip_code = IntegerField('Zip Code', validators= [DataRequired()])


class UserSignupForm(FlaskForm):
    first_name = StringField('First Name', validators= [DataRequired()])
    last_name = StringField('Last Name', validators= [DataRequired()])
    username = StringField('Username', validators= [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # address = FormField(Adress_Form)
    # phone_number = StringField('Phone Number', validators= [DataRequired()])
    submit_button = SubmitField()



class UserLoginForm(FlaskForm):
    username = StringField('Username', validators= [DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()



class PEZForm(FlaskForm):
    name = StringField('Name')
    series = StringField('Series')
    description = StringField('Description')
    price = DecimalField('Price', places = 2)
    value = DecimalField('Value', places = 2)
    year_introduced = IntegerField('Year Introduced')
    retired = BooleanField('Retired?')
    original_package = BooleanField('Original Package?')
    random_fact = StringField('Random Fact' )
    submit_button = SubmitField()