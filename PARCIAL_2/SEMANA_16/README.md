# Semana 16 - Manejo de eventos en Tkinter

## Información del Estudiante

**Nombre Completo:** Octavio Manuel Alvarez Cedeño

## Descripción del Sistema

Esta versión continúa `restaurante_app` desde la Semana 15. Conserva el inicio de sesión, la gestión de productos, el registro de ventas y la persistencia JSON, y amplía la sección de Usuarios para aplicar eventos de Tkinter.

El Administrador puede registrar, consultar, actualizar y eliminar usuarios con roles de Empleado o Cliente. La vista usa un formulario y un `Treeview`; las contraseñas no se muestran en la tabla. Los eventos capturan la selección de filas, el cambio de rol y los atajos de teclado, mientras `RestauranteServicio` conserva las validaciones y la persistencia.

## Estructura del Proyecto

```text
restaurante_app/
├── assets/
│   ├── icon_add.png
│   ├── icon_clear.png
│   ├── icon_delete.png
│   ├── icon_load.png
│   ├── icon_logout.png
│   ├── icon_products.png
│   ├── icon_sales.png
│   ├── icon_update.png
│   ├── icon_users.png
│   └── logo.png
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
```

## Responsabilidad de cada módulo

- `modelos/usuario.py`: representa usuarios, valida sus datos y roles, y convierte los objetos a/desde diccionarios JSON. Los roles contemplados son Administrador, Empleado y Cliente.
- `servicios/archivo_servicio.py`: centraliza la lectura y escritura de `productos.json`, `usuarios.json` y `ventas.json`.
- `servicios/restaurante_servicio.py`: carga las entidades y concentra las reglas del restaurante. Valida el rol del administrador y ejecuta las operaciones de usuarios, productos y ventas.
- `ui/login_view.py`: presenta el formulario de acceso y entrega el objeto del usuario autenticado a la aplicación.
- `ui/main_view.py`: presenta navegación, productos, usuarios y ventas; asocia botones y eventos de Tkinter con callbacks.
- `assets/`: contiene el logotipo y los iconos utilizados por la ventana y los botones de navegación y acciones.
- `main.py`: crea una única ventana Tkinter, los servicios y las vistas, y coordina el inicio y cierre de sesión.

## Gestión de usuarios y roles

La tabla presenta identificación/usuario, nombre, correo y rol. No presenta contraseñas. El Administrador puede crear, actualizar y eliminar cuentas de Empleado y Cliente; no puede crear ni eliminar cuentas Administrador desde este formulario. La cuenta administrativa autenticada tampoco se puede eliminar ni degradar por accidente.

Al actualizar un usuario, dejar vacía la contraseña conserva la contraseña actual. Al seleccionar una fila, su identificación queda bloqueada para evitar cambiar accidentalmente la clave de búsqueda del registro.

## Eventos implementados

| Interacción | Mecanismo | Respuesta |
|---|---|---|
| Seleccionar una fila del `Treeview` | `bind("<<TreeviewSelect>>", callback)` | Obtiene el identificador de la fila, consulta el objeto mediante `RestauranteServicio.buscar_usuario()` y carga los datos en el formulario. |
| Presionar Enter desde los campos del formulario | `bind("<Return>", callback)` | Reutiliza `registrar_usuario()` para registrar sin duplicar la lógica. |
| Presionar Escape desde la sección Usuarios | `bind("<Escape>", callback)` | Limpia el formulario y cancela la selección actual. |
| Cambiar el rol | `bind("<<ComboboxSelected>>", callback)` | Actualiza la descripción informativa del rol. |
| Pulsar Registrar, Actualizar, Eliminar o Limpiar | `command=callback` | Invoca la operación correspondiente; Eliminar solicita confirmación. |

Los callbacks recogen los valores de la interfaz y solicitan las operaciones al servicio. No leen ni escriben directamente los archivos JSON.

## Flujo de una operación

1. `main.py` carga el servicio y muestra el inicio de sesión.
2. `RestauranteServicio` valida las credenciales y entrega el usuario autenticado.
3. La vista principal oculta la opción Usuarios para Empleados y Clientes.
4. El Administrador abre Usuarios y registra, selecciona, actualiza o elimina una cuenta.
5. El evento o botón ejecuta su callback.
6. El callback solicita la operación a `RestauranteServicio`.
7. El servicio valida permisos y datos y solicita la persistencia a `ArchivoServicio`.
8. La vista actualiza el `Treeview` y comunica el resultado.

## Persistencia y compatibilidad

Los cambios de usuarios se guardan en `datos/usuarios.json` mediante `ArchivoServicio`. El campo `rol` se conserva junto con los demás datos. Para registros heredados sin rol, `Usuario.from_dict()` asigna Administrador a `admin`, Empleado a `mesero` y Cliente a las demás cuentas, evitando perder el acceso administrativo al migrar los datos de la Semana 15.

## Cómo ejecutar

1. Abrir una terminal en `PARCIAL_2/SEMANA_16/restaurante_app`.
2. Ejecutar:

```bash
py -3 main.py
```

En otros sistemas, se puede usar `python3 main.py`.

Credenciales de ejemplo incluidas en `datos/usuarios.json`:

- Administrador: usuario `admin`, contraseña `1234`.
- Empleado: usuario `mesero`, contraseña `4321`.
- Cliente: usuario `cliente`, contraseña `1111`.

El acceso es una simulación didáctica y no constituye autenticación segura para producción.

## Validaciones implementadas

- Registro con identificación no repetida, nombre, correo, contraseña y rol válidos.
- Restricción de las operaciones administrativas al rol Administrador, aplicada también en el servicio.
- Roles administrables limitados a Empleado y Cliente.
- Protección contra la eliminación o degradación de la cuenta administrativa activa.
- Confirmación visual antes de eliminar una cuenta.
- Persistencia de usuarios y recuperación al iniciar la aplicación.
- Actualización de la tabla después de registrar, actualizar o eliminar.

## Reflexión breve

La sección de Usuarios evidencia la diferencia entre `command=` y `bind()`: los botones ejecutan comandos directos, mientras que la tabla, el teclado y el `Combobox` responden a eventos específicos. La vista coordina la interacción y el servicio mantiene las reglas de negocio y el acceso a la persistencia.

---

**Fecha de entrega:** Semana 16 - Programación Orientada a Objetos
