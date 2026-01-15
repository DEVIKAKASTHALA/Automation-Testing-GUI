
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class FormPage(BasePage):
    # Locators
    FORM = 'form.main-form'
    NAME_INPUT = '#name'
    EMAIL_INPUT = '#email'
    PHONE_INPUT = '#phone'
    MESSAGE_TEXTAREA = '#message'
    SUBMIT_BUTTON = 'button[type=\"submit\"]'
    SUCCESS_MESSAGE = '.success-message'
    ERROR_MESSAGES = '.error-message'
    
    def __init__(self, page):
        super().__init__(page)
        self.url = '/contact'
    
    def navigate(self):
        super().navigate(self.url)
        logger.info('Navigated to form page')
    
    def fill_form(self, name='', email='', phone='', message=''):
        logger.info('Filling form')
        if name:
            self.fill(self.NAME_INPUT, name)
        if email:
            self.fill(self.EMAIL_INPUT, email)
        if phone:
            self.fill(self.PHONE_INPUT, phone)
        if message:
            self.fill(self.MESSAGE_TEXTAREA, message)
    
    def submit_form(self):
        logger.info('Submitting form')
        self.click(self.SUBMIT_BUTTON)
    
    def submit_empty_form(self):
        logger.info('Submitting empty form')
        self.submit_form()
    
    def has_validation_errors(self):
        return self.is_visible(self.ERROR_MESSAGES)
    
    def get_error_message(self, field=''):
        if field:
            selector = f'#{field} + .error-message'
        else:
            selector = self.ERROR_MESSAGES
        
        if self.is_visible(selector):
            return self.get_text(selector)
        return None
    
    def is_form_submitted_successfully(self):
        return self.is_visible(self.SUCCESS_MESSAGE)
    
    def get_success_message(self):
        if self.is_visible(self.SUCCESS_MESSAGE):
            return self.get_text(self.SUCCESS_MESSAGE)
        return None
