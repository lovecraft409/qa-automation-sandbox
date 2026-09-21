import pytest
import requests

BASE_URL = "https://reqres.in/api"


@pytest.mark.parametrize(
    "email, password, expected_status",
    [
        ("eve.holt@reqres.in", "cityslicka", 200),
        ("eve.holt@reqres.in", "", 400),
        ("missing_user@reqres.in", "password", 400),
    ],
)
def test_login(headers, email, password, expected_status):
    response = requests.post(
        f"{BASE_URL}/login",
        json={"email": email, "password": password},
        headers=headers,
    )

    assert response.status_code == expected_status

    if expected_status == 200:
        assert "token" in response.json()
