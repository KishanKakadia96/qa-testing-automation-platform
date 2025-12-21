# GitHub Actions CI/CD Setup Guide

## Overview
This project includes automated CI/CD workflows using GitHub Actions for continuous testing.

## Workflows Created

### 1. **api-tests.yml**
- **Triggers:** Push/PR to main, test, develop branches + manual dispatch
- **Purpose:** Run all API automation tests
- **Output:** HTML test report as artifact

### 2. **ui-tests.yml**
- **Triggers:** Push/PR to main, test, develop branches + manual dispatch
- **Purpose:** Run UI tests on Chrome browser
- **Output:** HTML test reports and screenshots (on failure)
- **Jobs:** Runs Chrome tests in parallel

### 3. **complete-test-suite.yml**
- **Triggers:** Push/PR to main branch + daily schedule (midnight UTC) + manual dispatch
- **Purpose:** Run complete test suite (API + UI)
- **Output:** Comprehensive test summary with all reports
- **Jobs:** API tests → UI tests → Summary generation (sequential)

## Required GitHub Secrets

Before workflows can run successfully, add these secrets to your GitHub repository:

1. Go to: **Settings → Secrets and variables → Actions**
2. Add the following secrets:
   - `API_USERNAME`: Restful Booker API username (default: `admin`)
   - `API_PASSWORD`: Restful Booker API password (default: `password123`)

## How to Add Secrets
```
Repository → Settings → Secrets and variables → Actions → New repository secret
```

## Running Workflows

### Automatic Triggers:
- **On Push:** Workflows run automatically when you push to main/test/develop
- **On PR:** Workflows run when creating/updating pull requests
- **Scheduled:** Complete suite runs daily at midnight UTC

### Manual Triggers:
1. Go to: **Actions** tab in GitHub
2. Select the workflow you want to run
3. Click **Run workflow** button
4. Choose the branch
5. Click **Run workflow**

## Viewing Results

### Test Reports:
1. Go to **Actions** tab
2. Click on a workflow run
3. Scroll to **Artifacts** section
4. Download report files:
   - `api-test-report` (API test results)
   - `ui-test-report-chrome` (UI Chrome results)

### Test Summary:
- Available in the workflow run summary page
- Shows overall test execution status
- Links to artifacts for detailed reports

## Workflow Features

- **Parallel Execution:** UI tests run on multiple browsers simultaneously  
- **Artifact Upload:** Test reports saved for 30 days  
- **Screenshot Capture:** UI test failures save screenshots (7 days retention)  
- **Test Summary:** Markdown summary in workflow run page  
- **Dependency Caching:** Pip packages cached for faster runs  
- **JUnit XML:** Machine-readable test results for CI/CD integration  

## Troubleshooting

### Tests failing in CI but passing locally?
- Check environment differences (OS, browser versions)
- Verify secrets are properly configured
- Check if the Restful Booker API is accessible

### Workflow not triggering?
- Ensure YAML files are in `.github/workflows/` directory
- Check branch names match trigger conditions
- Verify GitHub Actions is enabled for the repository

### Artifacts not available?
- Artifacts are only kept for configured retention period
- Check if the job completed (artifacts upload even if tests fail)
