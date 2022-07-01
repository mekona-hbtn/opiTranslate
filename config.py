#!/usr/bin/env python3
""""
App Config
===========
This module handles the Flask configuration setting for the application.
"""

# Gets the enviroment variables
import os


# Base configuration for the app
class Config(object):
    TESTING = False
    DB_URI = os.environ.get('OPDB_URI')
    DB_NAME = os.environ.get('DEV_DB_NAME')
    AWS_TRANSLATE = os.environ.get('AWS_TRANSLATE')


# Development environment configuration for the app
class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = os.environ.get('DEV_DB_NAME')


# Test environment configuration for the app
class TestConfig(Config):
    DEBUG = True
    TESTING = True
    DB_NAME = os.environ.get('TEST_DB_NAME')


# Production environment configuration for the app
class ProductionConfig(Config):
    DB_NAME = os.environ.get('PROD_DB_NAME')
