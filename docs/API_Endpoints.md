# Restful Booker - API Endpoints Documentation

## API Overview

**Base URL:** https://restful-booker.herokuapp.com/
**API Version:** v1
**Documentation:** https://restful-booker.herokuapp.com/apidoc/v1/
**Format:** JSON
**Authentication:** Token-based access

---

## Authentication

### POST /auth/

Authenticate user and obtain authentication token for modification.

**Method:** `POST`

**URL:** `/auth/`

**Headers:**
**Content-Type:** application/json
**Accept:** application/json

**Request Body:**
```json
{
    "username": "admin",
    "password": "password123"
}
```

**Response (200 OK):**
```json
{
    "token": "f36513dc40faf7e"
}
```

**Status Codes:**
- `200 OK` - Login successful, token returned
- `400 Bad Request` - Invalid credentials request
- `401 Unauthorized` - Invalid username or password

**Notes:**
- Token is required for PUT and DELETE operations
- Token can be passed in Cookie header: `Cookie: token=f36513dc40faf7e`
- Token does expire in this demo environment

---

## Bookings Endpoints

### GET /booking

Retrieve all bookings with optional filtering.

**Method:** `GET`

**URL:** `/booking`

**Query Parameters (Optional):**
**?firstname=** John - Filter by first name
**?lastname=** Doe - Filter by last name
**?checkin=** 2025-12-15 - Filter by check-in date (YYYY-MM-DD)
**?checkout=** 2025-12-20 - Filter by check-out date (YYYY-MM-DD)

**Headers:**
**Accept:** application/json

**Response (200 OK):**
```json
[
  {
    "bookingid": 1
  },
  {
    "bookingid": 2
  },
  {
    "bookingid": 3
  },
  {
    "bookingid": 4
  }
]
```

**Status Codes:**
- `200 OK` - Bookings retrieved successfully
- `500 Internal Server Error` - Server error

**Example Requests:**
1. Get all bookings
**GET** `/booking`

2. Filter by User name
**GET** `/booking?firstname=John&lastname=Doe`

3. Filter by dates
**GET** `/booking?checkin=2025-12-15&checkout=2025-12-20`

**Notes:**
- Returns array of booking IDs
- Use booking ID to get full details (see GET /booking/{id})
- Filtering is optional
- No authentication required

---

### GET /booking/{id}

Retrieve specific booking by ID.

**Method:** `GET`

**URL:** `/booking/{id}`

**Path Parameters:**
- `id` (required) - Integer booking ID

**Headers:**
**Accept:** application/json

**Response (200 OK):**
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

**Status Codes:**
- `200 OK` - Booking retrieved
- `404 Not Found` - Booking ID does not exist
- `500 Internal Server Error` - Server error

**Example:**
**GET** `/booking/1`

**Notes:**
- No authentication required
- Returns full booking details
- booking ID must be valid integer

---

### POST /booking

Create new booking.

**Method:** `POST`

**URL:** `/booking`

**Headers:**
**Content-Type:** application/json
**Accept:** application/json

**Request Body:**
```json
{
    "firstname": "John",
    "lastname": "Doe",
    "totalprice": 150,
    "depositpaid": true,
    "bookingdates": {
    "checkin": "2025-12-15",
    "checkout": "2025-12-20"
    },
    "additionalneeds": "Breakfast"
}
```

**Response (200 OK):**
```json
{
    "bookingid": 42,
    "booking": {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": true,
        "bookingdates": {
        "checkin": "2025-12-15",
        "checkout": "2025-12-20"
        },
        "additionalneeds": "Breakfast"
    }
}
```

**Status Codes:**
- `200 OK` - Booking created successfully
- `400 Bad Request` - Invalid request format or missing required fields
- `500 Internal Server Error` - Server error

**Field Requirements:**
| Field | Type | Required | Validation |
|-------|------|----------|-----------|
| firstname | string | Yes | Non-empty |
| lastname | string | Yes | Non-empty |
| totalprice | integer | Yes | Positive number |
| depositpaid | boolean | No | true/false |
| bookingdates.check-in | string | Yes | Date format: YYYY-MM-DD |
| bookingdates.check-out | string | Yes | Date format: YYYY-MM-DD, >= check-in |
| additionalneeds | string | No | Optional |

**Example Request:**
curl -X POST https://restful-booker.herokuapp.com/booking
-H "Content-Type: application/json"
-d '{
    "firstname": "Jane",
    "lastname": "Smith",
    "totalprice": 200,
    "depositpaid": false,
    "bookingdates": {
    "checkin": "2025-12-25",
    "checkout": "2025-12-30"
    },
    "additionalneeds": "Lunch"
}'

**Notes:**
- No authentication required for creation
- Booking ID is auto-generated
- Accepts any firstname/lastname combination
- No validation on negative prices (allows negative values)

---

### PUT /booking/{id}

Update existing booking.

**Method:** `PUT`

**URL:** `/booking/{id}`

**Path Parameters:**
- `id` (required) - Integer booking ID

**Headers:**
**Content-Type:** application/json
**Accept:** application/json
**Cookie:** token=<auth_token>

**Authentication:** Required
- Must include valid authentication token from `/auth/`
- Token passed in Cookie header

**Request Body:**
{
    "firstname": "Jane",
    "lastname": "Doe",
    "totalprice": 200,
    "depositpaid": false,
    "bookingdates": {
    "checkin": "2025-12-18",
    "checkout": "2025-12-25"
    },
    "additionalneeds": "Lunch"
}

**Response (200 OK):**
{
    "firstname": "Jane",
    "lastname": "Doe",
    "totalprice": 200,
    "depositpaid": false,
    "bookingdates": {
    "checkin": "2025-12-18",
    "checkout": "2025-12-25"
    },
    "additionalneeds": "Lunch"
}

**Status Codes:**
- `200 OK` - Booking updated successfully
- `400 Bad Request` - Invalid request format
- `403 Forbidden` - Missing or invalid authentication token
- `404 Not Found` - Booking ID does not exist
- `500 Internal Server Error` - Server error

**Example:**
1. Get authentication token
TOKEN=$(curl -s -X POST https://restful-booker.herokuapp.com/auth/
-H "Content-Type: application/json"
-d '{
    "username": "admin", 
    "password": "password123"
    }'
| jq -r '.token')

2. Update booking with token
curl -X PUT https://restful-booker.herokuapp.com/booking/1
-H "Content-Type: application/json"
-H "Cookie: token=$TOKEN"
-d '{
    "firstname": "Updated",
    "lastname": "Name",
    "totalprice": 250,
    "depositpaid": true,
    "bookingdates": {
    "checkin": "2025-12-18",
    "checkout": "2025-12-25"
    },
    "additionalneeds": "Dinner"
}'

**Notes:**
- Authentication token required
- Can update partial or all fields
- Full booking object must be sent (no partial updates)
- Response includes updated booking details

---

### DELETE /booking/{id}

Delete existing booking.

**Method:** `DELETE`

**URL:** `/booking/{id}`

**Path Parameters:**
- `id` (required) - Integer booking ID

**Headers:**
**Accept:** application/json
**Cookie:** token=<auth_token>

**Authentication:** Required
- Must include valid authentication token

**Response (201 Created):**
Empty response in body

**Status Codes:**
- `201 Created` - Booking deleted successfully
- `400 Bad Request` - Invalid request
- `403 Forbidden` - Missing or invalid authentication token
- `404 Not Found` - Booking ID does not exist
- `500 Internal Server Error` - Server error

**Example:**
Delete booking with authentication
curl -X DELETE https://restful-booker.herokuapp.com/booking/1
-H "Cookie: token=f36513dc40faf7e"

**Notes:**
- Authentication token required
- Returns HTTP 201
- No response body on success
- Booking is permanently removed

---

## Common Response Codes

| Status | Meaning | Scenario |
|--------|---------|----------|
| 200 | OK | Successful GET, POST, PUT |
| 201 | Created | Successful DELETE |
| 400 | Bad Request | Invalid format, missing fields |
| 403 | Forbidden | Missing/invalid authentication |
| 404 | Not Found | Booking ID doesn't exist |
| 500 | Server Error | Unexpected server-side error |

---

## Authentication Flow

### Without Authentication (GET operations)
Client → GET `/booking`

Server → Returns list of all bookings

### With Authentication (POST/PUT/DELETE)
Client → POST `/auth/` (credentials)

Server → Returns authentication token

Client → PUT/DELETE `/booking/{id}` (with token in Cookie)

Server → Performs operation and returns response

---

## Data Types & Formats

### Date Format
- Format: `YYYY-MM-DD`
- Example: `2025-12-15`

### Integer Fields
- totalprice: Integer
- bookingid: Integer

### String Fields
- firstname, lastname: Non-empty strings
- additionalneeds: Optional string

### Boolean Fields
- depositpaid: true/false

---

## Common Use Cases

### Use Case 1: Create and Retrieve Booking
1. Create booking
POST `/booking`
```json
{
    "firstname": "John",
    "lastname": "Doe",
    ...
}
```

Response: 
```json
{
    "bookingid": 42, 
    ...
}
```

2. Retrieve booking
GET `/booking/42`

Response: 
```json
{
    "firstname": "John", 
    "lastname": "Doe", 
    ...
}
```

### Use Case 2: Update Booking with Authentication
1. Login
POST `/auth/`
```json
{
    "username": "admin",
    "password": "password123"
}
```

Response: 
```json
{
    "token": "f36513dc40faf7e"
}
```

2. Update booking
PUT `/booking/42`
Header: Cookie: token=f36513dc40faf7e
```json
{
    "firstname": "Jane",
    ...
}
```

### Use Case 3: Filter Bookings by Date
Get bookings between specific dates
GET `/booking?checkin=2025-12-15&checkout=2025-12-20`

Response: 
```json
[
    {
        "bookingid": 1
    },
    {
        "bookingid": 3
    }, 
    ...
]
```

---

## API Limitations & Notes

- No pagination implemented (returns all results)
- No search functionality beyond provided filters
- Negative prices are accepted (likely a bug)
- No rate limiting observed in demo
- No API versioning (single version)
- CORS enabled for browser requests
- Runs on public/shared database (data not private)

---

## Testing Strategy for API

### Path Tests
- Create booking with valid data 
- Retrieve all bookings 
- Retrieve specific booking 
- Update booking with valid data 
- Delete booking with authentication 

### Negative Tests
- Create booking with missing firstname 
- Create booking with invalid date range 
- Update without authentication 
- Delete without authentication 
- Update non-existent booking 

### Edge Cases
- Create booking with negative price 
- Create booking with special characters 
- Very long firstname/lastname 
- Update with partial data 

---

## Document Version History

| Version | Date | Author | Status |
|---------|------|--------|--------|
| 1.0 | 2025-11-19 | QA Team | Complete |
