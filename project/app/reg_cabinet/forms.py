from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, AnyOf, Regexp, EqualTo, DataRequired, ValidationError


class LoginFormCabinet(FlaskForm):
    username = StringField('username', validators=[InputRequired('A username is required'),
                                                   Length(min=5, max=10, message='Must be at least 5 and at most 10 '
                                                                                 'characters')])
    password = PasswordField('password',
                             validators=[InputRequired('Password is required'), AnyOf(values=['password', 'secret'])])


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

