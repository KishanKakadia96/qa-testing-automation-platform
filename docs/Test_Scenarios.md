# Test Scenarios for Restful Booker Application

## Scenario 1: Valid Booking Creation
**Preconditions:** Application online, API accessible.
**Steps:**
1. Open booking creation form.
2. Enter valid data for all required fields.
3. Submit the form.
**Expected Result:** Booking successfully created and listed.

## Scenario 2: Booking Update
**Preconditions:** Existing booking present.
**Steps:**
1. Select booking to update.
2. Modify booking details.
3. Submit changes.
**Expected Result:** Booking updated successfully.

## Scenario 3: Booking Deletion
**Preconditions:** Existing booking present.
**Steps:**
1. Select booking to delete.
2. Confirm deletion.
**Expected Result:** Booking removed from system.

## Scenario 4: API Authentication
**Preconditions:** API accessible.
**Steps:**
1. Submit login request with valid credentials.
2. Receive authentication token.
**Expected Result:** Token received for authenticated requests.

## Scenario 5: Form Validation
**Preconditions:** Booking form open.
**Steps:**
1. Submit form with missing required fields.
**Expected Result:** Validation errors displayed.

## Scenario 6: Error Handling
**Preconditions:** API accessible.
**Steps:**
1. Submit invalid API requests.
**Expected Result:** Proper error responses like 400, 403, etc.

## Scenario 7: Data Consistency via API
**Preconditions:** Booking created.
**Steps:**
1. Retrieve booking via API.
2. Compare data to original submission.
**Expected Result:** Data matches exactly.

## Scenario 8: Handling Invalid Input
**Preconditions:** Booking form open/API accessible.
**Steps:**
1. Submit booking with invalid dates or negative price.
**Expected Result:** Appropriate error handling.

## Scenario 9: Booking List Display
**Preconditions:** Multiple bookings exist.
**Steps:**
1. Load booking list UI.
**Expected Result:** All bookings displayed correctly.

## Scenario 10: Security Testing
**Preconditions:** API requires authentication for updates/deletions.
**Steps:**
1. Attempt unauthorized booking update or deletion.
**Expected Result:** Request denied with error.
