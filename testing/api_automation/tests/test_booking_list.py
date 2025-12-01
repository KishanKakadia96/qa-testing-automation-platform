import pytest

@pytest.mark.parametrize("filter_param", [None, "2019-12-02", "2018-01-01"])
def test_booking_list_filtering(booking_client, filter_param):
    """
    Test booking list retrieval with and without filters.
    Test covers: TC029-TC031, TC061-TC064, TC072
    """ 
    params = {}
    if filter_param:
        params["checkin"] = filter_param
        bookings = booking_client.get_all_bookings(**params)
        assert bookings.status_code == 200
        for booking in bookings.json():
            booking_details = booking_client.get_booking(booking['bookingid'])
            assert booking_details.status_code == 200
            booking_data = booking_details.json()
            assert booking_data['bookingdates']['checkin'] == filter_param