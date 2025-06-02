import requests
from printer import print_array, print_dict
from database import use_peewee

import logging

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

    print(response_json)

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
            # Timeout
            response = session.get('https://httpbin.org/delay/5', timeout=3)
            print(response.status_code)
        except requests.exceptions.Timeout:
            print('Request timed out')

# get_with_params()
# post_with_body_and_header()
# session_request_timeout()

# Persist cookie
s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)

import time

# Requests session
s = requests.Session()
start = time.time()
for i in range(10):
    s.get('https://jsonplaceholder.typicode.com/posts')
print(f'Requests session: {time.time() - start}')

# Requests
start = time.time()
for i in range(10):
    requests.get('https://jsonplaceholder.typicode.com/posts')
print(f'Requests: {time.time() - start}')

# Headers
s = requests.Session()
s.headers.update({ 'x-test1': 'first' })

response1 = s.get('https://httpbin.org/headers')
response2 = s.get('https://httpbin.org/headers', headers={ 'x-test2': 'second' })
print(response1.json())
print(response2.json())

# Exercise 2 -> database.py
# use_peewee()
