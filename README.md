# DevOps Activity: Advanced GitHub Actions for a Flask Application

## Overview
This project implements a minimal Flask API and integrates advanced GitHub Actions workflows for CI, linting, code coverage, security scanning, and dependency management.

## Endpoints Implemented

**GET /hello**  
- Returns a simple JSON message: `{"message": "Hello, World!"}`

**POST /echo**
- Accepts JSON payload and returns the same payload with status code 201

**POST /student**  
- Accepts JSON payload with student information (e.g., `{"name": "Alice", "major": "CS"}`) and creates a new student in-memory. Returns the created student with an auto-generated ID and status code 201.

**PUT /student/<student_id>**  
- Accepts JSON payload to update an existing student. Returns the updated student data with status code 200.

**DELETE /student/<student_id>**  
- Deletes the student with the specified ID. Returns a confirmation message and status code 200.

## Tests
`test_app.py` contains unit tests for all endpoints using `pytest`.  
Run locally with:

```bash
pytest -q
```
## Issues Encountered

1. Codecov upload initially failed
 - Fixed by upgrading to codecov-action@v3 and ensuring the GitHub repo was recognized by Codecov.
