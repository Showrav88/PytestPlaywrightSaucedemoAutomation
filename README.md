# PytestPlaywrightSaucedemoAutomation
This repository contains a robust End-to-End (E2E) test automation suite for the Saucedemo web application. The suite is built using Python, the Pytest framework, and the Playwright library for reliable browser interaction.

The project follows the Page Object Model (POM) pattern for maintainability, utilizes Pytest fixtures for efficient data management, and covers critical user journeys, including full purchase validation and negative testing.

Prerequisites

To run these tests, you must have the following installed:

Python 3.8+
pytest 9.0.1
VS code
Git (for cloning the repository)

Setup Instructions (Running on a Local Machine)

Follow these steps to set up the project environment and execute the tests locally.

1. Clone the Repository

Open your terminal or command prompt and clone the project:
```bash
git clone https://github.com/Showrav88/PytestPlaywrightSaucedemoAutomation.git
```
# Create the virtual environment
```bash
python -m venv venv
```
# Activate the virtual environment
# On Windows:
```bash
.\venv\Scripts\activate
```
3. Install Dependencies

Once the virtual environment is active, install the required Python packages:
```bash
pip install -r requirements.txt

```
4. Install Browser Drivers

Playwright requires browser drivers to run the tests. Run this command to install Chromium, Firefox, and WebKit drivers:
```bash
playwright install
```
6. Run the Tests

Execute the E2E test suite using Pytest.

To run the main E2E test:
```bash
standard user:
pytest -s tests/test_standard_user_e2e.py
locked user :
pytest -s tests/test_locked_user_e2e.py
```




