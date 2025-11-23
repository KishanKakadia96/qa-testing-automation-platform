import requests

class BaseAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')

    def get(self, endpoint, params=None, headers=None, cookies=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params, headers=headers, cookies=cookies)

    def post(self, endpoint, data=None, headers=None, cookies=None):
        return requests.post(f"{self.base_url}{endpoint}", json=data, headers=headers, cookies=cookies)

    def put(self, endpoint, data=None, headers=None, cookies=None):
        return requests.put(f"{self.base_url}{endpoint}", json=data, headers=headers, cookies=cookies)

    def delete(self, endpoint, headers=None, cookies=None):
        return requests.delete(f"{self.base_url}{endpoint}", headers=headers, cookies=cookies)
