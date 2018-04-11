from flask import Blueprint

home_app = Blueprint('user_app', __name__)

@home_app.route('/')
def login():
    return "Welcome you to your Flask App Using Blueprint!"