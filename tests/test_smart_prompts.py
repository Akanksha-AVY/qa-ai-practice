import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# # ============================================
# PROMPT 1 — Data validation test
# ============================================
# Test GET /users/1 and validate ALL fields:
# id is integer, name is non-empty string,
# email contains "@", address has city field,
# company has name field and catch any exceptions in validation
class TestUserAPI:
    
    def test_get_user(self):
        response = requests.get(f"{BASE_URL}/users/1")
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        
        user = response.json()
        try:
            assert isinstance(user['id'], int), "User 'id' is not an integer"
            assert isinstance(user['name'], str) and user['name'].strip() != "", "User 'name' is empty or not a string"
            assert '@' in user['email'], "User 'email' does not contain '@'"
            assert 'city' in user['address'], "User 'address' does not contain 'city'"
            assert 'name' in user['company'], "User 'company' does not contain 'name'"
        except AssertionError as e:
            pytest.fail(f"Data validation failed: {e}")


# ============================================
# PROMPT 2 — Query parameter test
# ============================================
# Test GET /posts with query param _limit=5
# Assert: exactly 5 posts returned,
# each post has id title body and userId,
# all userIds are positive integers 
    def test_get_posts_with_limit(self):
        response = requests.get(f"{BASE_URL}/posts", params={"_limit": 5})
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        
        posts = response.json()
        assert isinstance(posts, list), f"Expected response to be a list, got {type(posts)}"
        assert len(posts) == 5, f"Expected 5 posts, got {len(posts)}"
        
        for post in posts:
            assert 'id' in post, "Post missing 'id' field"
            assert 'title' in post, "Post missing 'title' field"
            assert 'body' in post, "Post missing 'body' field"
            assert 'userId' in post, "Post missing 'userId' field"
            assert isinstance(post['userId'], int) and post['userId'] > 0, "Post 'userId' is not a positive integer"

# ============================================
# PROMPT 3 — Create and verify pattern
# ============================================
# Test POST /posts with title "KYC Verification Test"
# body "Testing financial onboarding flow" userId 1
# Assert: status 201, response id is integer,
# title and body match exactly what was sent and userId is 1
    def test_create_post(self):
        payload = {
            "title": "KYC Verification Test",
            "body": "Testing financial onboarding flow",
            "userId": 1
        }
        response = requests.post(f"{BASE_URL}/posts", json=payload)
        assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
        
        post = response.json()
        assert isinstance(post['id'], int), "Response 'id' is not an integer"
        assert post['title'] == payload['title'], f"Expected title '{payload['title']}', got '{post['title']}'"
        assert post['body'] == payload['body'], f"Expected body '{payload['body']}', got '{post['body']}'"
        assert post['userId'] == payload['userId'], f"Expected userId {payload['userId']}, got {post['userId']}"


# ============================================
# PROMPT 4 — Performance + uniqueness test
# ============================================
# Test GET /users and validate: 
# status 200, returns exactly 10 users, 
# every user has unique id, 
# every user email contains @, 
# total response time under 3 seconds  
# and if any assertion fails, print which validation failed
    def test_get_users(self):
        response = requests.get(f"{BASE_URL}/users")
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        failures = []

        # response time under 3 seconds
        elapsed = response.elapsed.total_seconds()
        if elapsed >= 3:
            failures.append(f"Response time too slow: {elapsed:.2f}s (>= 3s)")

        # parse users and validate structure
        try:
            users = response.json()
        except Exception as e:
            pytest.fail(f"Failed to parse JSON response: {e}")

        if not isinstance(users, list):
            failures.append(f"Expected list of users, got {type(users)}")
        else:
            # exactly 10 users returned
            if len(users) != 10:
                failures.append(f"Expected 10 users, got {len(users)}")

            # all user ids are unique
            ids = [u.get('id') for u in users]
            if len(set(ids)) != len(ids):
                failures.append("User ids are not unique")

            # every user email contains '@'
            for u in users:
                uid = u.get('id', '<unknown>')
                email = (u.get('email') or '')
                if '@' not in email:
                    failures.append(f"User id {uid} has invalid email: '{email}'")

        # if any assertion failed, fail with details
        if failures:
            pytest.fail("Data validation failed:\n" + "\n".join(failures))
        