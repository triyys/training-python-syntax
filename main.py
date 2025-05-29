import requests
from printer import print_array, print_dict
from database import use_peewee

import logging
# import http.client as http_client

# http_client.HTTPConnection.debuglevel = 1

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('urllib3')
logger.setLevel(logging.DEBUG)
logger.propagate = True

# Exercise 1
url = 'https://jsonplaceholder.typicode.com/posts'

def get_with_params():
    params = { 'userId': 1 }

    request_with_params = requests.get(url, params=params)

    response_json = request_with_params.json()

    if isinstance(response_json, list):
        print_array(response_json)
    elif isinstance(response_json, dict):
        print_dict(response_json)
    else:
        print_dict(response_json)

def post_with_body_and_header():
    headers = { 'content-type': 'application/json' }

    data = { 'title': 'Python', 'body': 'Hello World', 'userId': 1 }

    request_with_body = requests.post(url, json=data, headers=headers)

    if request_with_body.status_code == 201:
        print(request_with_body.json())

    if request_with_body.status_code == 500:
        print(request_with_body.text)

def session_request_timeout():
    with requests.Session() as session:
        try:
            # Persist cookie
            session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
            r = session.get('https://httpbin.org/cookies')
            print(r.text)

            # Timeout
            response = session.get('https://httpbin.org/delay/5', timeout=3)
            print(response.status_code)
        except requests.exceptions.Timeout:
            print("Request timed out")

# get_with_params()
# post_with_body_and_header()
# session_request_timeout()

# Exercise 2 -> database.py
use_peewee()
