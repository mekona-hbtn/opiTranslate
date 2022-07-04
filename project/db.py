#!/usr/bin/env python3
"""
MongoDB Connection
==================
This module makes the connection to the NoSQL database in MongoDB.
"""

# Core Flask & MongoDB imports
from flask import current_app as app
from pymongo import MongoClient

# Conects to the MongoDB server
MONGO_URI = app.config['DB_URI']
mongo = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

# Gets the production and test databases
FLASK_ENV = app.config['ENV']

if FLASK_ENV == 'production':
    app.config.from_object('config.ProductionConfig')
    db = mongo[app.config['DB_NAME']]
else:
    app.config.from_object('config.DevelopmentConfig')
    db = mongo[app.config['DB_NAME']]
