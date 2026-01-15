# Architecture Documentation

## Overview

This test automation framework follows the Page Object Model (POM) design pattern for maintainability and reusability.

## Directory Structure

### \`config/\`

Contains configuration files and settings.

### \`pages/\`

Page Object Model classes representing application pages.

### \`tests/\`

Test suites organized by type (e2e, integration, unit).

### \`utils/\`

Utility functions and helpers.

## Design Patterns

### Page Object Model

- Each page is represented by a class
- Locators are defined as class attributes
- Actions are methods on the page class
- Promotes reusability and maintainability

### Test Fixtures

- Pytest fixtures manage browser lifecycle
- Session and function-scoped fixtures
- Automatic cleanup after tests

## Technology Stack

- **Playwright**: Modern browser automation
- **Pytest**: Test framework and runner
- **Python**: Programming language
