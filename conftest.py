import pytest
from selenium import webdriver
from utils.loginPage import login


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito") # Abre en modo incógnito
    
    driver = webdriver.Chrome(options=options)
    
    yield driver # Aquí el test "se mete" y corre
    
    driver.quit() # Cuando el test termina, se cierra solo

@pytest.fixture
def login_in_driver(driver):
    login(driver) # Llama a la función de login para que el driver ya esté logueado
    return driver # Devuelve el driver logueado para usarlo en los tests
