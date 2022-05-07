from app import app


if __name__ == "__main__":
    app.run(debug=True)

# Use following to create a new database:
# from app.models import Products, db, User
# db.create_all()