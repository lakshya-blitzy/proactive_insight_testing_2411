# Proactive Insights Testing – 101

Compact FastAPI + SQLite sample shop application for repository scanning and test-generation validation. This is a demo fixture, not production-ready commerce software.

## Features
- User registration and login
- PBKDF2 password hashing
- Product creation and listing
- Order creation and retrieval
- SQLite persistence and lightweight HTML/JavaScript UI
- API validation and end-to-end workflow tests

## Run locally
Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```
Open http://127.0.0.1:8000 and API docs at http://127.0.0.1:8000/docs.

## Run tests
```bash
pytest -v
```

## Suggested scan scope
- Unit: input validation and password hashing/verification.
- Integration: API/database persistence and error handling.
- E2E: register → login → create product → place order → retrieve order.
- Non-functional: concurrency, response-time baselines, invalid-input handling, dependency/security scanning.

The `shop.db` file is created automatically at runtime. Authentication is simplified for test-fixture purposes; do not use this demo for real customer data.
