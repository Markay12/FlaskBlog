# forms for html in separate file for tracking

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo #to check validation of input
#equalTo validator to check password and confirm password

#create individual classes for different kinds of forms, the first being to register
class RegistrationForm(FlaskForm):
    #form fields (what information do we want to store)
    #create some restrictions for usernames with use of validators
    username = StringField('Username --> ', validators=[DataRequired(min=2, max=20)]) #ask for some username
    #min length = 2 and max = 20
    email = StringField('Email --> ', validators=[DataRequired(), Email()])

    password = PasswordField('Password --> ', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password --> ', validators=[DataRequired(), EqualTo()])

    submit = SubmitField('Sign Up!')


class LoginForm(FlaskForm):
    email = StringField('Email --> ', validators=[DataRequired(), Email()])
    password = PasswordField('Password --> ', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign Up!')
    