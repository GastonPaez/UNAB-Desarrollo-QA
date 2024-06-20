### UNAB - DESARROLLO DE SOFTWARE
### GRUPO 7 - QA

#### Pruebas con Selenium en Python

- [x] Prueba automatica de Busqueda y navegacion de productos encontrados
- [x] Prueba automatica de navegacion por categorias 
- [x] Prueba automatica sobre carrito
- [x] Prueba de Login con credenciales correctas y erroneas

#### Pagina testeada: **https://opencart.abstracta.us**

| Número | Tipo de Prueba     | Escenario                         | Acción                                                                                           | Resultado Esperado                                             | Resultado                                 |
|--------|------------|-------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------|
| 1    | Prueba Automática con Selenium  | Búsqueda y navegación de productos encontrados       | Ingresar "mac" en el campo del buscador y presionar buscar. Luego ingresar y poder visualizar cada uno de los productos encontrados.                                                                 | Obtener de resultado los 4 productos mac y poder ingresar en cada uno de ellos sin problema                                       | Se realiza la búsqueda con resultado de 4 elementos. Se ingresa en cada uno de ellos de manera exitosa |
| 2      | Prueba Automática con Selenium                          | Navegación panel de categorías, visualizar productos y poder incorporarlos al carrito de compras.     | Ingresar en cada categoría y sub categoría añadiendo un producto de cada una de ellas al carrito de compras.                              | Se debe poder ingresar y visualizar cada una de las categorías y subcategorías ingresadas y en el caso de que existan productos agregar uno al carrito de compras. Con cada categoría. | Se navega por las categorías, se ingresa en cada categoría y en caso de que no encuentre productos, ingresa en la siguiente sub categoría añadiendo al producto encontrado al carrito de compras.
| 3      |Prueba Automática con Selenium| Prueba de login                          |Dirigirse a al navbar, solapa de my account, e ingresar en Login. Ingresar "aargento@mail.com" en el campo E-Mail Address e ingresar “Prueba1234” en el campo Password. Presionar botón Login.                   | Debe ingresar en una nueva vista con la cuenta del usuario                                      | Se bloquea la página y muestra advertencia de seguridad. Por falta de certificado SSL            |
| 4      |Prueba Automática con Selenium con Opción (--ignore-certificate-errors)  | Prueba de login con credencial exitosa     | Dirigirse a al navbar, solapa de my account, e ingresar en Login. Ingresar "aargento@mail.com" en el campo E-Mail Address e ingresar "Prueba1234" en el campo Password. Presionar botón Login.                                                            | Debe ingresar en una nueva vista con la cuenta del usuario                                       | Se realiza el login exitoso y se ingresa en el panel My Account del usuario ingresado |
| 5      |Prueba Automática con Selenium  con Opción (--ignore-certificate-errors)  | Prueba de login con credencial errónea     | Dirigirse a al navbar, solapa de my account, e ingresar en Login. Ingresar "mail@mail.com" en el campo E-Mail Address e ingresar "Prueba1234" en el campo Password. Presionar botón Login.                                                            | Debe permanecer en la misma vista y mostrar mensaje de error.                                       | Muestra mensaje de error:  Warning: No match for E-Mail Address and/or Password. |

***
