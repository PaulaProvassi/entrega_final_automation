from os import name

import pytest
from selenium import webdriver

from utils.data_reader import read_user_csv
from page.login_page import LoginPage
import pathlib
import pytest_html


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") # Abre en modo headless
    options.add_argument("--incognito") # Abre en modo incógnito
    
    driver = webdriver.Chrome(options=options)
    
    yield driver # Aquí el test "se mete" y corre
    
    driver.quit() # Cuando el test termina, se cierra solo


@pytest.fixture # Globaliza el driver ya logueado 
def driver_logged(driver):
    login_page = LoginPage(driver)

    user = read_user_csv()[0]  # Obtiene el primer usuario del CSV
    
    login_page.login(user['username'], user['password'])
    
    yield driver@pytest.hookimpl(tryfirst=True, hookwrapper=True)


def pytest_runtest_makereport(item, call):
    # Ejecuta el hook original y obtiene el resultado
    outcome = yield
    report = outcome.get_result()

    # Si la prueba falló, toma una captura de pantalla
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver') or item.funcargs.get('driver_logged') # Obtiene el driver del fixture

        if driver:
            target = pathlib.Path("reports/screenshots")
            target.mkdir(parents=True, exist_ok=True)

            file_name = target / f"{item.name}.png"

            driver.save_screenshot(str(file_name))

            if hasattr(report, 'extra'):
                report.extra.append({
                    "name": 'screenshot',
                    "format": 'image/png',
                    'content': str(file_name)
                })

            extras = getattr(report, 'extra', [])
            extras.append(pytest_html.extras.png(str(file_name))) 

            report.extras = extras