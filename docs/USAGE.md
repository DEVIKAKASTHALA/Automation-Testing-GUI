# Usage Guide

## Running Tests

### All Tests

\`\`\`bash
pytest tests/
\`\`\`

### Specific Suite

\`\`\`bash
pytest tests/e2e/
pytest tests/integration/
\`\`\`

### With Markers

\`\`\`bash
pytest -m smoke
pytest -m regression
pytest -m responsive
\`\`\`

### Parallel Execution

\`\`\`bash
pytest -n 4
\`\`\`

## Configuration

### Environment Variables

Set in \`.env\` file:

- BASE_URL
- HEADLESS
- BROWSER

### Viewports

Configure in \`config/config.py\`

## Reporting

### HTML Report

\`\`\`bash
pytest --html=reports/report.html
\`\`\`

### Allure Report

\`\`\`bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
