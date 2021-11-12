from flask import Flask, render_template, request, flash, redirect, url_for
from . import app
import os, sys, platform
from datetime import datetime
from .func import validations, write_json
from .forms import Cab_form, LoginForm


@app.route("/blog")
def blog():
    news_dict = {
        'first day': 'I feel good',
        'Second Day': 'I feel bad',
        'Third Day': 'I happy',
    }
    return render_template("blog.html", news_dict=news_dict, sys_info=request.headers.get('User-Agent'),
                           sys=sys.version, os_name=os.name, platform=platform.system(), release=platform.release(),
                           date=datetime.now())


@app.route("/news")
def sale():
    sale_dict = {
        'Iphone x': '256$',
        'I Mac': '1999$',
        'Samsung s12': '599$',

    }
    return render_template("sale.html", sale_dict=sale_dict, sys_info=request.headers.get('User-Agent'),
                           sys=sys.version, os_name=os.name, platform=platform.system(), release=platform.release(),
                           date=datetime.now())


@app.route("/")
def aboutme():
    return render_template("aboutme.html", boolean=False, name='Svyatoslav', error='Wrong data',
                           sys_info=request.headers.get('User-Agent'), sys=sys.version, os_name=os.name,
                           platform=platform.system(), release=platform.release(), date=datetime.now())


# Lab 4
@app.route("/form", methods=['GET', 'POST'])
def form():
    form = LoginForm()
    flash('password is password or secret')
    if form.validate_on_submit():
        return f'The username is {form.username.data}. The password is {form.password.data}'

    return render_template('form.html', form=form)


# Lab 5
@app.route("/register_cabinet", methods=['GET', 'POST'])
def register_cabinet():
    form = Cab_form()
    validations(form)
    if form.validate_on_submit():
        write_json(form)
        flash('User has been written in json file')
        return redirect(url_for('register_cabinet'))

    return render_template('cab_form.html', form=form)
