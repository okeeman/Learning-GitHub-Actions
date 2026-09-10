import pytest
from app import app

@pytest.fixture
def client():
    """Fixture to create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home route returns correct message."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello, Flask!"

def test_add_numbers_success(client):
    """Test adding two valid numbers."""
    response = client.get("/add?a=5&b=3")
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 8

def test_add_numbers_missing_params(client):
    """Test missing query parameters."""
    response = client.get("/add?a=5")
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data

def test_add_numbers_invalid_params(client):
    """Test invalid number format."""
    response = client.get("/add?a=abc&b=3")
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
