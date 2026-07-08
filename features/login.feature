Feature: Inicio de sesion
    Background:
        Given que el usuario esta en la pagina de Login

    Scenario: Login exitoso
        When ingresa el usuario "standard_user" y la contraseña "secret_sauce"
        And hace clic en el boton Login
        Then deberia ingresar al inventario

    Scenario: Login invalido con contraseña incorrecta
        When ingresa el usuario "standard_user" y la contraseña "12345"
        And hace clic en el boton Login
        Then deberia ver el mensaje de error "Epic sadface: Username and password do not match any user in this service"