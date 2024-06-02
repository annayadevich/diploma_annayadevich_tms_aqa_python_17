import pytest
import requests
URL = "https://petstore.swagger.io/v2/"


@pytest.fixture
def add_pet():
    payload = {
        "id": 1,
        "category": {
            "id": 1,
            "name": "dog"
        },
        "name": "Amily",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 1,
                "name": "string"
            }
        ],
        "status": "available"
    }

    requests.post(
        url=f'{URL}pet',
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json=payload
    )

    yield payload

    requests.delete(
        url=f'{URL}pet/{payload["pet_id"]}'
    )