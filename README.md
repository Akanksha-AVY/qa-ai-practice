# 🤖 QA AI Practice — Automated Testing with AI Assistance

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.0+-green?logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-9.0+-orange?logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=github-actions&logoColor=white)
![Status](https://img.shields.io/badge/Tests-Passing-brightgreen)

> A production-ready QA Automation framework built using **Selenium**, **Pytest**, and **GitHub Copilot AI assistance** — featuring UI testing, REST API testing, and a fully automated CI/CD pipeline via GitHub Actions.

---

## 📁 Project Structure

```
qa-ai-practice/
├── tests/
│   ├── test_login.py        # Selenium UI tests — login flow automation
│   └── test_api.py          # REST API tests — CRUD & auth validation
├── .github/
│   └── workflows/
│       └── selenium-tests.yml  # GitHub Actions CI/CD pipeline
├── requirements.txt
└── .gitignore
```

---

## ✨ Features

- ✅ **UI Test Automation** — Selenium + WebDriverManager + Pytest
- ✅ **API Test Automation** — REST API validation with `requests`
- ✅ **Page Object Model** — Clean, maintainable test architecture
- ✅ **Explicit Waits** — Zero `time.sleep()`, full `WebDriverWait` usage
- ✅ **Headless Chrome** — CI/CD compatible browser execution
- ✅ **GitHub Actions Pipeline** — Auto-runs tests on every push
- ✅ **AI-Assisted Development** — Tests generated using GitHub Copilot
- ✅ **Meaningful Assertions** — Every test has descriptive failure messages

---

## 🧪 Test Suites

### 1. UI Tests — `tests/test_login.py`

Tests the login flow on [Practice Test Automation](https://practicetestautomation.com/practice-test-login/) site.

| Test | Scenario | Type |
|---|---|---|
| `test_valid_login` | Login with correct credentials | Happy Path |
| `test_invalid_login` | Login with wrong password | Negative |
| `test_empty_fields` | Submit with empty fields | Edge Case |

### 2. API Tests — `tests/test_api.py`

Tests REST API endpoints on [JSONPlaceholder](https://jsonplaceholder.typicode.com).

| Test | Endpoint | Method | Validates |
|---|---|---|---|
| `test_get_users` | `/users` | GET | Status 200 + data list |
| `test_get_user_by_id` | `/users/1` | GET | User id + username |
| `test_get_nonexistent_user` | `/users/999` | GET | Status 404 |
| `test_create_post` | `/posts` | POST | Status 201 + response body |
| `test_update_post` | `/posts/1` | PUT | Status 200 + updated title |
| `test_delete_post` | `/posts/1` | DELETE | Status 200 |
| `test_response_time` | `/users` | GET | Response under 2 seconds |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- Google Chrome browser
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Akanksha-AVY/qa-ai-practice.git
cd qa-ai-practice

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run only UI tests
pytest tests/test_login.py -v

# Run only API tests
pytest tests/test_api.py -v

# Run with short traceback
pytest tests/ -v --tb=short

# Run in headless mode (CI)
pytest tests/ -v --tb=short
```

---

## ⚙️ CI/CD Pipeline

Every push to `main` automatically triggers the GitHub Actions pipeline which:

1. 🖥️ Spins up a fresh Ubuntu environment
2. 🐍 Installs Python 3.12
3. 🌐 Installs Google Chrome
4. 📦 Installs all dependencies
5. 🧪 Runs the full test suite
6. ✅ Reports pass/fail results

```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

View live pipeline runs → [Actions Tab](https://github.com/Akanksha-AVY/qa-ai-practice/actions)

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.12 | Core language |
| Selenium | 4.0+ | UI browser automation |
| Pytest | 9.0+ | Test framework |
| Requests | 2.31+ | API HTTP calls |
| WebDriverManager | 4.0+ | Auto ChromeDriver management |
| GitHub Actions | — | CI/CD pipeline |
| GitHub Copilot | — | AI-assisted test generation |

---

## 🤖 AI-Assisted Development

This project was built using **GitHub Copilot** as an AI coding assistant:

- 💡 Test cases generated from **intent-based comments**
- 🔍 Locators and assertions **reviewed and validated** manually
- 🛠️ Copilot Chat used for **refactoring and debugging**
- 🚀 CI/CD pipeline config **co-written with AI assistance**

> *"I treat Copilot like a junior developer whose code I always review — AI generates the structure, I validate the logic."*

---

## 📊 Key Testing Concepts Demonstrated

- **Page Object Model (POM)** — Separation of locators and test logic
- **Explicit Waits** — `WebDriverWait` with `expected_conditions`
- **Fixtures** — Pytest `@pytest.fixture` with `yield` for setup/teardown
- **Negative Testing** — Invalid credentials, missing fields, 404 responses
- **API Validation** — Status codes, response body, schema, response time
- **Headless Execution** — `--headless`, `--no-sandbox` for CI compatibility
- **F-strings** — Meaningful failure messages in every assertion

---

## 👩‍💻 Author

**Akanksha Yadav**  
QA Automation Engineer | 4+ Years Experience  
📧 yadavakanksha.akki98@gmail.com  
📍 Dubai, UAE

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ If you found this useful, please give it a star!
