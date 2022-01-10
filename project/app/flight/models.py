from .. import db
import enum
from datetime import datetime


class RouteType(enum.Enum):
    Internal = 'Internal'
    International = 'International'


class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.Integer, nullable=False)
    point_departure = db.Column(db.String(50), nullable=False)
    point_destination = db.Column(db.String(50), nullable=False)
    departure_date = db.Column(db.String(35), default=datetime.utcnow)
    departure_time = db.Column(db.String(35), default=datetime.utcnow)
    travel_time = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Enum(RouteType))
    price = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
