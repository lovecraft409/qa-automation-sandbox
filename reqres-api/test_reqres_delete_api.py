import pytest
import requests

BASE_URL = "https://reqres.in/api"


@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        (2, 204),
    ],
)
def test_delete_user(headers, user_id, expected_status):
    response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=headers)

    assert response.status_code == expected_status
    assert response.text == ""
