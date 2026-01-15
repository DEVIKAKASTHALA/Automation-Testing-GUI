
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class DashboardPage(BasePage):
    # Locators
    DASHBOARD_TITLE = 'h1.dashboard-title'
    STATS_WIDGET = '.stats-widget'
    NAVIGATION_MENU = '.nav-menu'
    MOBILE_MENU_BUTTON = '.mobile-menu-toggle'
    USER_PROFILE = '.user-profile'
    NOTIFICATION_ICON = '.notification-icon'
    SEARCH_BAR = '#search'
    
    def __init__(self, page):
        super().__init__(page)
        self.url = '/dashboard'
    
    def navigate(self):
        super().navigate(self.url)
        logger.info('Navigated to dashboard')
    
    def get_dashboard_title(self):
        return self.get_text(self.DASHBOARD_TITLE)
    
    def is_dashboard_loaded(self):
        return self.is_visible(self.DASHBOARD_TITLE) and \
               self.is_visible(self.STATS_WIDGET)
    
    def open_mobile_menu(self):
        logger.info('Opening mobile menu')
        self.click(self.MOBILE_MENU_BUTTON)
    
    def search(self, query):
        logger.info(f'Searching for: {query}')
        self.fill(self.SEARCH_BAR, query)
        self.page.keyboard.press('Enter')
    
    def click_profile(self):
        logger.info('Clicking user profile')
        self.click(self.USER_PROFILE)
    
    def get_notification_count(self):
        badge = self.page.query_selector('.notification-badge')
        if badge:
            return int(badge.text_content())
        return 0
