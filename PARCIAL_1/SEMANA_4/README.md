# Sistema básico de gestión de Restaurante (POO - Python)

Alumno: Octavio Manuel Alvarez Cedeño

Descripción breve:

Este proyecto implementa un sistema educativo y sencillo para gestionar los elementos básicos de un restaurante: productos (platos y bebidas), clientes y la lógica para crear pedidos y calcular totales. Está pensado para demostrar buenas prácticas de organización mediante módulos y separación de responsabilidades en POO.

Este repositorio contiene un desarrollo educativo que demuestra cómo organizar un proyecto en módulos usando Programación Orientada a Objetos (POO) en Python. El ejemplo modela un sistema simple de restaurante con entidades mínimas: Producto, Cliente y un servicio Restaurante que administra productos, clientes y pedidos.

Estructura del proyecto (ubicación dentro de `SEMANA_4`)

restaurante_app/
├── __init__.py
├── modelos/
│   ├── __init__.py
│   ├── producto.py      # Clase Producto
│   └── cliente.py       # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py   # Clase Restaurante (lógica del sistema)
└── main.py              # Punto de entrada que demuestra uso


Descripción de los modelos

- modelos/producto.py
  - Clase: Producto
  - Atributos: id, nombre, tipo (plato/bebida), precio, descripcion
  - Métodos: `aplicar_descuento(porcentaje)` para ajustar el precio y `__str__()` para representación legible.

- modelos/cliente.py
  - Clase: Cliente
  - Atributos: id, nombre, telefono (opcional), mesa (opcional), pedidos (lista)
  - Métodos: `agregar_pedido(lista_productos)` para registrar pedidos; `monto_total()` para sumar lo gastado; `__str__()`.

Lógica del servicio

- servicios/restaurante.py
  - Clase: Restaurante
  - Responsabilidades:
    - Registrar y listar productos y clientes
    - Buscar productos por id o nombre y clientes por id
    - Crear pedidos asociando un cliente con una lista de ids de productos
    - Mostrar pedidos de un cliente con detalle y total gastado

Punto de entrada (demostración)

- main.py crea una instancia de `Restaurante`, registra varios `Producto` y `Cliente`, crea pedidos y muestra por consola los productos, totales y detalles de pedidos.

Cómo ejecutar (PowerShell / Windows)

1. Abrir PowerShell y ubicarse en la carpeta `SEMANA_4/restaurante_app`:

```powershell
cd "D:\PERSONAL_OA\UNIVERSIDAD\2do SEMESTRE\PROGRAMACION ORIENTADA A OBJETOS\PYTHON\2626-poo-alvarez-octavio\PARCIAL_1\SEMANA_4\restaurante_app"
python main.py
```

Nota: si `python` no está disponible en PATH, instale Python 3.8+ desde python.org y recuerde marcar la opción de agregar a PATH.

Alternativa (ejecutar como paquete desde la raíz del repo):

```powershell
cd "D:\PERSONAL_OA\UNIVERSIDAD\2do SEMESTRE\PROGRAMACION ORIENTADA A OBJETOS\PYTHON\2626-poo-alvarez-octavio\PARCIAL_1\SEMANA_4"
python -m restaurante_app.main
```

Salida esperada (resumen)

- Listado de productos con su precio y descripción
- Totales de los pedidos creados en la demostración
- Listado de clientes y detalle de sus pedidos, con el total gastado por cliente

Buenas prácticas y observaciones

- Las clases incluyen el método especial `__str__` para representar objetos de forma legible en consola.
- Las importaciones están organizadas por paquetes (`modelos`, `servicios`) para separar responsabilidades.
- El ejemplo es intencionalmente sencillo para centrarse en la organización y las relaciones entre clases; puede ampliarse agregando una clase `Pedido`, persistencia (archivo/BD) o una capa de interfaz.

Posibles mejoras futuras

- Añadir pruebas unitarias con `pytest` para verificar comportamiento de clases y servicios.
- Implementar una clase `Pedido` para modelar pedidos como entidades propias (con estado, fecha, etc.).
- Añadir persistencia (JSON/SQLite) para conservar datos entre ejecuciones.

Comandos para subir a GitHub (ejemplo desde `SEMANA_4`)

```powershell
cd "D:\PERSONAL_OA\UNIVERSIDAD\2do SEMESTRE\PROGRAMACION ORIENTADA A OBJETOS\PYTHON\2626-poo-alvarez-octavio\PARCIAL_1\SEMANA_4"
git add restaurante_app -A
git commit -m "Agregar sistema restaurante_app: modelos, servicios y main"
git push origin main
```

Contacto / Créditos

Desarrollado como actividad de curso para demostrar organización de proyectos con POO en Python.

Reflexión sobre la importancia de modularizar y separar responsabilidades

Modularizar el software y separar responsabilidades permite construir proyectos más mantenibles, testeables y comprensibles. Al dividir el código en modelos (que representan entidades) y servicios (que contienen la lógica de negocio), se facilita la localización de errores, la reutilización de componentes y la colaboración entre desarrolladores. Incluso en ejercicios pequeños, aplicar esta organización ayuda a escalar el sistema en el futuro y a incorporar mejoras (persistencia, pruebas, interfaces) sin romper las partes ya funcionales.

