from flask import Flask, render_template, request, flash, redirect, url_for
import os, sys, platform
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired, Length, AnyOf, Regexp
from func import validations, write_json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdAWdfz21zasdasdaw64!'


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
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('A username is required'),
                                                   Length(min=5, max=10, message='Must be at least 5 and at most 10 '
                                                                                 'characters')])
    password = PasswordField('password',
                             validators=[InputRequired('Password is required'), AnyOf(values=['password', 'secret'])])


@app.route("/form", methods=['GET', 'POST'])
def form():
    form = LoginForm()
    flash('password is password or secret')
    if form.validate_on_submit():
        return f'The username is {form.username.data}. The password is {form.password.data}'

    return render_template('form.html', form=form)


# Lab 5
class Cab_form(FlaskForm):
    email = StringField('Email*', validators=[InputRequired('Email is required'),
                                              Regexp('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'),
                                              Length(min=5, max=30,
                                                     message='Must be at least 5 and at most 10 characters')])
    password1 = PasswordField('Password*', validators=[InputRequired('Password is required'),
                                                       Length(min=6, message='Must be at least 6')])
    password2 = PasswordField('Repeat the password*', validators=[InputRequired('Password is required'),
                                                                  Length(min=6, message='Must be at least 6')])

    # Дані екзаменаційного листка (сертифіката) ЄВІ/ЄФВВ - вказується для вступу до магістратури
    number = StringField('Number*',
                         validators=[InputRequired('Number is required'), Regexp('[0-9]{7}', message='Must be numbers'),
                                     Length(min=7, max=7)])
    pin = StringField('Pin code*',
                      validators=[InputRequired('Pin code is required'), Regexp('[0-9]{4}', message='Must be numbers'),
                                  Length(min=4, max=4)])
    year = SelectField('Year*', choices=[('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2017', '2017'),
                                         ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013')])
    serial = StringField('Serial number', validators=[
        Length(max=3, message='Must be at 2 symbols if year 2015 and least or must be 3 symbols if greater than 2015')])
    number_doc = StringField('Number document*', validators=[Length(min=6, max=8, message='Number document error')])


@app.route("/register_cabinet", methods=['GET', 'POST'])
def register_cabinet():

    form = Cab_form()
    validations(form)
    if form.validate_on_submit():
        write_json(form)
        flash('User has been written in json file')
        return redirect(url_for('register_cabinet'))


    return render_template('cab_form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
