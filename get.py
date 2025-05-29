import requests
from printer import print_array, print_dict

url = 'https://jsonplaceholder.typicode.com/posts'

params = { 'userId': 1 }

request_with_params = requests.get(url, params=params)

response_json = request_with_params.json()

if isinstance(response_json, list):
    print_array(response_json)
elif isinstance(response_json, dict):
    print_dict(response_json)
else:
    print_dict(response_json)
