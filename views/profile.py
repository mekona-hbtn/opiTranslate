#!/usr/bin/env python3
import requests
from flask import Blueprint, render_template

profile = Blueprint('profile', __name__)


@profile.route('/profile', strict_slashes=False)
def candidate():
    from app import techie_info

    # Getting the DB info
    techie = techie_info.find_one({'alias': 'Opgrounder 3438'})
    interview = techie['interview']

    # Request translation to AWS API
    url = 'https://448zpz6x43.execute-api.us-east-1.amazonaws.com/opi/opi'
    translation = {}
    for key, value in interview.items():
        translate = {"text": value}
        translation[key] = requests.post(url, json=translate).text

    # Preparing variables to be available in the context of the template
    context = {
        'techie': techie,
        'interview': interview,
        'translation': translation
    }

    return render_template('profile.html', **context)
