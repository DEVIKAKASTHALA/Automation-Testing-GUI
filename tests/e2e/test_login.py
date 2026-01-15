import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.smoke
@pytest.mark.e2e
def test_login_with_valid_credentials(page):
    """Test successful login with valid credentials"""
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.login('test@example.com', 'password123')
    
    assert login_page.is_logged_in()
    assert 'dashboard' in login_page.get_current_url()

@pytest.mark.e2e
def test_login_with_invalid_credentials(page):
    """Test login fails with invalid credentials"""
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.login('invalid@example.com', 'wrongpassword')
    
    assert not login_page.is_logged_in()
    error_msg = login_page.get_error_message()
    assert error_msg is not None
    assert 'invalid' in error_msg.lower() or 'incorrect' in error_msg.lower()

@pytest.mark.e2e
def test_login_with_empty_fields(page):
    """Test login validation with empty fields"""
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.login('', '')
    
    assert not login_page.is_logged_in()
    assert login_page.get_error_message() is not None

@pytest.mark.e2e
def test_logout_functionality(page):
    """Test user can logout successfully"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login('test@example.com', 'password123')
    
    assert login_page.is_logged_in()
    
    login_page.logout()
    
    assert not login_page.is_logged_in()
    assert 'login' in login_page.get_current_url()

@pytest.mark.smoke
@pytest.mark.e2e
def test_login_redirects_to_dashboard(page):
    """Test login redirects to dashboard"""
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    login_page.navigate()
    login_page.login('test@example.com', 'password123')
    
    assert dashboard_page.is_dashboard_loaded()
    assert 'Dashboard' in dashboard_page.get_title()
