# Semana 14 - Componentes y contenedores

## Información del Estudiante
**Nombre Completo:** Octavio Manuel Alvarez Cedeño

## Descripción del Sistema

Proyecto de interfaz gráfica para `restaurante_app` usando Tkinter. Se mantiene la arquitectura modular con modelos, servicios, archivos JSON y una capa `ui/` para las vistas. La aplicación conserva el flujo de inicio de sesión y evoluciona la interfaz principal incorporando componentes, contenedores, formularios y áreas de visualización para gestionar productos de manera clara y ordenada.

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

- `modelos/producto.py`: clase `Producto` con código, nombre, categoría, precio y stock.
- `modelos/usuario.py`: clase `Usuario` con identificación, nombre, correo y contraseña para la validación de acceso.
- `servicios/archivo_servicio.py`: acceso y persistencia de los archivos JSON (`productos.json` y `usuarios.json`).
- `servicios/restaurante_servicio.py`: administración de la lógica del negocio, validación de acceso y operaciones sobre productos.
- `ui/login_view.py`: vista de inicio con usuario y contraseña.
- `ui/main_view.py`: panel principal con contenedores, formulario de productos, tabla/listado y consulta de usuarios.
- `main.py`: crea la ventana principal y alterna entre login y panel general del restaurante.

## Flujo de la aplicación

1. `main.py` prepara la ventana principal y crea `RestauranteServicio`.
2. Se muestra `LoginView`.
3. El usuario ingresa credenciales.
4. `RestauranteServicio.validar_acceso()` valida la información.
5. Si es correcta, se muestra `MainView`.
6. El usuario puede navegar entre la sección de usuarios y la gestión de productos.
7. Los productos pueden registrarse, consultarse, actualizarse y eliminarse mediante botones.
8. Cada operación se procesa en `RestauranteServicio` y se guarda en `productos.json`.
9. La interfaz se actualiza para reflejar el estado actual del sistema.

## Excepciones controladas

- `FileNotFoundError`: si no existe un archivo JSON, el sistema inicia con una colección vacía.
- `json.JSONDecodeError`: si el contenido del JSON no es válido.
- `KeyError` / `ValueError`: los registros inválidos se omiten o se rechazan sin detener la aplicación.

## Cómo ejecutar

1. Abrir la terminal en `PARCIAL_2/SEMANA_14/restaurante_app`.
2. Ejecutar:

```bash
python main.py
```

3. Ingresar una de las credenciales disponibles en `usuarios.json`:
   - Usuario: `admin` / Contraseña: `1234`
   - Usuario: `mesero` / Contraseña: `4321`

## Validaciones implementadas

- Login con credenciales válidas.
- Mensaje visual si el usuario o la contraseña están vacíos.
- Mensaje visual si las credenciales son incorrectas.
- Consulta de usuarios desde la vista principal.
- Formulario organizado para productos con contenedores.
- Registro de un nuevo producto.
- Carga de un producto por código.
- Actualización de datos de un producto existente.
- Eliminación de un producto.
- Persistencia en `productos.json` después de cada operación.
- Actualización automática de la interfaz tras cada cambio.

## Reflexión breve

Esta etapa se centra en aplicar correctamente los conceptos de componentes y contenedores de Tkinter. La mejora principal es la organización visual de la aplicación, separando las áreas de navegación, formularios y presentación de información, mientras se conserva la lógica de negocio en servicios y la persistencia por archivos JSON.

---

**Fecha de entrega:** Semana 14 - Programación Orientada a Objetos
