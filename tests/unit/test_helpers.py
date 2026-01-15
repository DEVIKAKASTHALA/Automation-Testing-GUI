
import pytest
from utils.helpers import generate_random_email, format_phone_number

@pytest.mark.unit
def test_generate_random_email():
    """Test random email generation"""
    email = generate_random_email()
    assert '@' in email
    assert '.' in email
    assert len(email) > 5

@pytest.mark.unit
def test_format_phone_number():
    """Test phone number formatting"""
    formatted = format_phone_number('1234567890')
    assert len(formatted) > 10
    assert formatted.startswith('(')
