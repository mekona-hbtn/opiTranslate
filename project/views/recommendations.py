#!/usr/bin/env python3
"""
Recomendations view
==========================
This module contains the logic behind the candidates recommended for the offer.
It selects the database profile techie information to serve in the template.
"""

# Core app & Flask imports
from flask import Blueprint, abort, render_template

# Creates the blueprint of the profile view
recommendations = Blueprint('recommendations', __name__)


@recommendations.route('/recommendations', strict_slashes=False)
def job_offer():
    from project.db import db

    # Gets all the candidates from the DB
    techies = list(db.techie_info.find())
    if not techies:
        abort(404)

    # Prepares variables to be available in the context of the template
    context = {
        'techie': techies
    }

    # Sends the candidates info to the template
    return render_template('recommendations.html', **context)
