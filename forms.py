from wtforms import Form, validators, StringField, PasswordField, SubmitField
from models import db, User
import logging


class SignupForm(Form):
    username = StringField('Username', [validators.required(), validators.Length(min=3, max=30)])
    password = PasswordField('Password', [validators.required(), validators.Length(min=6, max=30)])
    email = StringField('Email', [validators.required(), validators.Length(min=6, max=35), validators.Email()])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        username = User.query.filter_by(username=self.username.data.lower()).first()
        email = User.query.filter_by(email=self.email.data.lower()).first()
        if username:
            self.username.errors.append("That username is already taken")
            return False
        elif email:
            self.email.errors.append("That email is already taken")
            return False
        else:
            return True
