
from flask import Blueprint

app = Blueprint("general", __name__)

@app.route("/")
def home():
    return "Hello from general blueprint!"

