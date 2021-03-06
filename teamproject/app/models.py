from flask_login import UserMixin
from app import db, login


@login.user_loader
def load_user(user_id):
    """
    Get uer by user id
    :param user_id: User id
    :return: user item
    """
    return User.query.filter_by(id=user_id).first()


# Add usermixin can check/verify user login
class User(db.Model, UserMixin):
    """
    User class, which contains id, username, password, email and the products.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    product = db.relationship('Products', backref=db.backref('author', lazy=True))
    cart = db.relationship('Carts', backref=db.backref('author', lazy=True))
    # photo_image = db.Column(db.String(120), default='static/uploads/dog_PNG50321.png', nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Products(db.Model):
    """
    Product, which contains the product id, name, price, info, image and the seller's user id.
    """
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # name of the products
    product_name = db.Column(db.String(50), nullable=False)

    # price of the products
    product_price = db.Column(db.Float, nullable=False)

    # information of the products
    product_info = db.Column(db.Text, nullable=False)

    product_image = db.Column(db.String, nullable=False)

    # Eproduct_img = db.Column(db.String(100), nullable=False)
    # product_createtime = db.Column(db.DateTime,default=datetime.now)

    product_seller_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #users = db.relationship('User', backref=db.backref('author', lazy=True))
    #order = db.relationship('Carts', backref=db.backref('productlist', lazy=True))


class Carts(db.Model):
    """
    Data class for the shopping cart, which contains order ids, names, prices and seller's user ids.
    """
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    seller_name = db.Column(db.String(50), nullable=False)
    order_name = db.Column(db.String(50), nullable=False)
    order_price = db.Column(db.Float, nullable=False)

    carts_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

