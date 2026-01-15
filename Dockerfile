@"
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install --with-deps chromium firefox webkit

# Copy application code
COPY . .

# Create directories
RUN mkdir -p reports screenshots logs

# Run tests
CMD ["pytest", "tests/", "-v"]
"@ | Out-File -FilePath "Dockerfile" -Encoding UTF8