import requests
import logging
# import http.client as http_client

# http_client.HTTPConnection.debuglevel = 1

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('urllib3')
logger.setLevel(logging.DEBUG)
logger.propagate = True


url = 'https://jsonplaceholder.typicode.com/posts'
headers = { 'content-type': 'application/json' }

data = { 'title': 'Python', 'body': 'Hello World', 'userId': 1 }

request_with_body = requests.post(url, data=data)

if request_with_body.status_code == 201:
    print(request_with_body.json())
