# 🧪 QA Automation Portfolio

**QA Engineer | Mobile & API Testing | Playwright | Scrum Master**

Hi! I'm Tanu Gupta , a Quality Assurance Engineer with 4+ years of experience in manual testing, iOS mobile testing, and test planning. I previously served as iOS QA Lead at Infosys. I hold a Master's degree from California State University, San Bernardino, a Certified Scrum Master credential, and CompTIA Security+ certification.

This portfolio showcases my automation testing skills using **Playwright (Python)** and **Postman API Testing**.

---

## 📁 Portfolio Structure

```
qa-automation-portfolio/
├── playwright-tests/
│   ├── test_01_login.py              # Login functionality tests
│   ├── test_02_form_filling.py       # Form filling & validation
│   ├── test_03_shopping_cart.py      # Shopping cart operations
│   ├── test_04_checkout_e2e.py       # Full end-to-end checkout
│   └── test_05_screenshots.py        # Screenshot & visual testing
├── postman-collections/
│   └── QA_Portfolio_API_Tests.postman_collection.json
├── screenshots/                       # Generated test screenshots
├── requirements.txt
└── README.md
```

---

## 🎭 Playwright Test Suite (UI Automation)

Automated tests for [SauceDemo](https://www.saucedemo.com/) and [DemoQA](https://demoqa.com/) — two popular demo sites for QA practice.

### Test Descriptions

| # | Test File | What It Tests | Test Cases |
|---|-----------|---------------|------------|
| 1 | `test_01_login.py` | Login functionality | Valid login, invalid credentials, locked-out user |
| 2 | `test_02_form_filling.py` | Form submission & validation | Fill text fields, submit, verify output, invalid email |
| 3 | `test_03_shopping_cart.py` | Cart operations | Add single item, add multiple items, verify contents, remove item |
| 4 | `test_04_checkout_e2e.py` | Complete checkout flow (E2E) | Login → Add item → Cart → Checkout → Order complete |
| 5 | `test_05_screenshots.py` | Visual testing & screenshots | Full page, element capture, error states, responsive viewports |

### How to Run

```bash
# 1. Clone this repository
git clone https://github.com/[your-username]/qa-automation-portfolio.git
cd qa-automation-portfolio

# 2. Install dependencies
pip install -r requirements.txt
playwright install

# 3. Run all tests
python -m pytest playwright-tests/ -v

# 4. Or run individual test files
python playwright-tests/test_01_login.py
python playwright-tests/test_04_checkout_e2e.py
```

---

## 📮 Postman API Test Collection

A comprehensive API test collection covering CRUD operations against [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — a free REST API for testing.

### API Tests Included

| # | Request | Method | What It Tests |
|---|---------|--------|---------------|
| 1 | Fetch All Users | `GET` | Response structure, array length, required fields |
| 2 | Fetch Single User | `GET` | Specific user data, nested objects, content type |
| 3 | Fetch User's Posts | `GET` | Nested resources, data relationship validation |
| 4 | Create New Post | `POST` | Resource creation, 201 status, response body match |
| 5 | Update Existing Post | `PUT` | Resource update, data persistence |
| 6 | Delete a Post | `DELETE` | Resource deletion, 200 confirmation |
| 7 | Non-existent User | `GET` | Negative test — 404 handling |
| 8 | Filter by Query Param | `GET` | Query parameter filtering, result validation |

### How to Import & Run

1. Open **Postman** (download free at [postman.com](https://www.postman.com/downloads/))
2. Click **Import** → Select `postman-collections/QA_Portfolio_API_Tests.postman_collection.json`
3. Click **Run Collection** to execute all 8 tests with assertions

---

## 🛠️ Technical Skills

**Testing:** Test Planning, Test Case Design, Defect Lifecycle, Regression Testing, UAT, Smoke & Sanity, Functional Testing, Mobile Testing (iOS/Android), Accessibility Testing (WCAG 2.1)

**Automation:** Playwright (Python), Postman API Testing, SQL (Data Validation)

**Tools:** Jira, Git/GitHub, Postman, Burp Suite, Wireshark, Nmap

**Methodologies:** Agile/Scrum (Certified Scrum Master), SDLC, STLC, Risk-Based Testing

**Security:** CompTIA Security+, API Security, SIEM, IDS/IPS

---

## 📜 Certifications

- ✅ Certified Scrum Master (CSM)
- ✅ CompTIA Security+
- ✅ Postman API Fundamentals Student Expert *(in progress)*

---

## 📫 Contact

- **LinkedIn:** [your-linkedin-url]
- **Email:** [your-email]
- **Location:** San Bernardino, CA

---

*This portfolio demonstrates my transition from manual QA into automation testing. I combine strong manual testing fundamentals with growing automation skills to deliver thorough quality assurance.*
