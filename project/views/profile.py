#!/usr/bin/env python3
"""
Profile view
==========================
This module contains the logic behind the profiles of the candidates in the
offer. It selects the database to work with and connects to the AWS Translate
API to translate the interview.
"""

# Core app & Flask imports
import requests
from bson import ObjectId
from datetime import datetime
from flask import Blueprint, abort, current_app, render_template, request

# Creates the blueprint of the profile view
profile = Blueprint('profile', __name__)


@profile.route('/profile/<id>', methods=['GET', 'POST'], strict_slashes=False)
def candidate(id):
    from project.db import db

    # Gets the techi info from the DB by id
    by_id = {'_id': ObjectId(id)}
    techie = db.techie_info.find_one(by_id)

    if not techie:
        abort(404)

    interview = techie['interview']

    # Prepares variables to be available in the context of the template
    context = {
        'techie': techie,
        'birthdate': datetime.strftime(techie['birthdate'], '%d %B %Y'),
        'interview': interview
    }

    # Handles the Translate button
    if request.method == 'POST':

        # Requests the interview translation to AWS Translate API
        URL = current_app.config['AWS_TRANSLATE']
        translation = {}
        for key, value in interview.items():
            if value:
                translate = {"text": value}
                value_translated = requests.post(URL, json=translate).text
                translation[key] = value_translated.replace('"', '')
            else:
                translation[key] = ""

        # Saves the translation in the context interview variable
        context['interview'] = translation

    # Sends the techi_info to the template
    return render_template('profile.html', **context)
