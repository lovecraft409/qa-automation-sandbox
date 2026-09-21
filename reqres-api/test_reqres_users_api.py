import pytest
import requests

BASE_URL = "https://reqres.in/api"


@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        (2, 200),
        (999, 404),
    ],
)
def test_get_user(headers, user_id, expected_status):
    response = requests.get(f"{BASE_URL}/users/{user_id}", headers=headers)

    assert response.status_code == expected_status

    if expected_status == 200:
        assert "data" in response.json()
