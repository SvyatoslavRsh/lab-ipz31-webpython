from flask import Flask, g, request, jsonify
from functools import wraps
from ..flight.models import Flight
from .. import db
from datetime import datetime

from . import api_flight

api_username = 'admin'
api_password = 'password'


def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == api_username and auth.password == api_password:
            return f(*args, **kwargs)
        return jsonify({'message': 'Authentication failed!'}), 403

    return decorated


@api_flight.route('/flights', methods=['GET'])
@protected
def get_flights():
    flights = Flight.query.all()
    return_values = [{"id": flight.id,
                      "flight_number": flight.flight_number,
                      "point_departure": flight.point_departure,
                      "point_destination": flight.point_destination,
                      "departure_date": flight.departure_date,
                      "departure_time": flight.departure_time,
                      "travel_time": flight.travel_time,
                      "price": flight.price,
                      "user_id": flight.user_id} for flight in flights]

    return jsonify({'Flights': return_values})


@api_flight.route('/flight/<int:id>', methods=['GET'])
@protected
def get_flight(id):
    flight = Flight.query.get_or_404(id)
    return jsonify({"id": flight.id,
                    "flight_number": flight.flight_number,
                    "point_departure": flight.point_departure,
                    "point_destination": flight.point_destination,
                    "departure_date": flight.departure_date,
                    "departure_time": flight.departure_time,
                    "travel_time": flight.travel_time,
                    "price": flight.price,
                    "user_id": flight.user_id})


@api_flight.route('/flight', methods=['POST'])
def add_flight():
    flight_new_data = request.get_json()
    flight = Flight.query.filter_by(flight_number=flight_new_data['flight_number']).first()

    if flight:
        return jsonify({"Message": "Flight already exist"})

    date_format = datetime.strptime(flight_new_data['departure_date'], '%y-%m-%d')
    time_format = datetime.strptime(flight_new_data['departure_time'], '%y-%m-%d')
    print(date_format)

    plane = Flight(
        flight_number=flight_new_data['flight_number'],
        point_departure=flight_new_data['point_departure'],
        point_destination=flight_new_data['point_destination'],
        departure_date=date_format,
        departure_time=time_format,
        travel_time=flight_new_data['travel_time'],
        type=flight_new_data['type'],
        price=flight_new_data['price'],
        user_id=flight_new_data['user_id'],
    )

    db.session.add(plane)
    db.session.commit()
    return jsonify({"id": plane.id,
                    "flight_number": plane.flight_number,
                    "point_departure": plane.point_departure,
                    "point_destination": plane.point_destination,
                    "departure_date": plane.departure_date,
                    "departure_time": plane.departure_time,
                    "travel_time": plane.travel_time,
                    "price": plane.price,
                    "user_id": plane.user_id})


@api_flight.route('/flight/<int:id>', methods=['PUT', 'PATCH'])
@protected
def edit_flight(id):
    flight = Flight.query.get(id)
    if not flight:
        return jsonify({"Message": "Category does not exist"})

    update_flight_data = request.get_json()
    flights = Flight.query.filter_by(flight_number=update_flight_data['flight_number']).first()
    if flights:
        return jsonify({"Message": "Flight already exist"})

    flight.flight_number = update_flight_data['flight_number']
    flight.point_departure = update_flight_data['point_departure']
    flight.point_destination = update_flight_data['point_destination']
    flight.departure_date = update_flight_data['departure_date']
    flight.departure_time = update_flight_data['departure_time']
    flight.travel_time = update_flight_data['travel_time']
    flight.type = update_flight_data['type']
    flight.price = update_flight_data['price']
    flight.user_id = update_flight_data['user_id']

    db.session.add(flight)
    db.session.commit()

    return jsonify({"id": flight.id,
                    "flight_number": flight.flight_number,
                    "point_departure": flight.point_departure,
                    "point_destination": flight.point_destination,
                    "departure_date": flight.departure_date,
                    "departure_time": flight.departure_time,
                    "travel_time": flight.travel_time,
                    "price": flight.price,
                    "user_id": flight.user_id})


@api_flight.route('/flight/<int:id>', methods=['DELETE'])
@protected
def delete_institution(id):
    flight = Flight.query.get_or_404(id)
    db.session.delete(flight)
    db.session.commit()

    return jsonify({'Message': 'The flight has been deleted!'})