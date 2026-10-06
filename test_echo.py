import requests


def test_get_without_params():
    response = requests.get("https://postman-echo.com/get")
    assert response.status_code == 201
    data = response.json()
    assert data["args"] == {}


def test_get_with_params():
    params = {
        "name": "Ksenia"
    }
    response = requests.get(
        "https://postman-echo.com/get",
        params=params
        )
    assert response.status_code == 200
    data = response.json()
    assert data["args"] == params


def test_post_without_body():
    response = requests.post("https://postman-echo.com/post")
    assert response.status_code == 200
    data = response.json()
    assert data["json"] is None
    assert data["data"] == {}


def test_post_with_json():
    info = {
        "name": "Ksenia",
        "age": "21"
        }
    response = requests.post(
        "https://postman-echo.com/post",
        json=info
        )
    assert response.status_code == 200
    data = response.json()   
    assert data["json"] == info
   

def test_post_with_params_and_json():
    params = {
        "city": "Yaroslavl"
    }
    info = {
        "name": "Ksenia",
        "age": "21"
    }
    response = requests.post(
        "https://postman-echo.com/post",
        params=params,
        json=info
        )
    assert response.status_code == 200
    data = response.json()   
    assert data["json"] == info
    assert data["args"] == params