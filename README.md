# SauceDemo E-Commerce QA Testing

## Project Overview

This project demonstrates manual and automated testing of the SauceDemo e-commerce demo application.

The goal is to validate important e-commerce workflows, including user authentication, product inventory, sorting, shopping cart operations, and checkout functionality.

## Application Under Test

- **Application:** [SauceDemo](https://www.saucedemo.com/)
- **Test Account:** `standard_user`
- **Testing Type:** Manual Testing and UI Automation

## Technology Stack

| Tool | Purpose |
|---|---|
| Python | Programming language |
| Selenium WebDriver | Browser automation |
| Pytest | Test framework |
| pytest-html | HTML test reporting |
| Google Chrome | Browser |
| Git & GitHub | Version control |

## Project Structure

```text
qa-ecommerce-testing/
├── config/
│   └── test_data.py
├── docs/
│   ├── test-plan.md
│   ├── test-scenarios.md
│   ├── test-cases.md
│   └── bug-reports.md
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Test Coverage

### Manual Testing

- Test planning and test scenarios
- Login and logout validation
- Product inventory verification
- Product sorting
- Add and remove cart items
- Checkout form validation
- Order summary calculations
- Order completion and navigation

**Manual test cases:** 16

**Latest manual execution:** 16 passed using `standard_user`.

### Automation Testing

| Module | Automated Tests |
|---|---:|
| Login | 3 |
| Inventory | 6 |
| Shopping Cart | 6 |
| Checkout | 7 |
| **Total** | **22** |

**Latest automation execution:** 22 passed, 0 failed.

## Design Pattern

This project uses the **Page Object Model (POM)** to separate page locators and browser interactions from test logic.

Reusable fixtures in `conftest.py` handle browser setup and login preparation.

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/milandahal1000/SauceDemo_QA_Testing_Project.git
cd qa-ecommerce-testing
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux with Fish shell:

```fish
source .venv/bin/activate.fish
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure Google Chrome is installed.

## Running Tests

Run the complete test suite:

```bash
pytest -v -s
```

Run individual test modules:

```bash
pytest -v -s tests/test_login.py
pytest -v -s tests/test_inventory.py
pytest -v -s tests/test_cart.py
pytest -v -s tests/test_checkout.py
```

## HTML Test Report

The project uses `pytest-html` to generate an HTML report automatically.

After execution, open:

```text
reports/automation-report.html
```

On Linux:

```bash
xdg-open reports/automation-report.html
```

Screenshots are captured when an automated test fails.

## Test Data

Test credentials and checkout information are maintained centrally in:

```text
config/test_data.py
```

The project uses SauceDemo's public demo credentials. Do not use real personal or payment information.

## Project Limitations

- Testing is performed against a publicly available demo application.
- No real payment transactions are performed.
- Results may vary if the demo application changes.
- Performance, load, and production security testing are outside this project's scope.

## Author

**QA Testing Portfolio Project**

Created to demonstrate practical skills in manual testing, Python automation, Selenium WebDriver, Pytest, and Page Object Model.
