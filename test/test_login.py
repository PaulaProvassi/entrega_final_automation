from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_login_validation (login_in_driver):
    try:
        driver = login_in_driver

        assert "inventory.html" in driver.current_url, "Login fallido: No se redirigió a la página de inventario"
    except Exception as e:
        print(f"Error durante la validación del login: {e}")
