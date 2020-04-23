"""App entry point."""
from flask import send_from_directory, render_template
from app import create_app

app = create_app()

if __name__ == "__main__":
    #register landing page
    @app.route('/')
    def home():
        return render_template('index.html', title='Yelp-DV')
    app.run(port=app.config['PORT'])