# Sistema de Restaurante - Semana 11

## Información del Estudiante
**Nombre Completo:** Octavio Manuel Alvarez Cedeño

## Descripción del Sistema

Evolución del proyecto "restaurante_app" que añade persistencia para productos, usuarios y ventas, y una operación de venta que relaciona usuarios con productos y controla el stock disponible. Mantiene la organización modular y el flujo de carga/guardado en JSON.

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

## Responsabilidad de cada módulo

- `modelos/producto.py`: Clase `Producto` con stock, validaciones, `to_dict()` y `from_dict()`.
- `modelos/usuario.py`: Clase `Usuario` con validaciones y métodos de serialización.
- `modelos/venta.py`: Clase `Venta` que relaciona `usuario_id`, `producto_codigo` y `cantidad`, con registro de fecha.
- `servicios/archivo_servicio.py`: Lectura/escritura centralizada para productos, usuarios y ventas.
- `servicios/restaurante.py`: Lógica de negocio: registrar, buscar, actualizar, eliminar, vender y consultar ventas por usuario.
- `main.py`: Punto de entrada, carga inicial, menú y guardado tras operaciones.

## Flujo de venta (resumen)

1. main solicita identificación, producto y cantidad.
2. Restaurante valida existencia de usuario y producto, cantidad válida y stock suficiente.
3. Se crea `Venta` y se agrega a la colección.
4. Se decrementa `stock` del `Producto`.
5. Se guardan `ventas.json` y `productos.json`.

## Excepciones controladas

- FileNotFoundError: iniciar con colecciones vacías si no existen archivos.
- json.JSONDecodeError: manejar archivos con JSON inválido.
- PermissionError: informar si no hay permisos de lectura/escritura.
- KeyError / ValueError: omitir registros inválidos al reconstruir objetos.

## Cómo ejecutar

1. Abrir terminal en `PARCIAL_2/SEMANA_11` o en `PARCIAL_2/SEMANA_11/restaurante_app`.
2. Ejecutar:

```bash
python main.py
```

## Tests

Pruebas unitarias básicas en `restaurante_app/tests/test_sales.py` verifican la operación de venta, el stock y la persistencia de productos y ventas.
Ejecutar desde la carpeta `restaurante_app`:

```bash
python -m unittest discover -v
```

## Validaciones y restricciones

- No permitir ventas con cantidad inválida ni que dejen stock negativo.
- No registrar ventas si usuario o producto no existen.
- Mantener modelos como objetos del dominio (no usar diccionarios como sustitutos).

---

**Fecha de entrega:** Semana 11 - Programación Orientada a Objetos
