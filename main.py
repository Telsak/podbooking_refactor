from flask import Flask
from greetings import greetings_bp # imports the blueprint from the greetings.py file

def create_app():
    app = Flask(__name__)

    # pulls the imported blueprint into the flask app itself
    app.register_blueprint(greetings_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
