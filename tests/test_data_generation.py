import pytest
import random
import string
from datetime import datetime, timedelta

# ============================================
# TEST DATA GENERATORS
# ============================================

# Write a function generate_valid_user() that returns
# a dictionary with realistic fake user data containing:
# first_name, last_name, email using first+last+random 4 digits @testmail.com,
# phone in format +971-5XX-XXXXXXX (UAE format),
# date_of_birth as string 25-35 years ago in YYYY-MM-DD format,
# national_id as string of 10 random digits,
# country "UAE" 
def generate_valid_user():
    first_name = random.choice(["Alice", "Bob", "Charlie", "Diana", "Ethan"])
    last_name = random.choice(["Smith", "Johnson", "Williams", "Brown", "Jones"])
    random_digits = ''.join(random.choices(string.digits, k=4))
    email = f"{first_name.lower()}.{last_name.lower()}{random_digits}@testmail.com"
    phone = f"+971-5{random.randint(0, 9)}{random.randint(0, 9)}-{random.randint(1000000, 9999999)}"
    date_of_birth = (datetime.now() - timedelta(days=random.randint(25*365, 35*365))).strftime("%Y-%m-%d")
    national_id = ''.join(random.choices(string.digits, k=10))
    country = "UAE"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "date_of_birth": date_of_birth,
        "national_id": national_id,
        "country": country
    }   

# Write a function generate_valid_payment() that returns
# a dictionary with:
# transaction_id as "TXN" + 8 random uppercase letters,
# amount as random float between 100 and 10000 rounded to 2 decimals,
# currency randomly chosen from USD AED EUR GBP,
# status "pending",
# timestamp as current datetime in ISO format,
# sender_id and receiver_id as random integers between 1000 and 9999 
def generate_valid_payment():
    transaction_id = "TXN" + ''.join(random.choices(string.ascii_uppercase, k=8))
    amount = round(random.uniform(100, 10000), 2)
    currency = random.choice(["USD", "AED", "EUR", "GBP"])
    status = "pending"
    timestamp = datetime.now().isoformat()
    sender_id = random.randint(1000, 9999)
    receiver_id = random.randint(1000, 9999)

    return {
        "transaction_id": transaction_id,
        "amount": amount,
        "currency": currency,
        "status": status,
        "timestamp": timestamp,
        "sender_id": sender_id,
        "receiver_id": receiver_id
    }

# Write a function generate_invalid_user() that returns
# a dictionary with intentionally bad data:
# empty first_name,
# invalid email without @ symbol,
# phone with letters instead of numbers,
# date_of_birth as future date,
# national_id with only 5 digits instead of 10 
def generate_invalid_user():
    first_name = ""
    last_name = "Doe"
    email = "invalidemail.com"
    phone = "+971-5XX-ABCDE"
    date_of_birth = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
    national_id = ''.join(random.choices(string.digits, k=5))  # Only 5 digits
    country = "UAE"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "date_of_birth": date_of_birth,
        "national_id": national_id,
        "country": country
    }           

# ============================================
# TESTS USING GENERATED DATA
# ============================================

# Write a pytest class TestDataGeneration with the following test cases:

    # Test 1: generate 5 valid users, assert each has
    # all required fields, email contains @,
    # phone starts with +971, national_id is 10 digits

    # Test 2: generate 10 valid payments, assert each has
    # unique transaction_id, amount between 100 and 10000,
    # currency is one of USD AED EUR GBP,
    # status is pending

    # Test 3: generate invalid user and assert
    # all fields have the expected invalid values
    # (this simulates negative test data generation)  
class TestDataGeneration:
    
    def test_generate_valid_users(self):
        for _ in range(5):
            user = generate_valid_user()
            assert 'first_name' in user and user['first_name'], "User missing 'first_name' or it is empty"
            assert 'last_name' in user and user['last_name'], "User missing 'last_name' or it is empty"
            assert 'email' in user and '@' in user['email'], "User missing 'email' or it does not contain '@'"
            assert 'phone' in user and user['phone'].startswith('+971'), "User missing 'phone' or it does not start with '+971'"
            assert 'national_id' in user and len(user['national_id']) == 10 and user['national_id'].isdigit(), "User missing 'national_id' or it is not 10 digits"

    def test_generate_valid_payments(self):
        transaction_ids = set()
        for _ in range(10):
            payment = generate_valid_payment()
            assert payment['transaction_id'] not in transaction_ids, f"Duplicate transaction_id found: {payment['transaction_id']}"
            transaction_ids.add(payment['transaction_id'])
            assert 100 <= payment['amount'] <= 10000, f"Payment amount {payment['amount']} is out of expected range"
            assert payment['currency'] in ["USD", "AED", "EUR", "GBP"], f"Payment currency {payment['currency']} is not valid"
            assert payment['status'] == "pending", f"Payment status {payment['status']} is not 'pending'"

    def test_generate_invalid_user(self):
        user = generate_invalid_user()
        try:
            assert user['first_name'] == "", "Expected empty first_name"
            assert '@' not in user['email'], "Expected email without '@'"
            assert not user['phone'][7:].isdigit(), "Expected phone to have letters instead of numbers"
            future_date = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
            assert user['date_of_birth'] == future_date, f"Expected date_of_birth to be a future date {future_date}"
            assert len(user['national_id']) == 5 and user['national_id'].isdigit(), "Expected national_id to have only 5 digits"
        except AssertionError as e:
            pytest.fail(f"Data validation failed: {e}")
