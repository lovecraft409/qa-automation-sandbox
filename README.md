# QA Automation Sandbox

A hands-on QA automation project covering **UI testing** and **API testing** in Python, with tests running automatically in **GitHub Actions** and packaged in **Docker**.

Built to practice the full loop a QA automation engineer works in: write tests, structure them cleanly, run them in CI, and run them anywhere in a container.

## Tech Stack

| Area | Tools |
|---|---|
| Language | Python |
| Test framework | pytest |
| UI automation | Playwright (pytest-playwright) |
| API testing | requests |
| CI | GitHub Actions |
| Containers | Docker |

## What's Covered

### UI tests: `swag_labs_ui/`
Tests against the [SauceDemo](https://www.saucedemo.com) practice site, built with the **Page Object Model (POM)**.

- Login tests (valid and invalid credentials)
- Inventory sorting tests
- End-to-end checkout flow

### API tests: `reqres-api/`
Tests against the [ReqRes](https://reqres.in) public API using `requests`.

- Users: fetch and validate responses
- Login: success and failure cases
- Update: update a user and check the response
- Delete: delete a user and verify the status code

Shared setup (base URL, session, fixtures) lives in `reqres-api/conftest.py`.

## Project Structure

```
qa-automation-sandbox/
├── .github/workflows/     # CI pipeline (runs tests on every push)
├── reqres-api/            # API tests
│   ├── conftest.py
│   ├── test_reqres_users_api.py
│   ├── test_reqres_login.py
│   ├── test_reqres_update_api.py
│   └── test_reqres_delete_api.py
├── swag_labs_ui/          # UI tests (Playwright + POM)
├── Dockerfile
├── requirements.txt
└── README.md
```

## Concepts Practiced

- Page Object Model for maintainable UI tests
- pytest fixtures and `conftest.py` for shared setup
- Assertions on status codes, response bodies, and page state
- Positive and negative test cases
- End-to-end test design
- Continuous integration with GitHub Actions
- Containerizing a test suite with Docker

## Getting Started

### 1. Clone and install

```bash
git clone https://github.com/lovecraft409/qa-automation-sandbox.git
cd qa-automation-sandbox

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
playwright install
```

### 2. Run the tests

Run everything:

```bash
pytest
```

Run one suite:

```bash
pytest reqres-api
pytest swag_labs_ui
```

Run with a visible browser (UI tests):

```bash
pytest swag_labs_ui --headed
```

### 3. Run in Docker

```bash
docker build -t qa-automation-sandbox .
docker run --rm qa-automation-sandbox
```

## Continuous Integration

A GitHub Actions workflow in `.github/workflows/` installs dependencies and runs the test suite on every push, so a broken change is caught right away.

## Author

**lovecraft409**. Learning QA automation with a focus on Python, CI/CD, and containers.
