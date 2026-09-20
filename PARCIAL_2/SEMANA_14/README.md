# Semana 14 - Componentes y contenedores en Tkinter

## Descripción
Esta entrega corresponde a la Semana 14 de la asignatura Programación Orientada a Objetos. El proyecto mantiene la arquitectura modular del sistema `restaurante_app`, pero mejora la capa visual incorporando componentes, contenedores y formularios para gestionar productos de una forma más clara y ordenada.

## Estructura del proyecto

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

## Mejoras implementadas
- Se conserva el inicio de sesión con validación basada en `RestauranteServicio`.
- La interfaz principal se organiza con contenedores para separar navegación y contenido.
- Se incorpora un formulario para registrar, consultar, actualizar y eliminar productos.
- Se mantiene la información de usuarios disponible en una vista de consulta.
- Las operaciones de negocio quedan dentro del servicio y no en la capa visual.
- La persistencia continúa en archivos JSON con los datos del restaurante.

## Componentes y contenedores usados
- `ttk.Frame` para estructurar los paneles.
- `ttk.LabelFrame` para agrupar formularios y listados.
- `ttk.Entry` para capturar información del producto.
- `ttk.Button` para ejecutar acciones mediante `command=`.
- `ttk.Treeview` para visualizar los registros de productos.
- `tk.Text` para mostrar al usuario la información de usuarios.

## Operaciones de productos implementadas
- Registrar producto.
- Cargar producto por código.
- Actualizar información del producto.
- Eliminar producto.
- Mostrar el listado actualizado en la interfaz.

## Persistencia
La información de productos y usuarios se guarda en archivos JSON dentro de la carpeta `datos/`. El servicio encargado de manipular archivos valida y guarda los cambios de forma centralizada.

## Cómo ejecutar
1. Abrir una terminal en la carpeta `PARCIAL_2/SEMANA_14/restaurante_app`.
2. Ejecutar:

```bash
python main.py
```

3. Ingresar una de las credenciales disponibles en `usuarios.json`:
   - Usuario: `admin` / Contraseña: `1234`
   - Usuario: `mesero` / Contraseña: `4321`

## Observación
La lógica de negocio y validaciones se mantienen encapsuladas en `RestauranteServicio`, mientras que la interfaz se encarga de coordinar la interacción con el usuario.
