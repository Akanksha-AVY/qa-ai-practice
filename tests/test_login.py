import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Create a pytest fixture that launches Chrome browser and opens https://practicetestautomation.com/practice-test-login/ then quits after test

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.quit()

# Write a test class TestLogin that uses the browser fixture

class TestLogin:

    # Test 1: Login with username "student" and password "Password123" and assert "Congratulations" text is visible
    def test_valid_login(self, browser):
        username_input = browser.find_element(By.ID, "username")
        password_input = browser.find_element(By.ID, "password")
        submit_button = browser.find_element(By.ID, "submit")

        username_input.send_keys("student")
        password_input.send_keys("Password123")
        submit_button.click()

        # Wait for any element containing "Congratulations" to be visible
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Congratulations')]") )
        )

        # assert the success message text is present in the page body
        body_text = browser.find_element(By.TAG_NAME, "body").text
        assert "Congratulations" in body_text


    # Test 2: Login with username "student" and wrong password "wrongpass" and assert error message "Your password is invalid!" is visible
    def test_invalid_login(self, browser):
        username_input = browser.find_element(By.ID, "username")
        password_input = browser.find_element(By.ID, "password")
        submit_button = browser.find_element(By.ID, "submit")

        username_input.send_keys("student")
        password_input.send_keys("wrongpass")
        submit_button.click()

        # Wait for the error message to be visible
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Your password is invalid!')]"))
        )

        # assert error message text equals "Your password is invalid!"
        error_message = browser.find_element(By.XPATH, "//div[contains(text(), 'Your password is invalid!')]")
        assert error_message.text == "Your password is invalid!"


    # Test 3: Leave username and password empty, click login, assert error message is visible
    def test_empty_fields(self, browser):
        # Wait for submit button to be present before interacting
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "submit"))
        )
        submit_button = browser.find_element(By.ID, "submit")
        submit_button.click()

        # Wait until the page body contains an indicator of the validation error
        WebDriverWait(browser, 10).until(
            lambda d: (
                "username" in d.find_element(By.TAG_NAME, "body").text.lower()
                or "at least 2" in d.find_element(By.TAG_NAME, "body").text.lower()
            )
        )

        # assert the body contains an error indication about username length
        body_text = browser.find_element(By.TAG_NAME, "body").text
        assert ("username" in body_text.lower()) or ("at least 2" in body_text.lower())
        
