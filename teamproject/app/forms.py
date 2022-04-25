from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from app.models import User


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    # recaptcha = RecaptchaField()
    submit = SubmitField('Register')

    # check username if the same
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken')

    # check email if the same(already taken)
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign In')
