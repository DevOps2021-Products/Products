"""
Global Configuration for Application
"""
import os
import json
import logging

SECRET_KEY = 'secret-for-dev'
LOGGING_LEVEL = logging.INFO

# Get configuration from environment
DATABASE_URI = os.getenv(
    "DATABASE_URI",
    "postgres://postgres:postgres@localhost:5432/postgres"
)
# override if we are running in Cloud Foundry
if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.environ['VCAP_SERVICES'])
    creds = vcap['cloudantNoSQLDB'][0]['credentials']
    hostname = creds['host']
    password = creds['password']
    port = int(creds['port'])
    DATABASE_URI = vcap['user-provided'][0]['credentials']['url']
# Configure SQLAlchemy
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False