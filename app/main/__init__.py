# place for the main blueprint
from flask import Blueprint

# __name__ holds name of the current python module
bp = Blueprint('main', __name__)

from app.main import routes