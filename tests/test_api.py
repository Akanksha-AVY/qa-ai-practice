import pytest
import requests

# Base URL constant for https://jsonplaceholder.typicode.com
BASE_URL = "https://jsonplaceholder.typicode.com"

# Write a pytest class TestUserAPI with the following test cases for the JSONPlaceholder API:
class TestUserAPI:
    
    # Test 1: GET /users returns status 200 and list has 10 users with id, name, username, email fields
    def test_get_users(self):
        response = requests.get(f"{BASE_URL}/users")
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        
        users = response.json()
        assert isinstance(users, list), f"Expected response to be a list, got {type(users)}"
        assert len(users) == 10, f"Expected 10 users, got {len(users)}"
        
        for user in users:
            assert 'id' in user, "User missing 'id' field"
            assert 'name' in user, "User missing 'name' field"
            assert 'username' in user, "User missing 'username' field"
            assert 'email' in user, "User missing 'email' field"

    # Test 2: GET /users/1 returns status 200 and user id is 1 
    # and username is "Bret"
    def test_get_user(self):
        response = requests.get(f"{BASE_URL}/users/1")
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        
        user = response.json()
        assert user['id'] == 1, f"Expected user id 1, got {user['id']}"
        assert user['username'] == "Bret", f"Expected username 'Bret', got {user['username']}"

    # Test 3: GET /users/999 returns 404 for non existent user
    def test_get_non_existent_user(self):
        response = requests.get(f"{BASE_URL}/users/999")
        assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"

    # Test 4: POST /posts with title "QA Test" body "Automation"
    # and userId 1 returns 201 and response contains id
    def test_post_post(self):
        response = requests.post(f"{BASE_URL}/posts", json={
            "title": "QA Test",
            "body": "Automation",
            "userId": 1
        })
        assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
        post = response.json()
        assert 'id' in post, "Post missing 'id' field"

    # Test 5: PUT /posts/1 with updated title "Updated by Akanksha" 
    # returns 200 and title matches
    def test_put_post(self):
        response = requests.put(f"{BASE_URL}/posts/1", json={
            "title": "Updated by Akanksha",
            "body": "Updated content",
            "userId": 1
        })
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        post = response.json()
        assert post['title'] == "Updated by Akanksha", f"Expected title 'Updated by Akanksha', got {post['title']}"

    # Test 6: DELETE /posts/1 returns 200
    def test_delete_post(self):
        response = requests.delete(f"{BASE_URL}/posts/1")
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Test 7: GET /users response time is under 2 seconds 
    def test_get_users_response_time(self):
        response = requests.get(f"{BASE_URL}/users")
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        assert response.elapsed.total_seconds() < 2, f"Expected response time under 2 seconds, got {response.elapsed.total_seconds()}"