from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_product_validation():
    response = client.post("/products", json={"name": "Bad", "price": -1, "stock": 2})
    assert response.status_code == 422
