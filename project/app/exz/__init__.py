from flask import Blueprint

api_flight = Blueprint('api_flight', __name__)

from . import views