import requests
import allure

URL = "https://petstore.swagger.io/v2/"

@allure.feature("GET")
@allure.title("Get pet by petID")
@allure.id("1")
def test_get_pet_id():
    pet_id = 123
    response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )
    assert response.status_code in [200, 404], f"error: {response.status_code}"

    if response.status_code == 200:
        pet_data = response.json()
        assert "id" in pet_data, "There is no pet ID"
        assert "name" in pet_data, "There is no pet name"
    else:
        print("The pet was not found")

    print("The pet was found")

@allure.feature("GET")
@allure.title("Find pet by status")
@allure.id("2")
def test_pet_find_by_status():
    get_response = requests.get(
        url=f"{URL}pet/findByStatus",
        params={"status": "available"},
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200
    get_response = requests.get(
        url=f"{URL}pet/findByStatus",
        params={"status": "pending"},
        headers={"accept": "application/json"}
    )

    assert get_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}pet/findByStatus",
        params={"status": "sold"},
        headers={"accept": "application/json"}
    )
    jsn = get_response.json()
    assert get_response.status_code == 200
    print()
    print(jsn)
