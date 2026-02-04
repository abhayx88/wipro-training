import pytest
import requests

# -------------------------------------------------
# but here INCLUDED IN SAME FILE
# -------------------------------------------------
@pytest.fixture
def base_url():
    return "http://127.0.0.1:5000/api/patients"


# -------------------------------------------------
# STEP 5.3 : PARAMETERIZED TEST
# -------------------------------------------------
@pytest.mark.parametrize(
    "patient_data",
    [
        {
            "name": "Rahul",
            "age": 30,
            "gender": "Male",
            "disease": "Fever",
            "doctor": "Dr. Sharma"
        },
        {
            "name": "Neha",
            "age": 25,
            "gender": "Female",
            "disease": "Cold",
            "doctor": "Dr. Verma"
        }
    ]
)
def test_add_multiple_patients(base_url, patient_data):
    response = requests.post(base_url, json=patient_data)

    assert response.status_code == 201
    assert response.json()["message"] == "Patient added"


# -------------------------------------------------
# GET ALL PATIENTS
# -------------------------------------------------
def test_get_all_patients(base_url):
    response = requests.get(base_url)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# -------------------------------------------------
# STEP 5.4 : SKIP TEST
# -------------------------------------------------
@pytest.mark.skip(reason="Delete patient API not implemented yet")
def test_delete_patient():
    pass


# -------------------------------------------------
# STEP 5.4 : XFAIL TEST
# -------------------------------------------------
@pytest.mark.xfail(reason="Known bug: invalid patient id handling")
def test_get_invalid_patient(base_url):
    response = requests.get(f"{base_url}/999")
    assert response.status_code == 200   # intentionally wrong
