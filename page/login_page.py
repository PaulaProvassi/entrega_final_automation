from selenium.webdriver.common.by import By

from utils import logger 

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Selectores
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_password_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        try:
            self.driver.get("https://www.saucedemo.com/")
        except:
            logger.critical("No se pudo abrir la página de login")

    def ingresar_usuario(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def ingresar_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
    
    def login(self, username, password):
        self.open()
        self.ingresar_usuario(username)
        self.ingresar_password(password)
        self.click_login()

    def get_error_password_message(self):
        error = self.driver.find_element(*self.error_password_message).text
        print("Mensaje de error:", error)  # Imprime el mensaje de error para depuración    
        return error