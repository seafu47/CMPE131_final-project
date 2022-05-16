from app import app

if __name__ == "__main__":
    app.run(debug=True, host ="0.0.0.0", port=4999)

# Use following to create a new database:
# from app.models import Products, db, User
# db.create_all()
