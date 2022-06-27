#!/usr/bin/env python3
"""
Profile view
==========================
This module contains the logic behind the profiles of the candidates in the
offer. It selects the database to work with and connects to the AWS Translate
API to translate the interview.
"""

# Core app & Flask imports
from bson import ObjectId
import requests
from flask import Blueprint, render_template, abort, request, make_response

# Creates the blueprint of the profile view
profile = Blueprint('profile', __name__)


@profile.route('/profile/<id>', methods=['GET', 'POST'], strict_slashes=False)
def candidate(id):
    from app import test

    # Gets the techi info from the DB by id
    by_id = {'_id': ObjectId(id)}
    techie = test.techie_info.find_one(by_id)
    if not techie:
        abort(404)
    interview = techie['interview']

    # Prepares variables to be available in the context of the template
    context = {
        'techie': techie,
        'interview': interview,
    }

    # Handles the Translate button
    if request.method == 'POST':

        # Requests the interview translation to AWS Translate API
        url = 'https://448zpz6x43.execute-api.us-east-1.amazonaws.com/opi/opi'
        translation = {}
        for key, value in interview.items():
            translate = {"text": value}
            value_translated = requests.post(url, json=translate).text
            translation[key] = value_translated.replace('"', '')

        # Saves the translation in the context interview variable
        context['interview'] = translation

    # Sends the techi_info to the template
    return render_template('profile.html', **context)
