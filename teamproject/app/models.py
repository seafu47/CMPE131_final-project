from flask_login import UserMixin

from app import db, login


@login.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


# Add usermixin can check/verify user login
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
