
from playwright.sync_api import Page, expect
from config.config import Config
import logging

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = Config.BASE_URL
        self.timeout = Config.EXPLICIT_WAIT
    
    def navigate(self, url=''):
        full_url = self.base_url + url
        logger.info(f'Navigating to: {full_url}')
        self.page.goto(full_url)
    
    def click(self, selector):
        logger.info(f'Clicking element: {selector}')
        self.page.click(selector, timeout=self.timeout)
    
    def fill(self, selector, text):
        logger.info(f'Filling {selector} with: {text}')
        self.page.fill(selector, text, timeout=self.timeout)
    
    def get_text(self, selector):
        logger.info(f'Getting text from: {selector}')
        return self.page.text_content(selector, timeout=self.timeout)
    
    def is_visible(self, selector):
        try:
            return self.page.is_visible(selector, timeout=5000)
        except:
            return False
    
    def wait_for_element(self, selector):
        logger.info(f'Waiting for element: {selector}')
        self.page.wait_for_selector(selector, timeout=self.timeout)
    
    def wait_for_url(self, url_pattern):
        logger.info(f'Waiting for URL: {url_pattern}')
        self.page.wait_for_url(url_pattern, timeout=self.timeout)
    
    def take_screenshot(self, name):
        screenshot_path = Config.SCREENSHOT_DIR / f'{name}.png'
        logger.info(f'Taking screenshot: {screenshot_path}')
        self.page.screenshot(path=str(screenshot_path))
        return screenshot_path
    
    def get_current_url(self):
        return self.page.url
    
    def get_title(self):
        return self.page.title()
