@"
import pytest
from playwright.sync_api import sync_playwright
from config.config import Config
import logging
from pathlib import Path
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create directories
Config.SCREENSHOT_DIR.mkdir(exist_ok=True)
Config.REPORT_DIR.mkdir(exist_ok=True)
Config.LOG_FILE.parent.mkdir(exist_ok=True)

@pytest.fixture(scope='session')
def browser_type_launch_args():
    return {
        'headless': Config.HEADLESS,
        'slow_mo': Config.SLOW_MO
    }

@pytest.fixture(scope='session')
def browser_context_args():
    return {
        'viewport': Config.get_viewport('desktop'),
        'ignore_https_errors': True
    }

@pytest.fixture(scope='function')
def page(playwright):
    browser = playwright.chromium.launch(
        headless=Config.HEADLESS,
        slow_mo=Config.SLOW_MO
    )
    context = browser.new_context(
        viewport=Config.get_viewport('desktop')
    )
    page = context.new_page()
    page.set_default_timeout(Config.EXPLICIT_WAIT)
    
    yield page
    
    # Cleanup
    page.close()
    context.close()
    browser.close()

@pytest.fixture(scope='function')
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope='function')
def mobile_page(playwright):
    browser = playwright.chromium.launch(headless=Config.HEADLESS)
    context = browser.new_context(
        viewport=Config.get_viewport('mobile'),
        user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)'
    )
    page = context.new_page()
    
    yield page
    
    page.close()
    context.close()
    browser.close()

@pytest.fixture(scope='function')
def tablet_page(playwright):
    browser = playwright.chromium.launch(headless=Config.HEADLESS)
    context = browser.new_context(
        viewport=Config.get_viewport('tablet')
    )
    page = context.new_page()
    
    yield page
    
    page.close()
    context.close()
    browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == 'call' and report.failed:
        if Config.SCREENSHOT_ON_FAILURE:
            page = item.funcargs.get('page')
            if page:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                screenshot_name = f'{item.name}_{timestamp}'
                screenshot_path = Config.SCREENSHOT_DIR / f'{screenshot_name}.png'
                page.screenshot(path=str(screenshot_path))
                logger.info(f'Screenshot saved: {screenshot_path}')

def pytest_configure(config):
    config.addinivalue_line(
        'markers', 'smoke: Quick smoke tests'
    )
    config.addinivalue_line(
        'markers', 'regression: Full regression suite'
    )
    config.addinivalue_line(
        'markers', 'responsive: Responsive design tests'
    )
"@ | Out-File -FilePath "tests\conftest.py" -Encoding UTF8