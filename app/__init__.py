from flask import Flask, render_template
from app.routes import word_cloud

def create_app():
    # Construct the core application.
    app = Flask(__name__)
    app.config.from_object('app.config')
    with app.app_context():
        # Import parts of our application
        app.register_blueprint(word_cloud.word_cloud_bp)
        return app