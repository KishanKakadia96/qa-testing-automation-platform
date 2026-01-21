# QA Testing Automation Platform

A comprehensive, enterprise-grade testing automation platform featuring API testing, UI testing, manual test cases, and complete documentation. This project demonstrates QA engineering practices including test automation frameworks, bug tracking, and CI/CD integration.
> **Note**: Some API tests may fail due to bugs identified in the original testing site. These failures are expected and documented in the bug report, demonstrating the platform's ability to detect real-world defects.

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-9.0.1-green.svg)](https://pytest.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.38.0-green.svg)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Test Reports](#test-reports)
- [Documentation](#documentation)
- [CI/CD Integration](#cicd-integration)
- [Bug Reports](#bug-reports)

---

## Overview

This platform provides a complete testing solution for the **Restful Booker API** and web application, including:

- **API Automation Testing**: Comprehensive test suite with 41+ test cases covering CRUD operations, security, validation, authentication, and edge cases
- **UI Automation Testing**: Selenium-based tests for web application functionality with cross-browser support
- **Manual Testing**: Documented test cases and scenarios for manual verification
- **Postman Collections**: Ready-to-use API collections for quick testing and validation
- **Professional Documentation**: Complete test strategy, scenarios, RTM, and bug reports

### Test Coverage
- **Total API Tests**: 41
- **Security Tests**: 10
- **Validation Tests**: 14
- **Authentication Tests**: 4
- **CRUD Operations**: 5
- **UI Tests**: 12+
- **Manual Test Cases**: 50+

---

## Features

### API Automation
-  Complete CRUD operations testing (Create, Read, Update, Delete)
-  Advanced security testing (SQL Injection, XSS, NoSQL, Command Injection, Path Traversal)
-  Comprehensive input validation testing
-  Authentication and authorization testing
-  Boundary and edge case testing
-  Error handling validation
-  Performance and response time testing
-  Data-driven testing with JSON test data
-  Detailed HTML reports with pytest-html

### UI Automation
-  Selenium WebDriver with Page Object Model (POM) design pattern
-  Cross-browser testing (Chrome, Firefox)
-  Headless mode support
-  Dynamic waits and element handling
-  Screenshot capture on failures
-  Data-driven UI tests
-  Form validation testing
-  Responsive design testing

### Documentation
-  Comprehensive Test Strategy document
-  Detailed Test Scenarios
-  Requirements Traceability Matrix (RTM)
-  Professional Bug Reports (27 defects identified)
-  API Endpoint documentation
-  Application Analysis document

### CI/CD Integration
-  Automated test execution scripts
-  Postman collection runner
-  Batch scripts for Windows environments
-  Ready for Jenkins/GitHub Actions integration

---

## 📁 Project Structure

```
qa-testing-automation-platform/
├── ci_cd/                              # CI/CD automation scripts
│   └── postman_runner.bat             # Postman collection runner
│
├── docs/                               # Comprehensive documentation
│   ├── API_Bug_Report.md              # 27 defects identified and documented
│   ├── API_Endpoints.md               # API documentation
│   ├── Application_Analysis.md        # Application analysis
│   ├── RTM.csv                        # Requirements Traceability Matrix
│   ├── Test_Scenarios.md              # Detailed test scenarios
│   └── Test_Strategy.md               # Test strategy document
│
├── postman/                           # Postman collections
│   ├── collections/                   # API test collections
│   ├── environments/                  # Environment configurations
│   └── globals/                       # Global variables
│
├── testing/                           # All test automation code
│   ├── api_automation/               # API test automation
│   │   ├── api_client/              # API client implementations
│   │   │   ├── auth_client.py       # Authentication API client
│   │   │   ├── base_client.py       # Base API client with common methods
│   │   │   └── booking_client.py    # Booking API client
│   │   ├── configs/                 # Configuration management
│   │   │   └── config.py            # Environment configuration
│   │   ├── data/                    # Test data files
│   │   │   └── bookings_test_data.json
│   │   ├── logs/                    # Test execution logs
│   │   ├── reports/                 # HTML test reports
│   │   └── tests/                   # Test cases
│   │       ├── conftest.py          # Pytest fixtures and setup
│   │       ├── test_authentication.py
│   │       ├── test_booking_list.py
│   │       ├── test_bookings_crud.py
│   │       ├── test_bookings_validation.py
│   │       ├── test_boundary_edge.py
│   │       ├── test_error_handling.py
│   │       ├── test_performance_misc.py
│   │       └── test_security.py
│   │
│   ├── ui_automation/               # UI test automation
│   │   ├── data/                   # UI test data
│   │   ├── drivers/                # WebDriver factory
│   │   │   └── driver_factory.py   # Browser driver initialization
│   │   ├── logs/                   # UI test logs
│   │   ├── pages/                  # Page Object Model
│   │   │   ├── base_page.py       # Base page with common methods
│   │   │   ├── booking_page.py    # Booking page objects
│   │   │   └── home_page.py       # Home page objects
│   │   ├── reports/               # UI test reports
│   │   │   └── screenshots/       # Failure screenshots
│   │   └── tests/                 # UI test cases
│   │       ├── conftest.py
│   │       ├── test_advanced_scenarios.py
│   │       ├── test_booking_ui.py
│   │       ├── test_cross_browser.py
│   │       ├── test_data_driven.py
│   │       ├── test_form_validation.py
│   │       └── test_setup_verification.py
│   │
│   ├── manual_test/                # Manual testing
│   │   └── TestCases.csv          # Manual test cases
│   │
│   └── postman/                   # Postman test collections
│       ├── collections/
│       ├── environments/
│       └── globals/
│
├── .env                           # Environment variables
├── requirements.txt              # Python dependencies
├── pytest.ini                   # Pytest configuration
└── README.md                   # This file
```

---

## Technology Stack

### Core Technologies
- **Python 3.12**: Primary programming language
- **Pytest 9.0.1**: Testing framework
- **Requests 2.32.5**: HTTP library for API testing
- **Selenium 4.38.0**: Browser automation
- **WebDriver Manager 4.0.1**: Automatic driver management

### Testing & Reporting
- **pytest-html 4.1.1**: HTML test reports
- **pytest-xdist 3.8.0**: Parallel test execution
- **allure-pytest 2.15.2**: Advanced reporting
- **Postman/Newman**: API testing and collection running

### Configuration & Utilities
- **python-dotenv 1.2.1**: Environment variable management
- **CSV/JSON**: Test data management

---

## Installation

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)
- Git
- Chrome/Firefox browser (for UI tests)
- Postman (optional, for manual API testing)

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/qa-testing-automation-platform.git
   cd qa-testing-automation-platform
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   # Windows
   python -m venv venv
   venv/Scripts/activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   
   > **Note**: Both testing websites (Restful Booker API and Automation in Testing) are publicly available and open for all to use for testing and automation practice purposes.

   Create a `.env` file in the project root:
   ```env
   # API Configuration
   BASE_URL=https://restful-booker.herokuapp.com
   AUTH_ENDPOINT=/auth
   BOOKING_ENDPOINT=/booking
   API_USERNAME=admin
   API_PASSWORD=password123

   # UI Configuration
   TEST_URL=https://automationintesting.online/
   BROWSER=chrome
   IMPLICIT_WAIT=10
   EXPLICIT_WAIT=20
   HEADLESS=false
   ```

---

## Configuration

### API Testing Configuration
Edit `testing/api_automation/configs/config.py` or use environment variables:
- `BASE_URL`: API base URL
- `AUTH_ENDPOINT`: Authentication endpoint
- `BOOKING_ENDPOINT`: Booking endpoint
- `USERNAME`: API username
- `PASSWORD`: API password

### UI Testing Configuration
Configure browser settings in `.env`:
- `BROWSER`: chrome, firefox
- `HEADLESS`: true/false for headless mode
- `IMPLICIT_WAIT`: Implicit wait timeout (seconds)
- `EXPLICIT_WAIT`: Explicit wait timeout (seconds)

---

## Running Tests

### API Automation Tests

**Run All API Tests:**
```bash
cd testing/api_automation
pytest tests/ -v --html=reports/test_report.html --self-contained-html
```

**Run Specific Test Categories:**
```bash
# Security tests only
pytest tests/test_security.py -v

# CRUD operations
pytest tests/test_bookings_crud.py -v

# Validation tests
pytest tests/test_bookings_validation.py -v

# Authentication tests
pytest tests/test_authentication.py -v
```

**Run Tests in Parallel:**
```bash
pytest tests/ -n 4 -v
```

**Run with Detailed Logging:**
```bash
pytest tests/ -v -s --log-cli-level=INFO
```

### UI Automation Tests

**Run All UI Tests:**
```bash
cd testing/ui_automation
pytest tests/ -v --html=reports/ui_test_report.html --self-contained-html
```

**Run Specific UI Tests:**
```bash
# Booking tests
pytest tests/test_booking_ui.py -v

# Form validation
pytest tests/test_form_validation.py -v

# Cross-browser tests
pytest tests/test_cross_browser.py -v
```

**Run in Headless Mode:**
```bash
# Set HEADLESS=true in .env, then:
pytest tests/ -v
```

### Postman Collection Tests

**Using Postman:**
1. Import collections from `postman/collections/`
2. Import environment from `postman/environments/`
3. Run collection in Postman

**Using Newman (CLI):**
```bash
newman run postman/collections/QA-Testing.postman_collection.json \
  -e postman/environments/QA-Testing.postman_environment.json \
  --reporters cli,html \
  --reporter-html-export reports/postman_report.html
```

---

## Test Reports

### HTML Reports
After test execution, reports are generated in:
- **API Reports**: `testing/api_automation/reports/`
- **UI Reports**: `testing/ui_automation/reports/`
- **Screenshots**: `testing/ui_automation/reports/screenshots/` (on failures)

### Viewing Reports
```bash
# Open the latest HTML report in browser
# Windows
start testing/api_automation/reports/test_report.html

# Mac
open testing/api_automation/reports/test_report.html
```

### Test Logs
Detailed logs are available in:
- `testing/api_automation/logs/`
- `testing/ui_automation/logs/`

---

## 📚 Documentation

Comprehensive documentation is available in the `docs/` folder:

1. **[Test_Strategy.md](docs/Test_Strategy.md)** - Complete test strategy and approach
2. **[Test_Scenarios.md](docs/Test_Scenarios.md)** - Detailed test scenarios and cases
3. **[API_Bug_Report.md](docs/API_Bug_Report.md)** - 27 identified defects with severity classification
4. **[API_Endpoints.md](docs/API_Endpoints.md)** - API endpoint documentation
5. **[Application_Analysis.md](docs/Application_Analysis.md)** - Application structure analysis
6. **[RTM.csv](docs/RTM.csv)** - Requirements Traceability Matrix

### Key Findings
The comprehensive testing identified **27 defects**:
- **6 Critical** security vulnerabilities (SQL Injection, XSS, NoSQL Injection)
- **14 High** priority validation issues
- **4 Medium** authentication flaws
- **3 Medium** functional bugs

---

## 🔄 CI/CD Integration

### Batch Scripts
Windows batch scripts are provided in `ci_cd/`:
```bash
# Run Postman collections
ci_cd\postman_runner.bat
```

### GitHub Actions

> **Note**: For production environments or private repositories, consider using GitHub Secrets instead of hardcoded values.

A complete test suite workflow is available at `.github/workflows/complete-test-suite.yml` that runs both API and UI tests.

**Configuration:**

Environment variables are configured using GitHub repository variables (`${{ vars.VARIABLE_NAME }}`) at the job level in the workflow file. For production environments, consider using GitHub Secrets for sensitive data.

## Bug Reports

### Identified Issues
The testing platform identified **27 defects** across multiple categories:

#### Critical Security Issues (6)
- SQL Injection vulnerabilities
- XSS (Cross-Site Scripting) attacks
- NoSQL injection flaws
- Command injection vulnerabilities
- Path traversal issues

#### High Priority Validation Issues (14)
- Negative/zero price acceptance
- Invalid date format handling
- Empty required fields
- Special character validation
- Maximum length violations
- Null value acceptance
- Unicode character handling

#### Medium Priority Issues (7)
- Authentication token management
- Rate limiting gaps
- API response inconsistencies
- Search functionality missing

**Full details**: [API_Bug_Report.md](docs/API_Bug_Report.md)

---

## 👤 Author

**Kishan**
