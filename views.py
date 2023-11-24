from flask import Blueprint, render_template
from flask_login import login_required
import datetime
views = Blueprint('views', __name__)

@views.route('/')
def home():
    '''
    asking server for a current time
    which actually is quite dumb
    considering user could easily be
    in a different timezone.
    yet it's quite demonstrative
    '''
    date_str ='{dt:%B} {dt.day}th {dt.year}'.format(dt=datetime.datetime.now())
    return render_template('home.html', check=date_str)

@views.route('/success', methods=['GET', 'POST'])
@login_required
def success():
    return render_template('success.html')