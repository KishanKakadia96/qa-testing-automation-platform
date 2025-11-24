from .base_client import BaseAPIClient

class AuthClient(BaseAPIClient):
    """Client to handle authentication-related API calls."""
    def __init__(self, base_url):
        super().__init__(base_url)

    def login(self, username, password):
        payload = {"username": username, "password": password}
        response = self.post("/auth", data=payload)
        assert response.status_code == 200, f"Login failed: {response.text}"
        return response.json().get("token")

