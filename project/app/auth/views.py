from flask import url_for, render_template, flash, redirect, abort
from .. import db
from .forms import RegisterForm, LoginForm
from .models import User
from flask_login import login_user, current_user, logout_user, login_required

from . import auth_blueprint


@auth_blueprint.route("/register", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('blog'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data} !', category='success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form_reg=form, title='Register')


@auth_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    form_log = LoginForm()
    if form_log.validate_on_submit():
        user = User.query.filter_by(email=form_log.email.data).first()
        if user and user.verify_password(form_log.password.data):
            login_user(user, remember=form_log.remember.data)
            flash(f'You have been logged by username {user.email}!', category='success')
            return redirect(url_for('auth.account'))
        else:
            flash('Invalid login or password!', category='warning')
            return redirect(url_for('auth.login'))

    return render_template('login.html', form_log=form_log, title='Login')


@auth_blueprint.route("/users", methods=['GET', 'POST'])
@login_required
def users():
    all_users = User.query.all()
    count = User.query.count()
    if count == 0:
        abort(404)
    return render_template('user_list.html', all_users=all_users, count=count)


@auth_blueprint.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

@auth_blueprint.route("/logout")
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('blog'))

@auth_blueprint.route("/account")
@login_required
def account():
    return render_template('account.html')