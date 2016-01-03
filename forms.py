from wtforms import Form, validators, StringField, PasswordField


class SignupForm(Form):
    username = StringField('Username', [validators.required(), validators.Length(min=3, max=30)])
    password = PasswordField('Password', [validators.required(), validators.Length(min=6, max=30)])
    email = StringField('Email', [validators.required(), validators.Length(min=6, max=35), validators.Email()])
