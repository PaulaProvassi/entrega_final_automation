from selenium import webdriver

def before_scenario(context, scenario):
    # Abre el navegador antes de cada escenario
    context.driver = webdriver.Chrome() 
    context.driver.maximize_window()

def after_scenario(context, scenario):
    # Cierra el navegador después de cada escenario
    context.driver.quit()

