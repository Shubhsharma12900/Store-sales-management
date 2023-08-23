#!/usr/bin/python3

import os

# Flask configuration
SECRET_KEY = os.environ.get('APP_SECRET_KEY')

# MySQL configuration
DB_HOST = os.environ.get('127.0.0.1')
DB_USER = os.environ.get('root')
DB_PASSWORD = os.environ.get('Shubham12')
DB_DATABASE = os.environ.get('fresh_basket')

# MySQL connection config
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Shubham12@',
    'database': 'fresh_basket'
}
