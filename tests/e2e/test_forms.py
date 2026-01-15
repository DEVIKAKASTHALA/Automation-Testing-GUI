
import pytest
from pages.form_page import FormPage
from faker import Faker

fake = Faker()

@pytest.mark.e2e
def test_submit_form_with_valid_data(page):
   
    form_page = FormPage(page)
    form_page.navigate()
    
    form_page.fill_form(
        name=fake.name(),
        email=fake.email(),
        phone=fake.phone_number(),
        message=fake.text()
    )
    form_page.submit_form()
    
    assert form_page.is_form_submitted_successfully()
    assert 'success' in form_page.get_success_message().lower()

@pytest.mark.e2e
def test_submit_empty_form_shows_errors(page):
   
    form_page = FormPage(page)
    form_page.navigate()
    
    form_page.submit_empty_form()
    
    assert form_page.has_validation_errors()
    assert form_page.get_error_message('email') is not None

@pytest.mark.e2e
def test_invalid_email_format(page):
    
    form_page = FormPage(page)
    form_page.navigate()
    
    form_page.fill_form(
        name=fake.name(),
        email='invalid-email',
        message=fake.text()
    )
    form_page.submit_form()
    
    assert form_page.has_validation_errors()
    error_msg = form_page.get_error_message('email')
    assert 'email' in error_msg.lower() or 'invalid' in error_msg.lower()

@pytest.mark.e2e
@pytest.mark.parametrize('field,value', [
    ('name', ''),
    ('email', ''),
    ('message', '')
])
def test_required_field_validation(page, field, value):

    form_page = FormPage(page)
    form_page.navigate()
    
    form_data = {
        'name': fake.name(),
        'email': fake.email(),
        'message': fake.text()
    }
    form_data[field] = value
    
    form_page.fill_form(**form_data)
    form_page.submit_form()
    
    assert form_page.has_validation_errors()
