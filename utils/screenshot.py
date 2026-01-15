
from pathlib import Path
from datetime import datetime
from config.config import Config
import logging

logger = logging.getLogger(__name__)

def capture_screenshot(page, name='screenshot'):
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'{name}_{timestamp}.png'
    filepath = Config.SCREENSHOT_DIR / filename
    
    logger.info(f'Capturing screenshot: {filepath}')
    page.screenshot(path=str(filepath), full_page=True)
    
    return filepath

def capture_element_screenshot(page, selector, name='element'):
   
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'{name}_{timestamp}.png'
    filepath = Config.SCREENSHOT_DIR / filename
    
    element = page.query_selector(selector)
    if element:
        logger.info(f'Capturing element screenshot: {filepath}')
        element.screenshot(path=str(filepath))
        return filepath
    return None