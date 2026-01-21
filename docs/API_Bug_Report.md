# API Bug Report - QA Testing Automation Platform

**Generated Date:** January 13, 2026  
**Platform Under Test:** Restful Booker API  
**Total Defects Found:** 27  
**Test Framework:** Pytest with API Automation Suite  

---

## Executive Summary

The automated test suite executed 41 API tests and identified **27 critical defects** across security, validation, authentication, and functional areas. These findings demonstrate significant gaps in input validation, security controls, and API functionality.

### Defect Distribution by Severity

| Severity | Count | Category |
|----------|-------|----------|
| Critical | 6 | Security Vulnerabilities |
| High | 14 | Missing Input Validation |
| Medium | 4 | Authentication Flaws |
| Medium | 3 | Functional Bugs |

---

## CRITICAL - Security Vulnerabilities (6 Defects)

### BUG-SEC-001: SQL Injection Not Blocked
- **Test:** `test_sql_injection`
- **Severity:** Critical
- **Status:** Failed
- **Description:** API accepts SQL injection payloads without sanitization
- **Payload:** `"'; DROP TABLE bookings; --"`
- **Expected:** HTTP 400 Bad Request with validation error
- **Actual:** HTTP 200 OK - Payload accepted
- **Impact:** Database compromise, data loss, unauthorized access
- **Security Risk:** Injection

### BUG-SEC-002: XSS Script Injection Accepted in firstname
- **Test:** `test_xss_injection`
- **Severity:** Critical
- **Status:** Failed
- **Description:** XSS payload accepted in firstname field
- **Payload:** `<script>alert('XSS')</script>`
- **Expected:** HTTP 400 with sanitization
- **Actual:** HTTP 200 - Script stored in database
- **Impact:** Cross-site scripting attacks, session hijacking
- **Security Risk:** Injection

### BUG-SEC-003: XSS Script Injection Accepted in lastname
- **Test:** `test_xss_injection`
- **Severity:** Critical
- **Status:**  Failed
- **Description:** XSS payload accepted in lastname field
- **Payload:** `<img src=x onerror=alert('XSS')>`
- **Expected:** HTTP 400 with sanitization
- **Actual:** HTTP 200 - Script stored in database
- **Impact:** Cross-site scripting attacks, credential theft
- **Security Risk:**  Injection

### BUG-SEC-004: NoSQL Injection Not Validated
- **Test:** `test_nosql_injection`
- **Severity:** Critical
- **Status:**  Failed
- **Description:** NoSQL injection operators accepted
- **Payload:** `{"$ne": null}` in request body
- **Expected:** HTTP 400 Bad Request
- **Actual:** HTTP 200 OK - Payload accepted
- **Impact:** Database query manipulation, unauthorized data access
- **Security Risk:**  Injection

### BUG-SEC-005: Command Injection Not Blocked
- **Test:** `test_command_injection`
- **Severity:** Critical
- **Status:**  Failed
- **Description:** OS command injection payload accepted
- **Payload:** `; ls -la` in booking fields
- **Expected:** HTTP 400 with validation error
- **Actual:** HTTP 200 - Command payload stored
- **Impact:** Remote code execution, server compromise
- **Security Risk:**  Injection

### BUG-SEC-006: Path Traversal Not Validated
- **Test:** `test_path_traversal`
- **Severity:** Critical
- **Status:**  Failed
- **Description:** Path traversal payload accepted
- **Payload:** `../../etc/passwd` in booking fields
- **Expected:** HTTP 400 Bad Request
- **Actual:** HTTP 200 - Payload accepted
- **Impact:** Unauthorized file access, information disclosure
- **Security Risk:** Broken Access Control

---
## HIGH - Missing Input Validation (14 Defects)

### BUG-VAL-001: Negative Price Accepted
- **Test:** `test_negative_price`
- **Severity:** High
- **Status:** Failed
- **Description:** API accepts negative values for totalprice field
- **Payload:** `{"totalprice": -1000}`
- **Expected:** HTTP 400 with validation error message
- **Actual:** HTTP 200 - Booking created with negative price
- **Impact:** Financial data integrity
- **Business Logic Violation:** Prices cannot be negative in real-world scenarios

### BUG-VAL-002: Zero Price Accepted
- **Test:** `test_zero_price`
- **Severity:** High
- **Status:** Failed
- **Description:** API allows totalprice of 0
- **Payload:** `{"totalprice": 0}`
- **Expected:** HTTP 400 Bad Request
- **Actual:** HTTP 200 - Booking created with 0 price
- **Impact:** Free bookings created
- **Business Logic Violation:** Zero-price bookings should be flagged or rejected

### BUG-VAL-003: Extremely Large Price Accepted
- **Test:** `test_large_price`
- **Severity:** High
- **Status:** Failed
- **Description:** API accepts unrealistically large price values
- **Payload:** `{"totalprice": 999999999}`
- **Expected:** HTTP 400 with maximum value validation
- **Actual:** HTTP 200 - Booking created with extreme value
- **Impact:** calculation errors, system instability
- **Risk:** Potential integer or buffer overflow vulnerabilities

### BUG-VAL-004: Invalid Date Format Accepted
- **Test:** `test_invalid_date_formats`
- **Severity:** High
- **Status:** Failed
- **Description:** Invalid date strings accepted in checkin/checkout fields
- **Payload:** `{"checkin": "2024-13-45"}`
- **Expected:** HTTP 400 with date validation error
- **Actual:** HTTP 200 - Invalid date stored
- **Impact:** Data corruption, reporting issues, business logic failures
- **Data Integrity:** Invalid dates cannot be processed correctly

### BUG-VAL-005: Future Checkout Before Checkin Accepted
- **Test:** `test_checkout_before_checkin`
- **Severity:** High
- **Status:** Failed
- **Description:** Checkout date before checkin date is accepted
- **Payload:** `{"checkin": "2025-12-31", "checkout": "2025-01-01"}`
- **Expected:** HTTP 400 - Logical date validation error
- **Actual:** HTTP 200 - Booking created with invalid date range
- **Impact:** Invalid reservations, booking conflicts, business logic errors
- **Business Rule Violation:** Checkout must be after checkin

### BUG-VAL-006: Empty String Firstname Accepted
- **Test:** `test_empty_required_fields`
- **Severity:** High
- **Status:** Failed
- **Description:** Empty string allowed in firstname field
- **Payload:** `{"firstname": ""}`
- **Expected:** HTTP 400 - Required field validation
- **Actual:** HTTP 200 - Booking created with empty name
- **Impact:** Data quality issues, customer identification problems
- **Data Integrity:** Required fields should not be empty

### BUG-VAL-007: Empty String Lastname Accepted
- **Test:** `test_empty_required_fields`
- **Severity:** High
- **Status:** Failed
- **Description:** Empty string allowed in lastname field
- **Payload:** `{"lastname": ""}`
- **Expected:** HTTP 400 - Required field validation
- **Actual:** HTTP 200 - Booking created with empty name
- **Impact:** Data quality issues, incomplete customer records
- **Data Integrity:** Required fields should not be empty

### BUG-VAL-008: Special Characters Not Validated in firstname
- **Test:** `test_special_characters_in_names`
- **Severity:** High
- **Status:** Failed
- **Description:** Arbitrary special characters accepted in firstname
- **Payload:** `{"firstname": "!@#$%^&*()"}`
- **Expected:** HTTP 400 - Character validation error
- **Actual:** HTTP 200 - Special characters stored
- **Impact:** Data quality, display issues, potential encoding problems
- **Validation Gap:** Names should contain only valid characters

### BUG-VAL-009: Special Characters Not Validated in lastname
- **Test:** `test_special_characters_in_names`
- **Severity:** High
- **Status:** Failed
- **Description:** Arbitrary special characters accepted in lastname
- **Payload:** `{"lastname": "!@#$%^&*()"}`
- **Expected:** HTTP 400 - Character validation error
- **Actual:** HTTP 200 - Special characters stored
- **Impact:** Data quality, reporting issues, search functionality degradation
- **Validation Gap:** Names should contain only valid characters

### BUG-VAL-010: Excessively Long String Accepted in firstname
- **Test:** `test_max_length_validation`
- **Severity:** High
- **Status:** Failed
- **Description:** No maximum length validation on firstname field
- **Payload:** 10,000 character string in firstname
- **Expected:** HTTP 400 - Maximum length exceeded
- **Actual:** HTTP 200 - Extremely long string stored
- **Impact:** Database bloat, performance degradation, buffer overflow risk
- **Security Risk:** Potential resource exhaustion

### BUG-VAL-011: Excessively Long String Accepted in lastname
- **Test:** `test_max_length_validation`
- **Severity:** High
- **Status:** Failed
- **Description:** No maximum length validation on lastname field
- **Payload:** 10,000 character string in lastname
- **Expected:** HTTP 400 - Maximum length exceeded
- **Actual:** HTTP 200 - Extremely long string stored
- **Impact:** Database bloat, performance issues, memory consumption
- **Security Risk:** Potential resource exhaustion

### BUG-VAL-012: Null Value Accepted in firstname
- **Test:** `test_null_values`
- **Severity:** High
- **Status:** Failed
- **Description:** Null value allowed in required firstname field
- **Payload:** `{"firstname": null}`
- **Expected:** HTTP 400 - Required field error
- **Actual:** HTTP 200 - Booking created with null firstname
- **Impact:** Data integrity violations, application errors
- **Data Quality:** Required fields cannot be null

### BUG-VAL-013: Null Value Accepted in lastname
- **Test:** `test_null_values`
- **Severity:** High
- **Status:** Failed
- **Description:** Null value allowed in required lastname field
- **Payload:** `{"lastname": null}`
- **Expected:** HTTP 400 - Required field error
- **Actual:** HTTP 200 - Booking created with null lastname
- **Impact:** Data integrity violations, customer record corruption
- **Data Quality:** Required fields cannot be null

### BUG-VAL-014: Unicode Characters Not Properly Handled
- **Test:** `test_unicode_handling`
- **Severity:** High
- **Status:** Failed
- **Description:** Unicode characters cause encoding issues
- **Payload:** `{"firstname": "田中", "lastname": "Müller"}`
- **Expected:** HTTP 200 with proper encoding
- **Actual:** Characters corrupted or improperly stored
- **Impact:** Internationalization failures, data corruption for non-ASCII names
- **Accessibility:** System should support international characters

---

## MEDIUM - Authentication Flaws (4 Defects)

### BUG-AUTH-001: Weak Token Expiration
- **Test:** `test_token_expiration`
- **Severity:** Medium
- **Status:** Failed
- **Description:** Authentication tokens do not expire
- **Expected:** Tokens should expire after reasonable time period
- **Actual:** Tokens remain valid indefinitely
- **Impact:** unauthorized access if token is compromised
- **Security Risk:** Security Misconfiguration

### BUG-AUTH-002: Missing Rate Limiting on Authentication Endpoint
- **Test:** `test_auth_rate_limiting`
- **Severity:** Medium
- **Status:** Failed
- **Description:** No rate limiting on /auth endpoint allows attacks
- **Expected:** HTTP 429 after multiple failed attempts
- **Actual:** Unlimited authentication attempts allowed
- **Impact:** credential stuffing
- **Security Risk:** Broken Authentication

### BUG-AUTH-003: Invalid Credentials Error Message Too Verbose
- **Test:** `test_invalid_credentials`
- **Severity:** Medium
- **Status:** Failed
- **Description:** Error messages reveal whether username or password is incorrect
- **Expected:** Generic "Invalid credentials" message
- **Actual:** "Username not found" or "Incorrect password"
- **Impact:** Username enumeration, helps attackers in credential attacks
- **Security Risk:** Information Disclosure

### BUG-AUTH-004: Token Not Validated on Protected Endpoints
- **Test:** `test_token_validation`
- **Severity:** Medium
- **Status:** Failed
- **Description:** Some protected endpoints accept malformed or invalid tokens
- **Expected:** HTTP 401 for invalid tokens
- **Actual:** HTTP 200 - Operations succeed with invalid tokens
- **Impact:** Unauthorized access, bypass of authentication controls
- **Security Risk:** Broken Authentication

---

## MEDIUM - Functional Bugs (3 Defects)

### BUG-FUNC-001: Booking ID Not Returned in POST Response
- **Test:** `test_create_booking`
- **Severity:** Medium
- **Status:** Failed
- **Description:** POST /booking does not consistently return bookingid
- **Expected:** Response includes bookingid in standard format
- **Actual:** Inconsistent response structure
- **Impact:** Client applications cannot retrieve created booking ID
- **API Design:** Response format should be consistent

### BUG-FUNC-002: DELETE Request Does Not Return Proper Status
- **Test:** `test_delete_booking`
- **Severity:** Medium
- **Status:** Failed
- **Description:** DELETE endpoint returns incorrect status codes
- **Expected:** HTTP 200 or 204 on successful deletion
- **Actual:** HTTP 201 returned
- **Impact:** Misleading response codes
- **REST Compliance:** DELETE should not return 201 Created

### BUG-FUNC-003: Search/Filter Functionality Not Implemented
- **Test:** `test_search_bookings`
- **Severity:** Medium
- **Status:** Failed
- **Description:** GET /booking does not support query parameters for filtering
- **Payload:** `GET /booking?firstname=John&lastname=Doe`
- **Expected:** Filtered list of matching bookings
- **Actual:** HTTP 200 but all bookings returned (no filtering applied)
- **Impact:** Performance issues, inability to search specific bookings
- **Functionality Gap:** Missing critical search feature

---

## Priority

**Priority 1**: Address all critical security vulnerabilities (BUG-SEC-001 through BUG-SEC-006)  
**Priority 2**: Implement comprehensive input validation (BUG-VAL-001 through BUG-VAL-014)  
**Priority 3**: Fix authentication flaws (BUG-AUTH-001 through BUG-AUTH-004)  
**Priority 4**: Resolve functional inconsistencies (BUG-FUNC-001 through BUG-FUNC-003)

---