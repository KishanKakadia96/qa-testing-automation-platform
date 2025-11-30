import pytest
import json
from .conftest import load_test_data

# Load test data from JSON files
test_data = load_test_data('bookings_test_data.json')

@pytest.mark.parametrize("test_item", test_data)
def test_booking_validation_cases(booking_client, test_item):
    """
    Test various booking creation scenarios for validation.
    Test Covers: TC002, TC008, TC012-TC013, TC020, TC022, TC032-TC036, TC045, TC047, TC052, TC068
    """
    
    test_case = test_item["test_case"]
    description = test_item["description"]
    data = test_item["data"]
    expected_status = test_item["expected_status"]
    
    print(f"\n{'='*80}")
    print(f"TEST CASE: {test_case} - {description}")
    print(f"{'='*80}")
    print(f"\n REQUEST PAYLOAD:")
    print(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"\n Expected Status: {expected_status}")
    
    response = booking_client.post("/booking", data=data)
    
    print(f"Actual Status: {response.status_code}")
    print(f"\n RESPONSE BODY:")
    try:
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except:
        print(response.text)
    
    if response.status_code == 200 and expected_status == 200:
        print(f"TEST PASSED - Status code is acceptable ({response.status_code})")
    elif response.status_code != expected_status:
        print(f"TEST FAILED - Expected status {expected_status}, got {response.status_code}")
    else:
        print(f"TEST PASSED - Received expected status code ({response.status_code})")
    
    print(f"{'='*80}\n")
    
    assert response.status_code == expected_status