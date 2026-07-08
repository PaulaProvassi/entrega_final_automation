import requests
import pytest_check as check
import pytest

headers = {
    "x-api-key": "pub_149f4a57250164c80cc4128a9c073e5c9999872da2e9f583e58576b364aefb0a"
}

@pytest.mark.api
# 1. Prueba GET
def test_obtener_usuario():
    response = requests.get("https://reqres.in/api/users/2", headers=headers)
    check.equal(response.status_code, 200)

@pytest.mark.api
# 2. Prueba POST 
def test_crear_usuario():
    nuevo_usuario = {
        "name": "Paula Provassi",
        "job": "Automation Tester"
    }
    response = requests.post("https://reqres.in/api/users", headers=headers, json=nuevo_usuario)
    assert response.status_code == 201

@pytest.mark.api
# 3. Prueba PUT 
def test_actualizar_usuario_completo():
    datos_put = {
        "name": "Paula Elizabeth",
        "job": "QA Automation Engineer"
    }
    response = requests.put("https://reqres.in/api/users/2", headers=headers, json=datos_put)
    check.equal(response.status_code, 200)

@pytest.mark.api
# 4. Prueba PATCH 
def test_actualizar_usuario_parcial():
    datos_patch = {
        "job": "Lead QA"
    }
    response = requests.patch("https://reqres.in/api/users/2", headers=headers, json=datos_patch)
    assert response.status_code == 200

@pytest.mark.api
# 5. Prueba LOGIN VÁLIDO
def test_login_valido():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslickka"
    }
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    assert response.status_code == 200

@pytest.mark.api
# 6. Prueba LOGIN INVÁLIDO
def test_login_invalido():
    body = {
        "email": "eve.holt@reqres.in",
    }
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    assert response.status_code == 400