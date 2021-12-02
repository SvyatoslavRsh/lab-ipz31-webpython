from flask import Flask, render_template, request, flash, redirect, url_for
from . import app
import os, sys, platform
from datetime import datetime
from .func import validations, write_json
from .forms import Cab_form, LoginFormCabinet, LoginForm, RegisterForm
from . import app, db, bcrypt
from .models import User

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
    form = LoginFormCabinet()
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


# lab7
@app.route("/register", methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=bcrypt.generate_password_hash(format(form.password1.data)))
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data} !', category='success')
        return redirect(url_for('login'))
    return render_template('register.html', form_reg=form, title='Register')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form_log = LoginForm()
    if form_log.validate_on_submit():
        try:
            email = User.query.filter_by(email=form_log.email.data).first().email
            password = User.query.filter_by(email=form_log.email.data).first().password
        except AttributeError:
            flash('Invalid login or password!', category='success')
            return redirect(url_for('login'))

        if form_log.email.data == email and bcrypt.check_password_hash(password, form_log.password.data) == True:
            flash(f'You have been logged by username {User.query.filter_by(email=form_log.email.data).first().username}!', category='success')
            return redirect(url_for('login'))
        else:
            flash('Login unsuccessful', category='success')

    return render_template('login.html', form_log=form_log, title='Login')


@app.route("/users", methods=['GET', 'POST'])
def users():
    all_users = User.query.all()
    return render_template('user_list.html', all_users=all_users)
