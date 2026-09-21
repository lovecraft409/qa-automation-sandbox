import os

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def api_key():
    key = os.getenv("REQRES_API_KEY")
    assert key, "REQRES_API_KEY is not set"
    return key


@pytest.fixture(scope="session")
def headers(api_key):
    return {"x-api-key": api_key}
