from flask import Flask, request

app = Flask(__name__)

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
    app.run()