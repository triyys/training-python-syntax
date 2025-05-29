import requests

class TimeoutSession(requests.Session):
    def __init__(self, timeout=5):
        super().__init__()
        self.timeout = timeout

    def request(self, *args, **kwargs):
        kwargs.setdefault('timeout', self.timeout)
        return super().request(*args, **kwargs)


with TimeoutSession(3) as session:
    try:
        # Persist cookie
        session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
        r = session.get('https://httpbin.org/cookies')
        print(r.text)

        # Timeout
        response = session.get('https://httpbin.org/delay/5')
        print(response.status_code)
    except requests.exceptions.Timeout:
        print("Request timed out")
