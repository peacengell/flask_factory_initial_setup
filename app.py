from flask import Flask

def create_app():
    app =Flask(__name__)
    app.config.from_pyfile('settings.py')

    from home.views import home_app
    app.register_blueprint(home_app)

    return app # return the whole flask app.

