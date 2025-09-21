
from flask import Blueprint

app = Blueprint("general", __name__)

@app.route("/")
def home():
    return "Hello from general blueprint!"


@app.route("/about")
def about():
    return "this is about home!"

