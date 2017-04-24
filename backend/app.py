import os
from flask import Flask, request, jsonify
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
        data = session.query(DataPoint).all()
        return jsonify([i.serialize for i in data])

    elif request.method == "POST":
        # There's a new data point in town!
        name = request.form.get("name") or "Anonymous"
        Rstar = request.form.get("Rstar", type=float)
        fp = request.form.get("fp", type=float)
        ne = request.form.get("ne", type=float)
        fl = request.form.get("fl", type=float)
        fi = request.form.get("fi", type=float)
        fc = request.form.get("fc", type=float)
        L = request.form.get("L", type=float)

        N = Rstar * fp * ne * fl * fi * fc * L

        new_data = DataPoint(name=name, N=N, Rstar=Rstar, fp=fp, ne=ne, fl=fl, fi=fi, fc=fc, L=L)

        session.add(new_data)
        session.commit()

        return jsonify(new_data.serialize)

    else:
        # The only two requests that we support are "GET" and "POST"
        return "Unsupported HTTP request", 400

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])