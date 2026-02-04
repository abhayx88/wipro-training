import pytest
import requests

# ✅ FIXTURE (YAHAN ADD KARO)
@pytest.fixture
def base_url():
    return "http://127.0.0.1:5000"

# -------------------------
# TEST CASES
# -------------------------

def test_get_all_movies(base_url):
    response = requests.get(f"{base_url}/api/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_movie(base_url):
    payload = {
        "id": 102,
        "movie_name": "Inception",
        "language": "English",
        "duration": "2h 28m",
        "price": 300
    }

    response = requests.post(
        f"{base_url}/api/movies",
        json=payload
    )

    assert response.status_code == 201


def test_book_ticket(base_url):
    payload = {
        "movie_id": 101,
        "user": "Abhay",
        "tickets": 2
    }

    response = requests.post(
        f"{base_url}/api/bookings",
        json=payload
    )

    assert response.status_code == 201
