from flask import Blueprint

# creating a blueprint object named greetings_bp
greetings_bp = Blueprint('greetings', __name__)

# for routes, just add the blueprint object-name before the route
@greetings_bp.route('/hello')
def hello():
    return 'Hello, world!'

@greetings_bp.route('/goodbye')
def goodbye():
    return 'Goodbye, world!'