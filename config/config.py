
import os
from dotenv import load_dotenv
import json
from pathlib import Path

load_dotenv()

class Config:
    # Base Configuration
    BASE_URL = os.getenv('BASE_URL', 'https://example.com')
    HEADLESS = os.getenv('HEADLESS', 'true').lower() == 'true'
    BROWSER = os.getenv('BROWSER', 'chromium')
    SLOW_MO = int(os.getenv('SLOW_MO', 0))
    
    # Timeouts (milliseconds)
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', 10)) * 1000
    EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', 30)) * 1000
    PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', 60)) * 1000
    
    # Screenshots
    SCREENSHOT_ON_FAILURE = os.getenv('SCREENSHOT_ON_FAILURE', 'true').lower() == 'true'
    SCREENSHOT_DIR = Path(os.getenv('SCREENSHOT_DIR', 'screenshots'))
    
    # Selenium
    SELENIUM_HUB_URL = os.getenv('SELENIUM_HUB_URL', 'http://localhost:4444')
    
    # Test Configuration
    PARALLEL_WORKERS = int(os.getenv('PARALLEL_WORKERS', 4))
    RERUN_FAILURES = int(os.getenv('RERUN_FAILURES', 2))
    
    # Reporting
    REPORT_DIR = Path(os.getenv('REPORT_DIR', 'reports'))
    ALLURE_RESULTS_DIR = Path(os.getenv('ALLURE_RESULTS_DIR', 'reports/allure-results'))
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = Path(os.getenv('LOG_FILE', 'logs/test.log'))
    
    @classmethod
    def get_viewport(cls, device='desktop'):
        viewports = {
            'mobile': {'width': 375, 'height': 667},
            'tablet': {'width': 768, 'height': 1024},
            'desktop': {'width': 1920, 'height': 1080},
            'iphone_se': {'width': 375, 'height': 667},
            'iphone_13': {'width': 390, 'height': 844},
            'ipad': {'width': 768, 'height': 1024},
            'ipad_pro': {'width': 1024, 'height': 1366}
        }
        return viewports.get(device, viewports['desktop'])
    
    @classmethod
    def load_browser_config(cls):
        config_path = Path(__file__).parent / 'browsers.json'
        with open(config_path, 'r') as f:
            return json.load(f)
