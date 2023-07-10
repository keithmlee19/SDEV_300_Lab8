'''Defines login and registration form objects'''
from flask_wtf import FlaskForm
from wtforms import TextAreaField, PasswordField, SubmitField, validators

def IsNotCommonPW(form, field):
    '''Checks if password is in list of common passwords'''
    common_pw_set = set(line.strip() for line in open("CommonPassword.txt"))
    if field.data in common_pw_set:
        raise validators.ValidationError("Password too common, please try again.")

class LoginForm(FlaskForm):
    '''Login form class'''
    # no validators other than data required
    # because length/complexity validation happens while registering
    username = TextAreaField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
    submit = SubmitField("Sign In")

class RegistrationForm(FlaskForm):
    '''Registration form class'''
    username = TextAreaField("Username", [
        validators.DataRequired(),
        validators.regexp(
            "^[a-zA-Z0-9]{8,}$",
            message="Username must be at least 8 characters "
            "and contain only digits and uppercase/lowercase letters"
        )])
    password = PasswordField("Enter Password", [
        validators.DataRequired(),
        validators.regexp(
            "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{12,}$",
            message="Password must be at least 12 characters "
            "and contain at least 1 lowercase letter, 1 uppercase letter, 1 digit,"
            "and 1 special character"
        ),
        # passwords must match
        validators.EqualTo("password2", message="Passwords must match")
    ])
    # confirm password before registration
    password2 = PasswordField("Confirm Password", [validators.DataRequired()])
    submit = SubmitField("Register")

class PasswordUpdateForm(FlaskForm):
    '''Password update form class'''
    password = PasswordField("Enter Password", [
        validators.DataRequired(),
        validators.regexp(
            "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{12,}$",
            message="Password must be at least 12 characters "
            "and contain at least 1 lowercase letter, 1 uppercase letter, 1 digit,"
            " and 1 special character"),
        IsNotCommonPW,
        # passwords must match
        validators.EqualTo("password2", message="Passwords must match")
    ])
    password2 = PasswordField("Confirm New Password", [validators.DataRequired()])
    submit = SubmitField("Request Password Reset")
