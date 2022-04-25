from flask import render_template, flash, url_for, redirect, request
from flask_login import login_user, login_required, current_user, logout_user

from app import app, bcrypt, db
from app.forms import RegisterForm, LoginForm
from app.models import User


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    par = {
        'section1',
        'section2',
        'section3'
    }

    return render_template('index.html',
                           title='Home',
                           par=par)


@app.route('/register', methods=['GET', 'POST'])
def register():
    # if the user already login return to main html
    # no need register
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        user1 = User(username=username, email=email, password=password)
        db.session.add(user1)
        db.session.commit()
        flash('Congrats, register success', category='success')
        return redirect(url_for('index'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if the user already log in return to main html
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        user1 = User.query.filter_by(username=username).first()
        if user1 and bcrypt.check_password_hash(user1.password, password):
            login_user(user1, remember=remember)
            if request.args.get('next'):
                next_page = request.args.get('next')
                return redirect(next_page)
            flash('Log in successful', category='info')
            return redirect(url_for('index'))
        flash('Password not match', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
