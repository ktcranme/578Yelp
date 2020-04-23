from flask import Flask
from app.routes import word_cloud
import requests


def is_prod():
    r = requests.get('http://metadata.google.internal')
    if r.headers.get('Metadata-Flavor', None) == 'Google':
        return True
    return False


def create_app():

    # Construct the core application.
    app = Flask(__name__)
    if is_prod():
        app.config.from_object('app.config.Prod')
    else:
        app.config.from_object('app.config.Local')

    with app.app_context():
        # Import parts of our application
        app.register_blueprint(word_cloud.word_cloud_bp)
        return app
