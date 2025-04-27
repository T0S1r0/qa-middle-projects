# Selenium Automated Tests

This repository contains a set of automated tests written in Python using the Selenium WebDriver for web application testing.

## Features
- Registration form testing
- Search functionality testing
- Add to cart functionality testing
- User login testing
- Contact form submission testing

## Prerequisites
- Python 3.13 (latest version)
- Chrome WebDriver

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/T0S1r0/selenium_tests.git
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

## Running the Tests

1. To run the tests, use the following command:
    ```
    python -m unittest discover tests
    ```

2. Alternatively, you can run each test separately:
    ```
    python tests/test_registration.py
    python tests/test_search.py
    python tests/test_add_to_cart.py
    python tests/test_login.py
    python tests/test_contact_form.py
    ```

## License
MIT
