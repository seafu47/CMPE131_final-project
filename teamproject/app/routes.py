from flask import render_template, flash, url_for, redirect, request, session
from flask_login import login_user, login_required, current_user, logout_user
import os
from werkzeug.utils import secure_filename

from app import app, bcrypt, db
from app.forms import RegisterForm, LoginForm, UploadPhotoForm, AddProduct
from app.models import User, Products

from app.forms import DeleteUserForm

# AllOWED_EXTENSIONS = (['png', 'jpg'])
AllOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in AllOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    par = {
        'section1',
        'section2',
        'section3'
    }
    if request.method == "POST":
        if request.form.get('action1') == 'Upload':
            pass

    return render_template('index.html',
                           title='Home',
                           par=par)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = DeleteUserForm()

    if form.validate_on_submit():
        # TODO: Delete account here
        User.query.filter_by(id=current_user.get_id()).delete()
        db.session.commit()
        session.pop('_flashes', None)
        flash("Account deleted.", category='info')
        return redirect(url_for('index'))

    return render_template('profile.html',
                           title='Profile', form=form)


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
        session.pop('_flashes', None)
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
            session.pop('_flashes', None)
            flash('Log in successful', category='info')
            return redirect(url_for('index'))
        session.pop('_flashes', None)
        flash('Password does not match username!', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    session.pop('_flashes', None)
    flash('You were successfully logged out', category='info')
    return redirect(url_for('login'))


@app.route('/upload', methods=['GET', 'POST'])
def upload_form():
    form = AddProduct()
    if form.validate_on_submit():
        print("Form Submitted")
        product_name = form.product_name.data
        product_price = form.product_price.data
        product_infor = form.product_info.data
        p1 = Products(product_name=product_name, product_price=product_price, product_info=product_infor)
        current_user.product.append(p1)
        db.session.commit()
        # get photo data
        f = form.image_1.data
        filename = secure_filename(f.filename)
        flash('Add Product success', category='success')
        if f.filename == '':
            flash('No image selected')
            # back to previous page
            return render_template('upload.html', form=form)

        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.getcwd() + "/app/static/uploads/" + filename)
        return redirect(url_for('index'))
    pro_item = Products.query.all()
    return render_template('upload.html', form=form, pro_item=pro_item)


"""
@app.route('/upload', methods=['POST'])
@login_required
def upload_image():
    if 'file' not in request.files:
        flash("No file found")
        return redirect(request.url)
    file = request.files['file']

    if file.filename == '':
        flash("No imagine was selected")
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash("Image successfully uploaded")
        return render_template('upload.html', filename=filename)
    else:
        flash("Allowed image types are .png file")
        return redirect(request.url)
"""


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename))
