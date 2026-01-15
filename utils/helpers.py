@"
import random
import string
from faker import Faker

fake = Faker()

def generate_random_email():
    \"\"\"Generate random email address\"\"\"
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f'{username}@test.com'

def generate_random_string(length=10):
    \"\"\"Generate random string\"\"\"
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def format_phone_number(phone):
    \"\"\"Format phone number to (XXX) XXX-XXXX\"\"\"
    cleaned = ''.join(filter(str.isdigit, phone))
    if len(cleaned) == 10:
        return f'({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}'
    return phone

def generate_test_data():
    \"\"\"Generate test data dictionary\"\"\"
    return {
        'name': fake.name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'address': fake.address(),
        'company': fake.company()
    }
"@ | Out-File -FilePath "utils\helpers.py" -Encoding UTF8