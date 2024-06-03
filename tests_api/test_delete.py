import requests
import pytest
import allure


URL = "https://petstore.swagger.io/v2/"

@allure.feature("DELETE")
@allure.title("Delete pet")
@allure.id("1")
@pytest.mark.xfail
@pytest.mark.api_testing
@pytest.mark.new_features_testing
def test_delete_pet():
    payload = {
        "id": 1,
        "category": {
            "id": 1,
            "name": "cat"
        },
        "name": "Lyna",
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
    post_response = requests.post(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200
    pet_id = post_response.json()["id"]

    delete_response = requests.delete(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )
    assert delete_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 404

    delete_response = requests.delete(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )
    assert delete_response.status_code == 200
