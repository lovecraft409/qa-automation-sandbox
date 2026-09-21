import pytest
import requests

BASE_URL = "https://reqres.in/api"


@pytest.mark.parametrize(
    "name, job, expected_status",
    [
        ("James", "Qa Automation", 200),
    ],
)
def test_update_user(headers, name, job, expected_status):
    response = requests.patch(
        f"{BASE_URL}/users/2",
        json={"name": name, "job": job},
        headers=headers,
    )

    assert response.status_code == expected_status

    response_data = response.json()
    assert response_data["name"] == name
    assert response_data["job"] == job
