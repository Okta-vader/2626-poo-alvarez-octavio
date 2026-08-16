NOMBRE: Octavio Manuel Alvarez Cedeño

Descripción
Proyecto "restaurante_app" que administra productos y usuarios de un restaurante desde consola.

Estructura del proyecto
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py

Responsabilidades
- modelos/producto.py: clase Producto (codigo, nombre, categoria, precio).
- modelos/usuario.py: clase Usuario (identificación, nombre, correo).
- servicios/restaurante.py: clase Restaurante administra listas de productos y usuarios.
- main.py: interacción por consola y menú.

Estructuras de datos usadas
- list: para almacenar colecciones dinámicas (productos y usuarios) en Restaurante.
- tuple: MENU_OPTIONS en main.py contiene las opciones del menú y se mantiene inmutable.
- dict: MENU_FUNCIONES asocia la opción seleccionada (clave) con la función que la procesa (valor).
- set: categorias_unicas en Restaurante devuelve categorías únicas de productos sin duplicados.

Ejecución
Desde el directorio restaurante_app ejecutar:
python main.py

Reflexión
Seleccionar la estructura de datos adecuada mejora claridad, rendimiento y evita errores como duplicados o modificaciones accidentales. Aquí cada estructura cumple un propósito real en el flujo del programa.
