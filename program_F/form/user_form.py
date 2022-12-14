from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, BooleanField
from wtforms import EmailField
from wtforms.validators import DataRequired
import wtforms.validators


class RegisterForm(FlaskForm):
    name = EmailField('name', validators=[wtforms.validators.DataRequired()])
    fname = EmailField('family', validators=[wtforms.validators.DataRequired()])
    log = EmailField('Email', validators=[wtforms.validators.DataRequired()])
    password = PasswordField('Password', validators=[wtforms.validators.DataRequired()])
    submit = SubmitField('submit')


class LoginForm(FlaskForm):
    log = StringField('Login', validators=[wtforms.validators.DataRequired()])
    password = PasswordField('Password', validators=[wtforms.validators.DataRequired()])

    submit = SubmitField('Sign in')