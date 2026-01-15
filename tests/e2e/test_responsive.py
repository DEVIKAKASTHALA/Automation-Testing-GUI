
import pytest
from pages.dashboard_page import DashboardPage
from config.config import Config

@pytest.mark.responsive
@pytest.mark.parametrize('viewport', [
    {'width': 375, 'height': 667, 'device': 'mobile'},
    {'width': 768, 'height': 1024, 'device': 'tablet'},
    {'width': 1920, 'height': 1080, 'device': 'desktop'}
])
def test_responsive_navigation_menu(playwright, viewport):
  
    browser = playwright.chromium.launch(headless=Config.HEADLESS)
    context = browser.new_context(viewport=viewport)
    page = context.new_page()
    
    dashboard_page = DashboardPage(page)
    dashboard_page.navigate()
    
    if viewport['width'] < 768:
        # Mobile: hamburger menu should be visible
        assert dashboard_page.is_visible(dashboard_page.MOBILE_MENU_BUTTON)
    else:
        # Desktop: full navigation should be visible
        assert dashboard_page.is_visible(dashboard_page.NAVIGATION_MENU)
    
    page.close()
    context.close()
    browser.close()

@pytest.mark.responsive
def test_mobile_menu_toggle(mobile_page):
 
    dashboard_page = DashboardPage(mobile_page)
    dashboard_page.navigate()
    
    # Menu should be hidden initially
    assert dashboard_page.is_visible(dashboard_page.MOBILE_MENU_BUTTON)
    
    # Open mobile menu
    dashboard_page.open_mobile_menu()
    
    # Menu items should now be visible
    assert dashboard_page.is_visible(dashboard_page.NAVIGATION_MENU)

@pytest.mark.responsive
def test_desktop_layout_elements(page):
  
    page.set_viewport_size(Config.get_viewport('desktop'))
    dashboard_page = DashboardPage(page)
    dashboard_page.navigate()
    
    assert dashboard_page.is_visible(dashboard_page.NAVIGATION_MENU)
    assert dashboard_page.is_visible(dashboard_page.STATS_WIDGET)
    assert dashboard_page.is_visible(dashboard_page.USER_PROFILE)

@pytest.mark.responsive
def test_tablet_layout(tablet_page):
  
    dashboard_page = DashboardPage(tablet_page)
    dashboard_page.navigate()
    
    assert dashboard_page.is_dashboard_loaded()
    # Tablet might show mobile or desktop menu depending on design
    assert dashboard_page.is_visible(dashboard_page.NAVIGATION_MENU) or \
           dashboard_page.is_visible(dashboard_page.MOBILE_MENU_BUTTON)
