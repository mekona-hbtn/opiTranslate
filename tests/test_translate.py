#!/usr/bin/python3

import os
import requests
from dotenv import load_dotenv

load_dotenv('.env')


def test_tr1():
    text = {"text": "hola mundo"}
    URL = os.environ.get('AWS_TRANSLATE')
    value_translated = requests.post(URL, json=text).text
    assert value_translated == '"hello world"'


def test_tr2():
    text = {"text": "bonjour le monde"}
    URL = os.environ.get('AWS_TRANSLATE')
    value_translated = requests.post(URL, json=text).text
    assert value_translated == '"hello world"'


def test_tr3():
    text = {"text": "hallo welt"}
    URL = os.environ.get('AWS_TRANSLATE')
    value_translated = requests.post(URL, json=text).text
    assert value_translated == '"hello world"'
