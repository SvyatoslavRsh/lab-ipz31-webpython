from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, DateField
from wtforms.validators import Length, DataRequired, InputRequired


class FlightForm(FlaskForm):
    flight_number = IntegerField('Flight number')
    point_departure = StringField('Point departure')
    point_destination = StringField('Point destination')
    departure_date = DateField('Departure date')
    departure_time = DateField('Departure time')
    travel_time = IntegerField('Travel time / hours')
    route_type = SelectField('Route type', choices=[('Internal', 'Internal'), ('International', 'International')])
    price = IntegerField('Price $')
