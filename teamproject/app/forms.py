from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField, Form, validators, IntegerField, \
    TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from app.models import User


class RegisterForm(FlaskForm):
    """
    Register form for user registration, with username, email, password and the submit button.
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    # recaptcha = RecaptchaField()
    submit = SubmitField('Register')

    # check username if the same
    def validate_username(self, username):
        """
        Validates if a username is valid
        :param username: name to be validated
        :return: None
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken')

    # check email if the same(already taken)
    def validate_email(self, email):
        """
        Validates if an email is valid
        :param email: Email to be validated
        :return: None
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already register')


class LoginForm(FlaskForm):
    """
    Form for login, with username, password, remember and submit fields.
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign In')


class DeleteUserForm(FlaskForm):
    """
    Form to delete user.
    """
    delete = SubmitField('Delete Account')


class AddProduct(FlaskForm):
    """
    Form to upload products with name, price, info, image and submit button.
    """
    # product_name = StringField('Product Name', [validators.DataRequired()])
    # product_id = IntegerField('Product Id', validators=[DataRequired(), Length(min=6, max=20)])
    # product_price = IntegerField('Product Price', validators=[DataRequired(), Length(min=6, max=20)])
    # information = TextAreaField('Description', [validators.DataRequired()])

    product_name = StringField('Product Name', [validators.DataRequired()])
    # product_id = IntegerField('Product Id')
    product_price = IntegerField('Product Price')
    product_info = TextAreaField('Description')
    image_1 = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'images only please')])

    submit = SubmitField('Submit')


class UploadPhotoForm(FlaskForm):
    """
    Form to upload photos
    """
    photo = FileField(validators=[FileRequired()])
    submit = SubmitField('Upload')
