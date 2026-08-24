# Sistema de Restaurante - Semana 10

## Información del Estudiante
**Nombre Completo:** Octavio Manuel Alvarez Cedeño

## Descripción del Sistema

Evolución del proyecto "restaurante_app" con persistencia de productos en formato JSON. Mantiene la organización modular (modelos, servicios y main) y añade servicios/archivo_servicio.py para concentrar la lectura y escritura de datos en datos/productos.json. El resto del sistema continúa trabajando con objetos Producto durante la ejecución.

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── tests/
    ├── __init__.py
    └── test_persistence.py
```

## Responsabilidad de cada módulo

- `modelos/producto.py`: Clase `Producto` con validaciones, método `to_dict()` para serializar y `from_dict()` para reconstruir objetos desde registros JSON. Mantiene la lógica de validación de datos.
- `modelos/usuario.py`: Clase `Usuario` (información en memoria; no se persiste en esta actividad).
- `servicios/archivo_servicio.py`: Encapsula la lectura y escritura del archivo `datos/productos.json` usando `with open()`, `json.load()` y `json.dump()`. Controla FileNotFoundError, json.JSONDecodeError y propaga PermissionError cuando corresponde.
- `servicios/restaurante.py`: Lógica de negocio para administrar colecciones de `Producto` y `Usuario` (registrar, buscar, actualizar, eliminar, listar). Acepta una lista inicial de objetos `Producto` al construirse.
- `main.py`: Punto de entrada. Coordina la carga inicial de productos desde JSON, la interacción por consola (input) y solicita al `ArchivoServicio` el guardado cuando se modifican los productos.
- `tests/test_persistence.py`: Pruebas unitarias simples que verifican guardar y cargar productos y el manejo de JSON inválido.

## Estructuras de datos usadas y su propósito

- list: almacena las colecciones dinámicas `productos` y `usuarios` en `Restaurante`.
- tuple: `MENU_OPTIONS` en `main.py` contiene las opciones del menú (inmutable).
- dict: `MENU_FUNCIONES` en `main.py` asocia opciones a funciones; objetos `Producto` se serializan a diccionarios para JSON.
- set: `categorias_unicas()` devuelve categorías únicas sin duplicados.

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

## Flujo de persistencia (resumen)

1. Al iniciar, `main.py` crea `ArchivoServicio` y solicita `cargar()`.
2. Si el archivo existe y contiene una lista válida, cada registro se convierte en `Producto.from_dict()` y se entrega a `Restaurante`.
3. Si el archivo no existe, se inicia con lista vacía.
4. Cuando se registra, actualiza o elimina un producto, `main.py` solicita al servicio que guarde la colección actualizada convirtiendo cada `Producto` a diccionario y llamando a `ArchivoServicio.guardar()`.

## Excepciones controladas (implementadas)

- FileNotFoundError: permite iniciar sin `productos.json` (colección vacía).
- json.JSONDecodeError: detecta contenido no válido en el archivo y evita detener la aplicación; los registros inválidos se omiten con aviso.
- PermissionError: se informa si no hay permisos para leer o escribir el archivo.
- KeyError / ValueError: al reconstruir productos, registros incompletos o con datos inválidos son omitidos y detallados al usuario.

## Cómo ejecutar

1. Abrir terminal en la carpeta `PARCIAL_2/SEMANA_10/restaurante_app`.
2. Ejecutar:

```bash
python main.py
```

## Tests (unidad)

Se incluyeron pruebas básicas en `tests/test_persistence.py`.
Ejecutar desde la carpeta `restaurante_app`:

```bash
python -m unittest discover -v
```

## Validaciones implementadas (resumen)

- Evitar códigos de producto duplicados al registrar.
- Validar campos obligatorios y tipo de `precio` (no negativo).
- Manejo controlado de errores de archivo y formato JSON para no detener la aplicación.

## Reflexión breve

Agregar persistencia mediante JSON refuerza la separación de responsabilidades: el servicio de archivo se encarga exclusivamente de I/O, `Restaurante` gestiona la lógica del dominio y `Producto` conserva sus validaciones. Esto facilita pruebas y mantenimiento.

---

**Fecha de entrega:** Semana 10 - Programación Orientada a Objetos
