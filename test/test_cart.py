from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.smoke
def test_cart(login_in_driver):
    driver = login_in_driver
    # Agregar un producto al carrito
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click() 

    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert contador_cart.text == "1", "El producto no se agregó al carrito correctamente"

    # Verificar que el producto se haya agregado al carrito
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "El producto no se agregó al carrito correctamente"

    # Obterner el nombre del primer producto 
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Obterner el nombre del producto en el carrito
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Verificar que el producto en el carrito sea el mismo que se agregó
    assert cart_item == product_name, "El producto en el carrito no coincide"