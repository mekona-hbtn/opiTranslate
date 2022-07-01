#!/usr/bin/env python3
"""
opiTranslation Application
==========================
This is the file where the execution of the application starts. The back-end
follows the Flask framework. Be sure to run this application in a virtual
environment that has installed the libraries of the file `requirements.txt`.

Please follow the instructions in the README file to run this app.
"""
from project import app

if __name__ == '__main__':
    # Start the application
    app.run()
