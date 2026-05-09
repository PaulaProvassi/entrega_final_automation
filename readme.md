# Proyecto de Automatizacion QA - Paula Provassi

## Descripcion

Proyecto de automatizacion de pruebas realizado con Python, Selenium WebDriver y Pytest.

El objetivo del proyecto es automatizas distintas pruebas funcionales de una aplicación web.

## Tecnologias utilizadas
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Git

## Instalacion
git clone []
cd pre_entrega

## Instalacion de dependencias
pip3 install selenium pytest pytest-html

## Funcionamiento de las pruebas
- Test Login: Verifica el acceso correcto con credenciales válidas.

- Test Inventory: Comprueba que, tras el login, el catálogo de productos sea visible, el título sea correcto ("Products") y los elementos de la interfaz (menú y filtros) estén presentes.

- Test Cart: Valida la interacción con el carrito, asegurando que al añadir un producto el contador se incremente y el ítem aparezca en la lista de compras.

## Cómo ejecutar las pruebas
python3 -m pytest