from flask import render_template, flash, url_for, redirect, request, session
from flask_login import login_user, login_required, current_user, logout_user
import os
import string
import random
from werkzeug.utils import secure_filename

from app import app, bcrypt, db
from app.forms import RegisterForm, LoginForm, UploadPhotoForm, AddProduct
from app.models import User, Products, Carts

from app.forms import DeleteUserForm

# AllOWED_EXTENSIONS = (['png', 'jpg'])
AllOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    """
    Create a valid file name
    :param filename: file name to check
    :return: valid file name
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in AllOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    """
    Renders the home page. This page checks and takes input from the search bar.
    :return: Home page
    """
    if request.method == 'POST':
        title = request.form['search']

        if not title:
            flash('Search field is required!')
        else:
            pro_items = Products.query.filter(Products.product_name.like('%' + title + '%'))
            return render_template('index.html',
                                   title='Home',
                                   pro_items=pro_items)

    # form = AddProduct()
    pro_items = Products.query.all()

    """
    if request.method == "POST":
        if request.form.get('action1') == 'Upload':
            pass
    """
    return render_template('index.html',
                           title='Home',
                           pro_items=pro_items)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """
    Shows the profile page with the users credentials, and also shows the user's items.
    There are is also a "delete account" and a "delete listing" button.
    :return: Profile page
    """
    user_id = current_user.get_id()

    products = Products.query.filter_by(product_seller_user_id=user_id).all()

    form = DeleteUserForm()

    if form.validate_on_submit():
        # TODO: Delete account here
        # Delete all the items first
        for i in products:
            db.session.delete(i)

        User.query.filter_by(id=user_id).delete()
        db.session.commit()
        session.pop('_flashes', None)
        flash("Account deleted.", category='info')
        return redirect(url_for('index'))

    return render_template('profile.html',
                           title='Profile', form=form, pro_items=products)


@app.route('/deleteitem', methods=['POST', 'GET'])
@login_required
def delete_item():
    """
    Used to delete items
    :return: Delete item page
    """

    user_id = current_user.get_id()

    products = Products.query.filter_by().all()
    print([request.form['item_delete']][0])

    for i in products:
        if int([request.form['item_delete']][0]) == i.product_id:
            db.session.delete(i)
            break

        #db.session.delete(i)
    db.session.commit()


    return redirect(url_for('profile'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Register page, where the user can enter email, username and password to register
    :return: Register page
    """
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
    """
    Login page, where username and password are required to log in
    :return: Login page
    """
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
    """
    Logs out the user
    :return: Logout page
    """
    logout_user()
    session.pop('_flashes', None)
    flash('You were successfully logged out', category='info')
    return redirect(url_for('login'))


@app.route('/upload', methods=['GET', 'POST'])
def upload_form():
    """
    Upload a new listing.
    Name, price, description and a photo are required to create a listing.
    :return: Upload page
    """
    form = AddProduct()
    if form.validate_on_submit():
        product_name = form.product_name.data
        product_price = form.product_price.data
        product_infor = form.product_info.data
        image_name = ''.join(random.choice(string.ascii_letters) for i in range(16))
        p1 = Products(product_name=product_name, product_price=product_price, product_info=product_infor,
                      product_image=image_name)
        current_user.product.append(p1)
        db.session.commit()
        # get photo data
        f = form.image_1.data
        filename = secure_filename(f.filename)
        if f.filename == '':
            flash('No image selected')
            # back to previous page
            return render_template('upload.html', form=form)

        if f and allowed_file(image_name + '.png'):
            filename = secure_filename(image_name + '.png')
            f.save(os.getcwd() + "/app/static/uploads/" + filename)
        flash('Add Product success', category='success')
        return redirect(url_for('index'))
    # pro_item = Products.query.all()
    return render_template('upload.html', form=form)


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


@app.route('/shoppingcart', methods=['GET', 'POST'])
def shoppingcart():
    """
    Shopping cart page
    :return: Shopping cart html page
    """
    pro_items = Products.query.all()
    return render_template('shoppingcart.html',
                           pro_items=pro_items)



@app.route('/sorting', methods=['GET', 'POST'])
@login_required
def sorting():
    """
    Renders the home page with the list of items sorted by name
    :return:
    """

    if request.method == 'POST':
        title = request.form['search']

        if not title:
            flash('Search field is required!')
        else:
            pro_items = Products.query.filter(Products.product_name.like('%' + title + '%'))
            return render_template('sorting.html',
                                   title='Home',
                                   pro_items=pro_items)
    pro_items = Products.query.all()

    return render_template('sorting.html', pro_items=pro_items)


@app.route('/display/<filename>')
def display_image(filename):
    """
    Used to display images
    :param filename: Name of the file
    :return: Display image
    """
    return redirect(url_for('static', filename='uploads/' + filename))
