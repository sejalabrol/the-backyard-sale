from flask import Blueprint, flash, redirect, render_template, url_for
from .forms import RegisterForm

views = Blueprint("views", __name__)

@views.route("/")
def home():

    return render_template('home.html')

@views.route('/base')
def base():
    return render_template('base.html')

@views.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        flash('Successfully registered')
        return redirect(url_for('views.home'))

    return render_template('register.html', form = form)

