from flask import Flask, render_template
from app.routes import word_cloud, sentiment_analysis, checkin_heatmap, map, recommender


def create_app():
    app = Flask(__name__)
    with app.app_context():
        # Moving landing page route for gunicorn
        @app.route('/')
        def home():
            return render_template('index.html', title='Yelp-DV')

        # Import parts of our application
        app.register_blueprint(word_cloud.word_cloud_bp)
        app.register_blueprint(map.map_bp)
        app.register_blueprint(sentiment_analysis.sentiment_analysis_bp)
        app.register_blueprint(checkin_heatmap.checkin_heatmap_bp)
        app.register_blueprint(recommender.recommender_bp)
        return app
