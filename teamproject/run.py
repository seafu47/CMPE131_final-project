from app import app

# Start the app with the host 0.0.0.0 and port 4999
if __name__ == "__main__":
    app.run(debug=True, host ="0.0.0.0", port=4999)

# Use following to create a new database:
# from app.models import Products, db, User
# db.create_all()
