# Sistema de Restaurante - Semana 13

## Información del Estudiante
**Nombre Completo:** Octavio Manuel Alvarez Cedeño

## Descripción del Sistema

Proyecto base de interfaz gráfica para `restaurante_app` usando Tkinter. Se mantiene la arquitectura modular con modelos, servicios, archivos JSON y una capa `ui/` para las vistas. La aplicación funciona como una simulación de acceso al sistema y permite mostrar productos y usuarios registrados desde la interfaz principal.

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## Responsabilidad de cada módulo

- `modelos/producto.py`: clase `Producto` con atributos de código, nombre, categoría, precio y stock.
- `modelos/usuario.py`: clase `Usuario` con identificación, nombre, correo y contraseña para la simulación de acceso.
- `servicios/archivo_servicio.py`: acceso a archivos JSON (`productos.json` y `usuarios.json`).
- `servicios/restaurante_servicio.py`: administración de la información del restaurante, validación de acceso y listado de productos/usuarios.
- `ui/login_view.py`: pantalla de inicio con usuario y contraseña.
- `ui/main_view.py`: panel principal con opciones para consultar productos y usuarios y botón para cerrar sesión.
- `main.py`: crea la ventana principal, prepara dependencias y alterna entre la vista de login y la vista principal.

## Flujo de la aplicación

1. `main.py` prepara la ventana principal y crea `RestauranteServicio`.
2. Se muestra `LoginView`.
3. El usuario ingresa credenciales.
4. `RestauranteServicio.validar_acceso()` valida la información.
5. Si es correcta, se oculta la vista de login y se muestra `MainView`.
6. La ventana principal permite consultar productos y usuarios.
7. El botón de cerrar sesión regresa al login dentro de la misma ventana.

## Excepciones controladas

- FileNotFoundError: si no existe el archivo JSON, se inicia con una colección vacía.
- json.JSONDecodeError: si el contenido del archivo no es válido.
- KeyError / ValueError: los registros inválidos se omiten sin detener la aplicación.

## Cómo ejecutar

1. Abrir la terminal en `PARCIAL_2/SEMANA_13/restaurante_app`.
2. Ejecutar:

```bash
python main.py
```

## Validaciones implementadas

- Login con credenciales válidas.
- Mensaje visual si el usuario o la contraseña están vacíos.
- Mensaje visual si las credenciales son incorrectas.
- Visualización de productos y usuarios desde la vista principal.
- Opción `Ventas (pendiente)` identificada como funcionalidad futura.

## Reflexión breve

Esta etapa se centra en la base gráfica del sistema: una ventana principal, una vista de acceso y los servicios que gestionan la información. La estructura modular permite que, en futuras semanas, se agreguen más funcionalidades sin romper la organización del proyecto.

---

**Fecha de entrega:** Semana 13 - Programación Orientada a Objetos
