#!/usr/bin/env python3
"""
opiTranslation Application
==========================
This is the file where the execution of the application starts. The back-end
follows the Flask framework, imports the necessary view blueprints and connects
to a NoSQL database in MongoDB.

Be sure to run this application in a virtual environment that has installed all
the libraries of the file `requirements.txt`
"""

# Core Flask & MongoDB imports
from flask import Flask
from pymongo import MongoClient

# Imports from the Blueprints of the app
from views.profile import profile

# Conects to the MongoDB server
user, code, cluster = 'root', 'toor', 'opitranslate.dkaoilj.mongodb.net'
uri = f'mongodb+srv://{user}:{code}@{cluster}/?retryWrites=true&w=majority'

mongo = MongoClient(uri, serverSelectionTimeoutMS=5000)

# Gets the production and test databases
test = mongo['opground_test_db']



if __name__ == '__main__':
    # Creates the application & register the blueprints
    app = Flask(__name__)
    app.register_blueprint(profile)

    # Start the application
    app.run(port=5000, debug=True)
