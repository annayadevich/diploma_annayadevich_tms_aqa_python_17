import requests
import allure
URL = "https://petstore.swagger.io/v2/"

@allure.feature("PUT")
@allure.title("Update pet")
@allure.id("1")
def test_update_pet():
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
    post_response = requests.post(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200
    pet_id = post_response.json()["id"]

    update_payload = {
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

    put_response = requests.put(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=update_payload
    )
    assert put_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200
    print(get_response.json())

# def test_update_pet_with_form_data(pet_id=None):
#     post_response = requests.post(
#         url=f"{URL}pet/{pet_id}",
#         params={"petid": 123,
#                 "name": "Lyna",
#                 "status": "available"},
#         headers={"accept": "application/json"}
#     )
#     assert post_response.status_code == 200

