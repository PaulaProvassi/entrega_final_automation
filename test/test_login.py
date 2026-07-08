from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page.login_page import LoginPage
from utils.logger import logger
import pytest

@pytest.mark.smoke
def test_login_validation(driver):
    logger.info("Iniciando el driver para test_login_ok")
    login_page = LoginPage(driver)

    logger.info("Iniciando el test de login con usuario y contraseña válidos")
    login_page.login("standard_user", "secret_sauce")

    logger.info("Iniciando sesion...")
    
    assert "/inventory.html" in driver.current_url, "No se redirigió a la página de inventario después del login"
    logger.info("Login exitoso")

@pytest.mark.smoke
def test_login_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.login("standard_user", "wrong_password")

    error_message = login_page.get_error_password_message()
    
    #assert "Epic sadface: Username and password do not match any user in this service", "No se mostró el mensaje de error esperado para contraseña incorrecta"

    assert error_message == "hola"