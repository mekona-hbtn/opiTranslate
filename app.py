#!/usr/bin/env python3
import requests
from flask import Flask
from pymongo import MongoClient
from views.profile import profile

app = Flask(__name__)
app.register_blueprint(profile)

mongo = MongoClient(
    'mongodb+srv://opitranslate.dkaoilj.mongodb.net',
    username='root', password='toor')

db = mongo['opground_test_db']
techie_info = db['techie_info']


if __name__ == '__main__':
    app.run(port=5000, debug=True)
