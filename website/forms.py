from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import InputRequired, Length, Email

class RegisterForm(FlaskForm):
    username = StringField(label="Enter Username", validators=[Length(min=2, max=30), InputRequired()])
    email = EmailField(label="Email Address", validators=[Email(), InputRequired()])
    sample_file = FileField(label='Upload File')
    submit = SubmitField(label='Register')