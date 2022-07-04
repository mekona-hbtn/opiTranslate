#!/usr/bin/env python3
"""
App Settings
============
This module creates the Flaks application, sets the configuration values and
imports the necessary view blueprints.
"""

# Core Flask & MongoDB imports
from flask import Flask, make_response, redirect

# Imports from the Blueprints of the app
from .views.profile import profile
from .views.recommendations import recommendations


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.register_blueprint(profile)
    app.register_blueprint(recommendations)

    @app.route('/', strict_slashes=False)
    def index():
        return make_response(redirect('/recommendations'))

    return app
