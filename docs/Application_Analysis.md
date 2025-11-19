# Restful Booker - Application Analysis

## 1. Application Overview

**Application Name:** Restful Booker
**URL:** https://restful-booker.herokuapp.com/
**Purpose:** Hotel booking REST API with a simple web interface
**Technology:** Single-page application with REST backend
**Status:** Active (Staging/Demo environment)

---

## 2. Key Features

### 2.1 Booking Management
- **Create Booking:** Users can create new hotel bookings with User details
- **View Bookings:** Display list of all created bookings
- **Update Booking:** Modify existing booking details
- **Delete Booking:** Remove bookings from the system

### 2.2 Form Validation
- First Name: Required (text input)
- Last Name: Required (text input)
- Total Price: Required (numeric input)
- Deposit Paid: Optional (boolean checkbox)
- Check-in Date: Required (date)
- Check-out Date: Required (date)
- Additional Needs: Optional (text input)

### 2.3 Business Rules
- Check-out date must be after or equal to check-in date
- Price should be a positive number
- User names are required for any booking
- Bookings persist between sessions
- All bookings are publicly accessible (no authentication required for view)

---

## 3. User Workflows

### 3.1 Create Booking Workflow
1. User opens application at home page
2. User clicks "Create Booking" or similar button
3. Form page opens
4. User fills in all required fields:
   - First Name
   - Last Name
   - Check-in Date
   - Check-out Date
   - Total Price
5. User optionally adds:
   - Deposit Paid (checkbox)
   - Additional Needs (text)
6. User submits form
7. Booking is created and assigned a unique ID
8. Confirmation message appears
9. New booking appears in the list

### 3.2 Update Booking Workflow
1. User views the bookings list
2. User identifies booking to update (by ID or User name)
3. User clicks Edit/Update button
4. Pre-filled form opens with current booking data
5. User modifies desired fields
6. User submits form
7. Booking is updated
8. Success message appears
9. List updates with new information

### 3.3 Delete Booking Workflow
1. User views the bookings list
2. User identifies booking to delete
3. User clicks Delete button
4. Confirmation dialog appears
5. User confirms deletion
6. Booking is removed from the list
7. Success message appears

### 3.4 View Bookings Workflow
1. User opens application
2. Application loads list of all bookings
3. Each booking shows: ID, User Name, Check-in, Check-out, Price
4. User can scroll through all bookings
5. User can search/filter bookings

---

## 4. UI Components

### 4.1 Form Fields
| Field | Type | Required | Validation |
|-------|------|----------|-----------|
| First Name | Text Input | Yes | Non-empty, alphanumeric |
| Last Name | Text Input | Yes | Non-empty, alphanumeric |
| Check-in | Date | Yes | Valid date format |
| Check-out | Date | Yes | Valid date, >= checking |
| Total Price | Number Input | Yes | Positive number |
| Deposit Paid | Checkbox | No | Boolean |
| Additional Needs | Textarea | No | Optional text |

### 4.2 Buttons & Controls
- **Create Booking Button:** Opens new booking form
- **Save Button:** Submits form (Create/Update)
- **Cancel Button:** Closes form without saving
- **Edit Button:** Opens booking for editing
- **Delete Button:** Removes booking with confirmation
- **Refresh Button:** Reloads booking list

### 4.3 Messages & Alerts
- Booking creation success message
- Booking update success message
- Booking deletion success message
- Form validation error messages
- General error messages

---

## 5. Data Model

### 5.1 Booking Object
```json
{
    "firstname": "Josh",
    "lastname": "Allen",
    "totalprice": 111,
    "depositpaid": true,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "super bowls"
}
```

---

## 6. Test Scenarios

### Scenario 1: Valid Booking Creation
- User can create booking with all valid information
- Expected: Booking created, confirmation shown, appears in list

### Scenario 2: Missing Required Field
- User leaves "First Name" empty and attempts to create
- Expected: Error message displayed, booking not created

### Scenario 3: Invalid Date Range
- User sets check-out date before check-in date
- Expected: Error message or validation

### Scenario 4: Booking Update
- User modifies existing booking details
- Expected: Changes saved, list updated

### Scenario 5: Booking Deletion
- User deletes existing booking
- Expected: Booking removed from list, confirmation shown

### Scenario 6: Form Validation - Negative Price
- User enters negative price
- Expected: Validation error

### Scenario 7: Empty Booking List
- System state: No bookings exist
- Expected: Empty list message or no bookings displayed

### Scenario 8: Multiple Bookings
- System state: 5+ bookings exist
- Expected: All bookings displayed, scrollable list

### Scenario 9: Long Text Input
- User enters very long name or additional needs
- Expected: Text accepted and displayed correctly

### Scenario 10: Special Characters
- User enters special characters in name field
- Expected: Accepted or proper validation message

---

## 7. Application Limitations & Observations

- No authentication required for basic operations
- Bookings appear to be in a shared/public state
- Data persists between browser sessions
- Hosted on Heroku (demo/staging environment)
- Simple, minimalist UI design
- No pagination visible (loads all bookings)
- No search/filter functionality observed (verify)

---

## 8. Test Strategy Implications

Based on this analysis:

### Manual Testing Focus
- Form validation edge cases
- CRUD workflow completeness
- User error recovery
- Data persistence

### API Testing Focus
- All endpoints functional
- Request/response formats correct
- Status codes appropriate
- Error handling robust

### UI Testing Focus
- Form submission flow
- Confirmation messages display
- Booking list rendering
- Cross-browser compatibility

---

## Document Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-18 | QA Team | Initial application analysis |

---

**Status:** Ready for API documentation phase