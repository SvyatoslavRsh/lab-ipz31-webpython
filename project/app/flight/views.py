from flask import render_template, url_for, redirect, flash
from .forms import FlightForm
from .models import Flight
from flask_login import current_user, login_required
from .. import db
from . import flight_blueprint


@flight_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def flights():
    fl = Flight.query.all()
    return render_template('flights.html', flights=fl)


@flight_blueprint.route('/createFlight', methods=['GET', 'POST'])
@login_required
def create_flight():
    form = FlightForm()

    if form.validate_on_submit():
        flights = Flight(flight_number=form.flight_number.data, point_departure=form.point_departure.data,
                         point_destination=form.point_destination.data, departure_date=form.departure_date.data,
                         departure_time=form.departure_time.data, travel_time=form.travel_time.data,
                         type=form.route_type.data, price=form.price.data, user_id=current_user.id)

        db.session.add(flights)
        db.session.commit()

        return redirect(url_for('flight.flights'))

    return render_template('flight_form.html', form=form, UD='Create')


@flight_blueprint.route('/deleteFlight/<id>', methods=['GET', 'POST'])
@login_required
def del_flight(id):
    flight = Flight.query.get_or_404(id)
    if current_user.id == flight.user_id:
        db.session.delete(flight)
        db.session.commit()
        return redirect(url_for('flight.flights'))

    flash('Error', category='warning')
    return redirect(url_for('flight.flight_item', fli=id))


@flight_blueprint.route('/upd<fli>', methods=['GET', 'POST'])
@login_required
def upd_flight(fli):
    fl = Flight.query.get_or_404(fli)
    if current_user.id != fl.user_id:
        flash('Error', category='warning')
        return redirect(url_for('inst.detail_inst', pk=fl))

    form = FlightForm()

    if form.validate_on_submit():
        fl.flight_number = form.flight_number.data
        fl.point_departure = form.point_departure.data
        fl.point_destination = form.point_destination.data
        fl.departure_date = form.departure_date.data
        fl.departure_time = form.departure_time.data
        fl.travel_time = form.travel_time.data
        fl.type = form.route_type.data
        fl.price = form.price.data

        db.session.add(fl)
        db.session.commit()

        flash('Update done', category='access')
        return redirect(url_for('flight.flight_item', fli=fli))

    form.flight_number.data = fl.flight_number
    form.point_departure.data = fl.point_departure
    form.point_destination.data = fl.point_destination
    form.departure_date.data = fl.departure_date
    form.departure_time.data = fl.departure_time
    form.travel_time.data = fl.travel_time
    form.route_type.data = fl.type
    form.price.data = fl.price

    return render_template('flight_form.html', form=form, UD='Update')


@flight_blueprint.route('/<fli>', methods=['GET', 'POST'])
@login_required
def flight_item(fli):
    fl = Flight.query.get_or_404(fli)
    return render_template('flight_item.html', flight=fl)
