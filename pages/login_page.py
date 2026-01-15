
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    # Locators
    EMAIL_INPUT = '#email'
    PASSWORD_INPUT = '#password'
    LOGIN_BUTTON = 'button[type=\"submit\"]'
    ERROR_MESSAGE = '.error-message'
    LOGOUT_BUTTON = '#logout'
    USER_MENU = '.user-menu'
    
    def __init__(self, page):
        super().__init__(page)
        self.url = '/login'
    
    def navigate(self):
        super().navigate(self.url)
        logger.info('Navigated to login page')
    
    def login(self, email, password):
        logger.info(f'Logging in with email: {email}')
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def is_logged_in(self):
        try:
            return self.is_visible(self.USER_MENU) or '/dashboard' in self.get_current_url()
        except:
            return False
    
    def get_error_message(self):
        if self.is_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return None
    
    def logout(self):
        logger.info('Logging out')
        self.click(self.USER_MENU)
        self.click(self.LOGOUT_BUTTON)
