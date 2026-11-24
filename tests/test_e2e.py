from fastapi.testclient import TestClient
from app import app
import uuid

client = TestClient(app)

def test_customer_purchase_workflow():
    email = f"buyer-{uuid.uuid4().hex[:8]}@example.com"
    user = client.post("/users", json={"name": "Test Buyer", "email": email, "password": "StrongPass123"})
    assert user.status_code == 201
    user_id = user.json()["id"]
    login = client.post("/login", json={"name": "Test Buyer", "email": email, "password": "StrongPass123"})
    assert login.status_code == 200
    product = client.post("/products", json={"name": "Test Keyboard", "price": 49.99, "stock": 10})
    assert product.status_code == 201
    order = client.post("/orders", json={"user_id": user_id, "product_id": product.json()["id"], "quantity": 2})
    assert order.status_code == 201
    assert order.json()["total"] == 99.98
    assert client.get(f"/orders/{order.json()['id']}").status_code == 200
