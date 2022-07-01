#!/usr/bin/python3

import requests

def test_tr1():
    text = {"text": "hola mundo"}
    URL = 'https://t3i8bk3i2i.execute-api.us-east-1.amazonaws.com/opi/translate'
    value_translated = requests.post(URL, json=text).text
    assert value_translated == '"hello world"'
