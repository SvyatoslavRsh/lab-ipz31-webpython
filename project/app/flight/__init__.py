from flask import Blueprint

flight_blueprint = Blueprint('flight', __name__, template_folder="templates/flight")

from . import views