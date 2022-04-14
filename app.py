
import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect

from _app import routes

SECRET_KEY = os.urandom(32)

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.register_blueprint(routes.backend)
    app.register_blueprint(routes.home)

    csrf.init_app(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)

