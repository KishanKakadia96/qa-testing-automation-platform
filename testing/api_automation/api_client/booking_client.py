from .base_client import BaseAPIClient

class BookingClient(BaseAPIClient):
    def __init__(self, base_url):
        super().__init__(base_url)

    def create_booking(self, data):
        return self.post("/booking", data=data)

    def get_booking(self, booking_id):
        return self.get(f"/booking/{booking_id}")

    def update_booking(self, booking_id, data, token):
        headers = {"Cookie": f"token={token}"}
        return self.put(f"/booking/{booking_id}", data=data, headers=headers)

    def delete_booking(self, booking_id, token):
        headers = {"Cookie": f"token={token}"}
        return self.delete(f"/booking/{booking_id}", headers=headers)
