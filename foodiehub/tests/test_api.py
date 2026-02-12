import requests

BASE = "http://127.0.0.1:5000/api"

def test_register():
    res = requests.post(
        f"{BASE}/register",
        json={
            "name": "Abhay",
            "email": "abhay@test.com",
            "password": "1234"
        }
    )

    assert res.status_code in [201,409]


def test_login():
    res = requests.post(
        f"{BASE}/login",
        json={
            "email": "abhay@test.com",
            "password": "1234"
        }
    )

    assert res.status_code == 200
    assert "access_token" in res.json()
