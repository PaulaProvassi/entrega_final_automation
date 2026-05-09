from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login(driver):
    # ingresar a la pagina de login
    driver.get("https://www.saucedemo.com/")        

    # ingresar el usuario
    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user")

    # ingresar la contraseña
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    # presionar el botón de login
    password.send_keys(Keys.ENTER)