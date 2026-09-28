Restaurante App - Semana 15

Autor: Octavio Manuel Alvarez Cedeño

Resumen:
Versión que incorpora manejo básico de eventos: registro de ventas desde la interfaz.
Se mantiene la arquitectura modular (modelos, servicios, ui, datos) y la persistencia JSON.

Cambios principales:
- Se agregó el modelo Venta (modelos/venta.py) y datos/ventas.json
- ArchivoServicio ahora lee/guarda ventas (servicios/archivo_servicio.py)
- RestauranteServicio registra ventas (validación de usuario/producto, control de stock)
  y persiste ventas y productos.
- MainView incorpora la sección Ventas con selección de usuario/producto y botón "Registrar venta".
- Carpeta assets/ creada para logo e íconos (reemplazar logo.txt por logo.png si se desea).

Ejecución:
1. Abrir terminal en esta carpeta
2. Ejecutar: python -m restaurante_app.main

Nota: la autenticación es simulada (usuarios en datos/usuarios.json).