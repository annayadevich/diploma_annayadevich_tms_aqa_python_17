import requests
import allure

URL = "https://petstore.swagger.io/v2/"

@allure.feature("POST")
@allure.title("Create pet")
@allure.id("1")
def test_add_pet():
    payload = {
        "id": 3,
        "category": {
            "id": 3,
            "name": "dog"
        },
        "name": "Amily",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 3,
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
    get_response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}pet/2666666",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 404



# def test_upload_image():
#     base_url = "https://petstore.swagger.io/v2"
#     pet_id = 123
#     file_path = "D:\Work\Test data\Pictures\pngformat.png"
#
#     files = {"file": open(file_path, "rb")}
#     response = requests.post(f"{base_url}/pet/{pet_id}/uploadImage", files=files)
#
#     assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
#     assert "uploaded" in response.text, "File upload failed"