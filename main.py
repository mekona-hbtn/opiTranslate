#!/usr/bin/python3

if __name__ == '__main__':
    translateAPI = __import__('translate').translateAPI
    text = {"text": "hola mundo"}

    print(translateAPI(text))
