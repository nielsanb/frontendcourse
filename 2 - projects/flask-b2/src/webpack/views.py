from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('page.html')

@views.route('/notes')
@login_required
def notes():
    return render_template('notes.html')