#!/usr/bin/python3

from script.translate import translateAPI

def test_tr1():
    text = {"from": "auto",
            "to": "en",
            "text": "hola mundo"}
    assert translateAPI(text) == '"hello world"'

def test_tr2():
    text = {"from": "auto",
            "to": "en",
            "text": "hallo welt"}
    assert translateAPI(text) == '"hello world"'


def test_tr3():
    text = {"from": "auto",
            "to": "en",
            "text": "bonjour le monde"}
    assert translateAPI(text) == '"hello world"'