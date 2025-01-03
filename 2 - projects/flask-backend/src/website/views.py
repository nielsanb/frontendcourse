from flask import Blueprint, render_template
from flask_login import current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', current_user=current_user)


@views.route('/notes')
def notes():
    return render_template('notes.html', current_user=current_user)