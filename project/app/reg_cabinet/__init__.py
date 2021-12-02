from flask import Blueprint, render_template, flash, redirect, url_for
from flask import current_app as app
from .func import validations, write_json
from .forms import Cab_form, LoginFormCabinet

cabinet_blueprint = Blueprint('cabinet', __name__, template_folder="templates/reg_cabinet")

@app.route("/form", methods=['GET', 'POST'])
def form():
    form = LoginFormCabinet()
    flash('password is password or secret')
    if form.validate_on_submit():
        return f'The username is {form.username.data}. The password is {form.password.data}'

    return render_template('form.html', form=form)


@app.route("/register_cabinet", methods=['GET', 'POST'])
def register_cabinet():
    form = Cab_form()
    validations(form)
    if form.validate_on_submit():
        write_json(form)
        flash('User has been written in json file')
        return redirect(url_for('cabinet.register_cabinet'))

    return render_template('cab_form.html', form=form)