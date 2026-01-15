
from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)

def wait_for_element_visible(page: Page, selector: str, timeout=30000):
    """Wait for element to be visible"""
    logger.info(f'Waiting for element to be visible: {selector}')
    page.wait_for_selector(selector, state='visible', timeout=timeout)

def wait_for_element_hidden(page: Page, selector: str, timeout=30000):
    """Wait for element to be hidden"""
    logger.info(f'Waiting for element to be hidden: {selector}')
    page.wait_for_selector(selector, state='hidden', timeout=timeout)

def wait_for_url_contains(page: Page, url_part: str, timeout=30000):
    """Wait for URL to contain specific string"""
    logger.info(f'Waiting for URL to contain: {url_part}')
    page.wait_for_url(f'**/*{url_part}*', timeout=timeout)

def wait_for_timeout(seconds: int):
    import time
    logger.info(f'Waiting for {seconds} seconds')
    time.sleep(seconds)