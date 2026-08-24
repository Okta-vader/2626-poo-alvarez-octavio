Semana 10 - restaurante_app (persistencia JSON)

Autor: Octavio Manuel Alvarez Cedeño

Este proyecto es la evolución del restaurante_app de semanas anteriores. Se añadió persistencia de productos en datos/productos.json mediante servicios/archivo_servicio.py.

Archivos principales:
- restaurante_app/
  - datos/productos.json  (archivo de persistencia)
  - modelos/producto.py   (clase Producto con to_dict y from_dict y validaciones)
  - modelos/usuario.py
  - servicios/archivo_servicio.py (lectura y escritura JSON)
  - servicios/restaurante.py (lógica del negocio)
  - main.py (punto de entrada, carga y guardado de productos)

Tests:
- restaurante_app/tests/test_persistence.py  (pruebas unitarias con unittest)
  Ejecutar desde la carpeta restaurante_app: python -m unittest discover -v

Ejecución:
1. Desde la carpeta restaurante_app ejecutar: python main.py
2. Registrar / actualizar / eliminar productos. El archivo datos/productos.json se actualizará.

Excepciones controladas:
- FileNotFoundError: si no existe productos.json, se inicia con lista vacía.
- json.JSONDecodeError: si el archivo contiene JSON inválido, se anuncia y se inicia con vacío cuando corresponde.
- PermissionError: si no hay permisos al leer/escribir, se informa al usuario.
- KeyError / ValueError: registros incompletos o inválidos son omitidos con aviso.

Prueba mínima de persistencia:
1. Ejecutar main.py
2. Registrar productos
3. Cerrar y volver a ejecutar: los productos deben persistir

Autor: Octavio Manuel Alvarez Cedeño
