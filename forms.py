from flask_wtf import FlaskForm
from wtforms import form, StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, length


class Registration(FlaskForm):
    first_name = StringField(
        "First Name", [InputRequired("Please enter your first name")])
    last_name = StringField(
        "Last Name", [InputRequired("Please enter your last name")])
    email = StringField("Email", [InputRequired(
        "Please enter your email"), Email("Enter valid email")])
    password = PasswordField("Password", validators=[length(min=8, max=16)])
    re_password = PasswordField(
        "Re-enter Password", validators=[length(min=8, max=16)])
    submit = SubmitField("Submit")


class Login(FlaskForm):
    email = StringField(
        "Enter email", [InputRequired("Enter your email"), Email()])
    password = PasswordField("Enter you password", [
                             InputRequired("Please enter your password")])
    submit = SubmitField("Login")
