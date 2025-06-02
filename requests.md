## Call được get với params
- Code
```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'

params = { 'userId': 1 }

request_with_params = requests.get(url, params=params)

response_json = request_with_params.json()

print(response_json)
```
- Console
```
[{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident...
```
## Call được post có body và header
- Code
```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'

headers = { 'content-type': 'application/json' }

data = { 'title': 'Python', 'body': 'Hello World', 'userId': 1 }

request_with_body = requests.post(url, json=data, headers=headers)

if request_with_body.status_code == 201:
    print(request_with_body.json())

if request_with_body.status_code == 500:
    print(request_with_body.text)
```
- Console
```
{'title': 'Python', 'body': 'Hello World', 'userId': 1, 'id': 101}
```
## Logging request
Chèn thêm đoạn code sau để bật HTTP Logging
- Code
```python
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('urllib3')
logger.setLevel(logging.DEBUG)
logger.propagate = True
```
- Console
```
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): jsonplaceholder.typicode.com:443
{'title': 'Python', 'body': 'Hello World', 'userId': 1, 'id': 101}
DEBUG:urllib3.connectionpool:https://jsonplaceholder.typicode.com:443 "POST /posts HTTP/1.1" 201 76
```

## Session Objects in Requests
### 1. Sử dụng lại connection khi request nhiều lần đến cùng 1 host giúp cải thiện tốc độ
Đoạn code gọi API 10 lần với 2 cách gọi:
object của `requests.Session()` và `requests.get()` và so sánh tốc độ.
Đồng thời bật HTTP Logging để kiểm tra số lần mở HTTP connection giữa 2 cách.
- Code
```python
import time
import requests

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('urllib3')
logger.setLevel(logging.DEBUG)
logger.propagate = True

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
```
- Console
```
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): jsonplaceholder.typicode.com:443
DEBUG:urllib3.connectionpool:https://jsonplaceholder.typicode.com:443 "GET /posts HTTP/1.1" 200 None
DEBUG:urllib3.connectionpool:https://jsonplaceholder.typicode.com:443 "GET /posts HTTP/1.1" 200 None
...
Requests session: 0.4879951477050781

DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): jsonplaceholder.typicode.com:443
DEBUG:urllib3.connectionpool:https://jsonplaceholder.typicode.com:443 "GET /posts HTTP/1.1" 200 None
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): jsonplaceholder.typicode.com:443
DEBUG:urllib3.connectionpool:https://jsonplaceholder.typicode.com:443 "GET /posts HTTP/1.1" 200 None
...
Requests: 0.9626059532165527
```
### 2. Lưu lại cookie giữa các request
Đoạn code khởi tạo 1 object của `Session`
và gọi đến API `/cookies/set/sessioncookie/123456789` (mô phỏng set cookie).
Sau đó, tiếp tục gọi đến API `/cookies` để xem cookie được gửi chung với request này.
- Code
```python
import requests

s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)
```
- Console
```
{
  "cookies": {
    "sessioncookie": "123456789"
  }
}
```
### 3. Thêm header để dùng lại cho nhiều request
Đoạn code set header `x-test1` và dùng lại với nhiều request
- Code
```python
import requests

s = requests.Session()
s.headers.update({ 'x-test1': 'first' })

response1 = s.get('https://httpbin.org/headers')
response2 = s.get('https://httpbin.org/headers', headers={ 'x-test2': 'second' })
print(response1.json())
print(response2.json())
```
- Console
```
{'headers': { ... 'X-Test1': 'first'}}
{'headers': { ... 'X-Test1': 'first', 'X-Test2': 'second'}}
```

## Set timeout
Đoạn code gọi đến API `/delay/5` (mô phỏng thời gian trả về là 5 giây) nhưng với tham số `timeout=3`.
Do đó thư viện quăng lỗi `requests.exceptions.Timeout` và in ra thông báo.
- Code
```python
import requests

with requests.Session() as session:
    try:
        response = session.get('https://httpbin.org/delay/5', timeout=3)

        print(response.status_code)
    except requests.exceptions.Timeout:
        print('Request timed out')
```
- Console
```
Request timed out
```

## Làm sao để chạy async với requests?
Không thể chạy được async với requests vì:
- async/await trong python chỉ chạy nếu bên dưới nó là non-blocking I/O
- requests không hỗ trợ bất kỳ non-blocking I/O nào
[blocking-or-non-blocking](https://requests.readthedocs.io/en/latest/user/advanced/#blocking-or-non-blocking)

Thay vào đó, ta có thể sử dụng các thư viện khác hỗ trợ async như
[httpx](https://github.com/encode/httpx),
[grequests](https://github.com/spyoungtech/grequests),
[aiohttp](https://github.com/aio-libs/aiohttp), ...
