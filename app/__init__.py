from flask import Flask, render_template
from app.routes import word_cloud
from app.routes import map
import requests


def is_prod():
    try:
        r = requests.get('http://metadata.google.internal')
        if r.headers.get('Metadata-Flavor', None) == 'Google':
            print("running prod")
            return True
    except Exception as e:
        print(e)
        print("running local")
        return False


def create_app():
    # Construct the core application.
    app = Flask(__name__)
    if is_prod():
        app.config.from_object('app.config.Prod')
    else:
        app.config.from_object('app.config.Local')

    with app.app_context():
        # Moving landing page route for gunicorn
        @app.route('/')
        def home():
            return render_template('index.html', title='Yelp-DV')

        # Import parts of our application
        app.register_blueprint(word_cloud.word_cloud_bp)
        app.register_blueprint(map.map_bp)
        return app
