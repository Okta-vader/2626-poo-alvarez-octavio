# Sistema de Restaurante - Semana 12

## Información del Estudiante
**Nombre Completo:** Octavio Manuel Alvarez Cedeño

## Descripción del Sistema

Mejora de rendimiento sobre la versión de la Semana 11 mediante índices en memoria (diccionarios) para búsquedas frecuentes por clave única (código de producto e identificación de usuario). Las colecciones principales (listas) se conservan para persistencia y recorrido; los índices se mantienen sincronizados al registrar, modificar o eliminar registros.

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

## Mejoras realizadas (resumen)

- Se añadieron índices en memoria:
  - `productos_por_codigo: dict[codigo, Producto]` para búsquedas rápidas de productos por código.
  - `usuarios_por_id: dict[id, Usuario]` para búsquedas rápidas de usuarios por identificación.
  - `ventas_por_usuario: dict[id, list[Venta]]` para consultar las ventas de un usuario sin recorrer toda la lista de ventas.
- Las listas principales (`productos`, `usuarios`, `_ventas`) se mantienen para persistencia y operaciones que requieren recorrido.
- Los índices se reconstruyen al iniciar la aplicación a partir de los objetos recuperados desde JSON y se actualizan al registrar/eliminar/vender.

## Cómo afecta al rendimiento

Las búsquedas por código o identificación pasan de O(n) a O(1) amortizado, evitando recorridos completos de listas cuando se conoce la clave única.

## Cómo ejecutar

1. Abrir terminal en `PARCIAL_2/SEMANA_12/restaurante_app`.
2. Ejecutar:

```bash
python main.py
```

## Tests

Pruebas unitarias en `restaurante_app/tests/test_indices.py` verifican la sincronización de índices, la operación de venta y la actualización de stock.
Ejecutar desde la carpeta `restaurante_app`:

```bash
python -m unittest discover -v
```

## Notas

- Se mantuvo la organización modular y las validaciones de las clases del dominio.
- No se reemplazaron las colecciones principales por índices; estos últimos son auxiliares y se mantienen sincronizados.

---

**Fecha de entrega:** Semana 12 - Programación Orientada a Objetos
