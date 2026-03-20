from flask import Blueprint
from ..extensions import db
from ..models.user import User
from ..models.video import Video

api = Blueprint('api', __name__)

@api.route('/api/<name>')
def api_lookup(name):
    user = User.query.filter_by(name='Simon').first()

    return {"user": user.name}
