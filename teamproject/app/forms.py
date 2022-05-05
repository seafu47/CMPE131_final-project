from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField, Form, validators, IntegerField, TextAreaField
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


class DeleteUserForm(FlaskForm):
    delete = SubmitField('Delete Account')

class AddProduct(FlaskForm):
    #product_name = StringField('Product Name', [validators.DataRequired()])
    #product_id = IntegerField('Product Id', validators=[DataRequired(), Length(min=6, max=20)])
    #product_price = IntegerField('Product Price', validators=[DataRequired(), Length(min=6, max=20)])
    #information = TextAreaField('Description', [validators.DataRequired()])

    product_name = StringField('Product Name', [validators.DataRequired()])
    #product_id = IntegerField('Product Id')
    product_price = IntegerField('Product Price')
    product_info  = TextAreaField('Description')
    image_1 = FileField('Upload Image', validators=[FileAllowed(['jpg','png','jpeg'], 'images only please')])

    submit = SubmitField('Submit')

class UploadPhotoForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])
    submit = SubmitField('Upload')