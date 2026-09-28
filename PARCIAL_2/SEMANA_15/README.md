Restaurante App - Semana 15

Autor: Octavio Manuel Alvarez Cedeño

Objetivo de la entrega
Esta versión demuestra los conceptos fundamentales de manejo de eventos: una acción del usuario en la interfaz (botón) desencadena un callback que solicita a RestauranteServicio el registro de una venta, se valida la operación, se persiste en JSON y la interfaz muestra la respuesta. Mantiene la arquitectura modular trabajada en semanas previas (datos, modelos, servicios, ui y main.py).

Cambios y archivos importantes
- modelos/venta.py: nuevo modelo Venta (to_dict / from_dict) que registra usuario, producto, cantidad y fecha.
- datos/ventas.json: almacenamiento persistente de las ventas.
- servicios/archivo_servicio.py: métodos cargar_ventas() y guardar_ventas().
- servicios/restaurante_servicio.py: carga y lista de ventas; método registrar_venta(usuario_id, producto_codigo, cantidad) que valida usuario, producto, stock; reduce stock; persiste productos y ventas.
- ui/main_view.py: nueva sección "Ventas" con combobox para usuario y producto, campo cantidad, botón "Registrar venta" (usa command= y callback), y Treeview con las ventas registradas.
- assets/: carpeta creada para logo e íconos (colocar logo.png, icon.ico si se desea).

Estructura del proyecto
restaurante_app/
├── assets/                 # recursos visuales (logo, iconos)
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
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
└── main.py

Responsabilidades por módulo (resumen)
- modelos/producto.py: validaciones del dominio, to_dict()/from_dict().
- modelos/usuario.py: representación y serialización de usuarios.
- modelos/venta.py: representación de una venta y su serialización.
- servicios/archivo_servicio.py: lectura/escritura de JSON (productos, usuarios, ventas) usando with open, json.load/json.dump.
- servicios/restaurante_servicio.py: toda la lógica de negocio (registro/consulta/actualización/eliminación de productos, validación de acceso y registro de ventas). Las vistas llaman a este servicio, no acceden a archivos directamente.
- ui/: vistas con Tkinter/ttk. LoginView controla el acceso; MainView presenta Productos, Usuarios y Ventas.

Flujo mínimo (ejemplo de venta)
1. Usuario inicia la aplicación (main.py) → LoginView aparece.
2. El usuario ingresa credenciales (simuladas) y pulsa Ingresar.
3. LoginView delega la validación a RestauranteServicio.
4. Al ingresar correctamente, MainView se muestra.
5. El usuario abre la sección Ventas, selecciona Usuario y Producto (combobox), ingresa Cantidad y pulsa "Registrar venta".
6. El botón usa command= para ejecutar el callback registrar_venta() en MainView.
7. El callback solicita a RestauranteServicio.registrar_venta(usuario_id, producto_codigo, cantidad).
8. RestauranteServicio valida existencia y stock; si OK, reduce stock, crea Venta, persiste productos.json y ventas.json.
9. MainView actualiza la tabla de ventas y la tabla de productos para mostrar los cambios.

Comprobaciones y pruebas manuales recomendadas
- Ejecutar la app: desde la carpeta que contiene main.py ejecutar:
  - Windows: py -3 -m restaurante_app.main
  - Linux/Mac: python3 -m restaurante_app.main
- Login: usar usuarios en datos/usuarios.json (por defecto: admin/1234 y mesero/4321).
- Productos: comprobar que productos.json contenga productos iniciales y que la tabla los muestre.
- Registrar venta:
  - Seleccionar usuario y producto en Ventas, indicar cantidad y pulsar "Registrar venta".
  - Verificar que sales appear in datos/ventas.json and that productos.json stock decreased.
  - Reabrir la aplicación y confirmar que ventas y productos se cargan correctamente.
- Validaciones: probar cantidades mayores al stock, usuario o producto inexistente; la interfaz debe mostrar mensajes de error claros.

Notas técnicas y consideraciones
- La autenticación es pedagógica y no debe usarse en producción.
- Las vistas no escriben ni leen archivos JSON directamente; todo pasa por RestauranteServicio y ArchivoServicio.
- Los mensajes de error están gestionados con messagebox para feedback al usuario.
- Para mejorar la apariencia sustituir assets/logo.txt por un PNG y ajustar la ventana en main.py.

Ejecución rápida (resumen):
1. Abrir terminal en: PARCIAL_2/SEMANA_15/restaurante_app
2. Ejecutar: py -3 -m restaurante_app.main

Autor y contacto
Octavio Manuel Alvarez Cedeño

Última nota
Este README sigue el mismo formato y nivel de detalle utilizado en la semana anterior; documenta la evolución a Semana 15 centrada en eventos y ventas. Actualizar si se incorporan más funcionalidades posteriormente.