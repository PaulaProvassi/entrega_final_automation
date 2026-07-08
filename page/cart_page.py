from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
       

        # Locators
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.cart_items_name = (By.CLASS_NAME, "inventory_item_name")
        self.cart_items_price = (By.CLASS_NAME, "inventory_item_price")


    def obtener_productos_carrito(self):
        items = self.driver.find_elements(*self.cart_items)
       
        productos_carrito = []

        for item in items:
            nombre_item = item.find_element(*self.cart_items_name).text
            precio_item = item.find_element(*self.cart_items_price).text
       
            productos_carrito.append(
                   { 
                      "nombre": nombre_item, 
                     "precio": precio_item
                   }
            )
            
        return productos_carrito