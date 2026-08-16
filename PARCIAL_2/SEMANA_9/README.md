# Sistema de Restaurante - Semana 9

## Información del Estudiante
**Nombre Completo:** Octavio Manuel Alvarez Cedeño

## Descripción del Sistema

Proyecto "restaurante_app" que administra productos y usuarios de un restaurante desde la consola. Esta versión mantiene separación entre modelos, servicios y el punto de entrada (main.py), y evidencia el uso funcional de listas, tuplas, diccionarios y conjuntos.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

## Responsabilidad de cada módulo

- `modelos/producto.py`: Clase `Producto` (codigo, nombre, categoria, precio). Contiene métodos para representación y actualización.
- `modelos/usuario.py`: Clase `Usuario` (identificacion, nombre, correo).
- `servicios/restaurante.py`: Clase `Restaurante` que administra las colecciones (listas) de productos y usuarios y provee operaciones: registrar, buscar, actualizar, eliminar y listar.
- `main.py`: Interacción por consola y menú. Solicita datos con `input()` y usa los métodos del servicio; no modifica directamente las listas internas.

## Estructuras de datos usadas y su propósito

- list: Se utiliza para almacenar las colecciones dinámicas `productos` y `usuarios` en `Restaurante` (registro, actualización, eliminación y listado).
- tuple: `MENU_OPTIONS` en `main.py` contiene las opciones del menú; es inmutable y representa información estable durante la ejecución.
- dict: `MENU_FUNCIONES` en `main.py` asocia claves (opciones) a funciones que ejecutan cada acción (clave → valor), facilitando el enrutamiento del menú.
- set: El método `categorias_unicas()` en `Restaurante` devuelve un `set` con las categorías de productos sin duplicados para mostrar valores únicos.

## Menú de referencia

```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
----------------------------------------
6. Registrar usuario
7. Listar usuarios
----------------------------------------
8. Mostrar categorías
9. Salir
```

## Cómo ejecutar

1. Abrir terminal en la carpeta `PARCIAL_2/SEMANA_9/restaurante_app`.
2. Ejecutar:

```bash
python main.py
```

## Validaciones implementadas (resumen)

- Evitar códigos de producto duplicados al registrar.
- Evitar identificaciones de usuario duplicadas al registrar.
- Manejo de entradas inválidas (conversión de precio a `float`, campos obligatorios) con control de excepciones para no detener la aplicación.

## Reflexión breve

Escoger la estructura de datos adecuada simplifica la solución: las listas permiten colecciones dinámicas, las tuplas aseguran estabilidad en configuraciones, los diccionarios facilitan el mapeo de opciones a acciones y los conjuntos eliminan duplicados cuando se requiere unicidad.

---

**Fecha de entrega:** Semana 9 - Programación Orientada a Objetos
