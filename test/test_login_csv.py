import pytest
from page.login_page import LoginPage
from utils.data_reader import read_user_csv

@pytest.mark.parametrize("user", read_user_csv())
def test_login_csv(driver, user):
    login_page = LoginPage(driver)
  
    login_page.login(user['username'], user['password'])
    if user['valid'] == "true":
        assert "/inventory.html" in driver.current_url, "No se redireccionó a la página de inventario después de iniciar sesión"
    else:
        error = login_page.get_error_password_message()
        assert "Epic sadface: Username and password do not match any user in this service" in error
    