#!/usr/bin/python3
import requests

def translateAPI(text):
    ENDPOINT = "https://y0fnpgwvgb.execute-api.us-east-1.amazonaws.com/dev/translate"

    response = requests.post(ENDPOINT, json=text)

    return response.text