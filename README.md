# Mobile Automation Wikipedia (Python + Appium)

This project is a robust test automation framework for the Wikipedia Android mobile application.

## Tech Stack
* **Language**: Python
* **Test Framework**: Pytest
* **Driver**: Appium (UIAutomator2)
* **Reporting**: Allure Reports
* **Design Pattern**: Page Object Model (POM)

## Key Features
* **Automatic Onboarding Skip**: Seamlessly handles initial welcome screens.
* **Search Scenarios**: Includes both positive (successful search) and negative (no results) test cases.
* **Screenshots on Failure**: The framework automatically captures and attaches a mobile screen screenshot to the Allure report if a test fails.

## Getting Started

### 1. Prerequisites
* Python 3.12+ installed.
* Appium Server running.
* Android Emulator or real device connected.

### 2. Installation
Clone the repository and install the required dependencies:
```bash
pip install -r requirements.txt