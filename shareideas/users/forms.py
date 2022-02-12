from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from shareideas.models import User


class RegistrationForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired()])
    age = StringField('Age',
                      validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken! Please choose a different username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is taken! Please choose a different email')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class UpdateAccountForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired()])
    age = StringField('Age',
                      validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=20)])
    picture = FileField('Upload Profile Picture',
                        validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Update Profile')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username already exist! Please choose a different one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email already exist! Please choose a different one')


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email!')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
