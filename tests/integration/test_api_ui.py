
import pytest
import requests
from pages.dashboard_page import DashboardPage
from config.config import Config

@pytest.mark.integration
def test_api_data_displays_in_ui(page):
    """Test API data is correctly displayed in UI"""
    # Make API call
    response = requests.get(f'{Config.BASE_URL}/api/stats')
    assert response.status_code == 200
    api_data = response.json()
    
    # Check UI displays the data
    dashboard_page = DashboardPage(page)
    dashboard_page.navigate()
    
    # Verify UI matches API data
    assert dashboard_page.is_dashboard_loaded()
    # Add specific assertions based on your API structure

@pytest.mark.integration
def test_form_submission_creates_api_record(page):
    """Test form submission creates record via API"""
    from pages.form_page import FormPage
    from faker import Faker
    
    fake = Faker()
    form_page = FormPage(page)
    form_page.navigate()
    
    email = fake.email()
    form_page.fill_form(
        name=fake.name(),
        email=email,
        message=fake.text()
    )
    form_page.submit_form()
    
    # Verify via API
    response = requests.get(f'{Config.BASE_URL}/api/submissions')
    submissions = response.json()
    assert any(s['email'] == email for s in submissions)
