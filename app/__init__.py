from flask import Flask

# grab the config class from the config.py file
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # initialize flask extensions here


    # register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

    @app.route('/test')
    def test_page():
        return '<h1>Testing the flask application factory pattern</h1>'
    
    return app