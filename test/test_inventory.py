from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from page.inventory_page import InventoryPage
from page.login_page import LoginPage

@pytest.mark.smoke
def test_inventory_title(driver_logged):
    inventory_page = InventoryPage(driver_logged)
   
    titulo = inventory_page.get_titulo()
    assert titulo == "Swag Labs", "El título de la página de inventario no es correcto"


def test_products_visible(driver_logged):
    inventory_page = InventoryPage(driver_logged)

    productos = inventory_page.get_productos()
    assert len(productos) > 0, "No se encontraron productos en la página de inventario"
  

def test_ui_elements(driver_logged):
    inventory_page = InventoryPage(driver_logged)

    # Corregido: Ahora interactúa con la página, no con el navegador puro
    assert inventory_page.menu_visible(), "El menú no es visible en la página de inventario"
    assert inventory_page.filtro_visible(), "El filtro no es visible en la página de inventario"


def test_agregar_al_carrito(driver_logged):
    inventory_page = InventoryPage(driver_logged)

    # Corregido: El método vive en la página de inventario
    inventory_page.agregar_al_carrito()
    cantidad = inventory_page.obtener_contador_carrito()
    assert cantidad == "1", f"Se esperaba 1 producto en el carrito, pero dice: {cantidad}"


def test_navegacion_al_carrito(driver_logged):
    inventory_page = InventoryPage(driver_logged)

    # Guarda el nombre del producto desde la página
    nombre_esperado = inventory_page.obtener_nombre_primer_producto()
    
    # Hace clic en el icono usando el método de la página
    inventory_page.ir_al_carrito()
    
    # Para la URL sí le preguntamos directo al navegador (driver_logged)
    assert "/cart.html" in driver_logged.current_url, "No se redireccionó a la pantalla del carrito"
    