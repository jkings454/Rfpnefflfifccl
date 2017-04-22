import os
from flask import Flask, request
from models import DataPoint, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

app = Flask(__name__)

app.config.from_object(("config.%s" % os.getenv("APP_ENV",
                                     "Development"))) # If there's an "APP_ENV"
                                                     # Environment variable set, we'll use that
                                                     # environment, otherwise, we'll use Development

# Create an SQLAlchemy Session.

engine = create_engine(app.config["DATABASE_URI"])
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()


# Views

@app.route("/")
def index():
    return "Hello world!"

# API routes

@app.route("/api/v1/data", methods=["GET", "POST"])
def get_post_data():
    if request.method == "GET":
        # We're sending all of our data to the user!
        return "GET request received!"

    elif request.method == "POST":
        # There's a new data point in town!
        return "POST request received!"

    else:
        # The only two requests that we support are "GET" and "POST"
        return "Unsupported HTTP request", 400

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])