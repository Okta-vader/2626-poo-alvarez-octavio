import os
import tkinter as tk
from tkinter import messagebox, ttk


class MainView(ttk.Frame):
    def __init__(self, parent: tk.Misc, restaurante_servicio, on_logout, usuario_actual) -> None:
        super().__init__(parent, padding=15)
        self.restaurante_servicio = restaurante_servicio
        self.on_logout = on_logout
        self.usuario_actual = usuario_actual
        self.actor_id = usuario_actual.identificacion
        self.es_admin = usuario_actual.rol == "Administrador"
        self.seleccion_usuario_id: str | None = None
        self.configure(padding=15)

        assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
        icon_names = {
            "add": "icon_add.png",
            "load": "icon_load.png",
            "update": "icon_update.png",
            "delete": "icon_delete.png",
            "clear": "icon_clear.png",
            "users": "icon_users.png",
            "products": "icon_products.png",
            "sales": "icon_sales.png",
            "logout": "icon_logout.png",
            "logo": "logo.png",
        }
        self._icons = {
            key: tk.PhotoImage(file=os.path.join(assets_dir, filename))
            for key, filename in icon_names.items()
        }

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        sidebar = ttk.Frame(self, padding=12)
        sidebar.grid(row=0, column=0, sticky="ns", padx=(0, 15))
        sidebar.columnconfigure(0, weight=1)
        ttk.Label(sidebar, image=self._icons["logo"]).grid(row=0, column=0, pady=(0, 8))
        ttk.Label(sidebar, text="Menú", font=("Segoe UI", 14, "bold")).grid(
            row=1, column=0, sticky="ew", pady=(0, 15)
        )

        self.btn_productos = self._nav_button(sidebar, "Productos", "products", self.mostrar_productos)
        self.btn_productos.grid(row=2, column=0, sticky="ew", pady=4)
        self.btn_usuarios = self._nav_button(sidebar, "Usuarios", "users", self.mostrar_usuarios)
        self.btn_usuarios.grid(row=3, column=0, sticky="ew", pady=4)
        self.btn_ventas = self._nav_button(sidebar, "Ventas", "sales", self.mostrar_ventas)
        self.btn_ventas.grid(row=4, column=0, sticky="ew", pady=4)
        self.btn_logout = self._nav_button(sidebar, "Cerrar sesión", "logout", self.on_logout)
        self.btn_logout.grid(row=5, column=0, sticky="ew", pady=(12, 0))
        if not self.es_admin:
            self.btn_usuarios.grid_remove()

        self.content = ttk.Frame(self)
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.columnconfigure(0, weight=1)
        self.content.rowconfigure(1, weight=1)
        header = ttk.Frame(self.content)
        header.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        header.columnconfigure(0, weight=1)
        self.title_var = tk.StringVar(value="Gestión de productos")
        ttk.Label(header, textvariable=self.title_var, font=("Segoe UI", 18, "bold")).grid(
            row=0, column=0, sticky="w"
        )
        ttk.Label(header, text=f"{usuario_actual.nombre} · {usuario_actual.rol}").grid(
            row=0, column=1, sticky="e"
        )

        self._crear_panel_productos()
        self._crear_panel_usuarios()
        self._crear_panel_ventas()
        self.mostrar_productos()

    def _nav_button(self, parent, text: str, icon: str, command) -> ttk.Button:
        return ttk.Button(parent, text=text, image=self._icons[icon], compound="left", command=command)

    def _crear_panel_productos(self) -> None:
        self.product_panel = ttk.Frame(self.content)
        self.product_panel.columnconfigure(0, weight=1)
        self.product_panel.rowconfigure(1, weight=1)

        form = ttk.LabelFrame(self.product_panel, text="Formulario de producto", padding=12)
        form.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        form.columnconfigure(1, weight=1)
        self.codigo_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.categoria_var = tk.StringVar()
        self.precio_var = tk.StringVar()
        self.stock_var = tk.StringVar()
        product_fields = (
            ("Código:", self.codigo_var),
            ("Nombre:", self.nombre_var),
            ("Categoría:", self.categoria_var),
            ("Precio:", self.precio_var),
            ("Stock:", self.stock_var),
        )
        for row, (label, variable) in enumerate(product_fields):
            ttk.Label(form, text=label).grid(row=row, column=0, sticky="w", padx=(0, 10), pady=4)
            ttk.Entry(form, textvariable=variable).grid(row=row, column=1, sticky="ew", pady=4)

        actions = ttk.Frame(form)
        actions.grid(row=len(product_fields), column=0, columnspan=2, sticky="w", pady=(10, 0))
        product_buttons = (
            ("Registrar", "add", self.registrar_producto),
            ("Cargar", "load", self.cargar_producto),
            ("Actualizar", "update", self.actualizar_producto),
            ("Eliminar", "delete", self.eliminar_producto),
            ("Limpiar", "clear", self.limpiar_formulario_producto),
        )
        for text, icon, command in product_buttons:
            ttk.Button(actions, text=text, image=self._icons[icon], compound="left", command=command).pack(
                side="left", padx=(0, 7)
            )

        table = ttk.LabelFrame(self.product_panel, text="Productos registrados", padding=10)
        table.grid(row=1, column=0, sticky="nsew")
        table.columnconfigure(0, weight=1)
        table.rowconfigure(0, weight=1)
        columns = ("codigo", "nombre", "categoria", "precio", "stock")
        self.product_tree = ttk.Treeview(table, columns=columns, show="headings")
        for column, label, width in (
            ("codigo", "Código", 90),
            ("nombre", "Nombre", 180),
            ("categoria", "Categoría", 150),
            ("precio", "Precio", 90),
            ("stock", "Stock", 80),
        ):
            self.product_tree.heading(column, text=label)
            self.product_tree.column(column, width=width, anchor="center" if column in {"codigo", "precio", "stock"} else "w")
        self.product_tree.grid(row=0, column=0, sticky="nsew")

    def _crear_panel_usuarios(self) -> None:
        self.user_panel = ttk.Frame(self.content)
        self.user_panel.columnconfigure(0, weight=1)
        self.user_panel.columnconfigure(1, weight=2)
        self.user_panel.rowconfigure(0, weight=1)

        form = ttk.LabelFrame(self.user_panel, text="Datos del usuario", padding=12)
        form.grid(row=0, column=0, sticky="new", padx=(0, 12))
        form.columnconfigure(1, weight=1)
        self.usuario_id_var = tk.StringVar()
        self.usuario_nombre_var = tk.StringVar()
        self.usuario_correo_var = tk.StringVar()
        self.usuario_password_var = tk.StringVar()
        self.usuario_rol_var = tk.StringVar(value="Cliente")
        self.rol_info_var = tk.StringVar(value="Cliente: cuenta de usuario del restaurante.")

        ttk.Label(form, text="Usuario / ID:").grid(row=0, column=0, sticky="w", padx=(0, 8), pady=5)
        self.usuario_id_entry = ttk.Entry(form, textvariable=self.usuario_id_var)
        self.usuario_id_entry.grid(row=0, column=1, sticky="ew", pady=5)
        ttk.Label(form, text="Nombre:").grid(row=1, column=0, sticky="w", padx=(0, 8), pady=5)
        self.usuario_nombre_entry = ttk.Entry(form, textvariable=self.usuario_nombre_var)
        self.usuario_nombre_entry.grid(row=1, column=1, sticky="ew", pady=5)
        ttk.Label(form, text="Correo:").grid(row=2, column=0, sticky="w", padx=(0, 8), pady=5)
        self.usuario_correo_entry = ttk.Entry(form, textvariable=self.usuario_correo_var)
        self.usuario_correo_entry.grid(row=2, column=1, sticky="ew", pady=5)
        ttk.Label(form, text="Contraseña:").grid(row=3, column=0, sticky="w", padx=(0, 8), pady=5)
        self.usuario_password_entry = ttk.Entry(form, textvariable=self.usuario_password_var, show="*")
        self.usuario_password_entry.grid(row=3, column=1, sticky="ew", pady=5)
        ttk.Label(form, text="Rol:").grid(row=4, column=0, sticky="w", padx=(0, 8), pady=5)
        self.usuario_rol_combo = ttk.Combobox(
            form,
            textvariable=self.usuario_rol_var,
            values=("Administrador", "Empleado", "Cliente"),
            state="readonly",
        )
        self.usuario_rol_combo.grid(row=4, column=1, sticky="ew", pady=5)
        self.usuario_rol_combo.bind("<<ComboboxSelected>>", self._al_seleccionar_rol)
        ttk.Label(form, textvariable=self.rol_info_var, wraplength=260).grid(
            row=5, column=0, columnspan=2, sticky="w", pady=(4, 8)
        )
        ttk.Label(form, text="Deje la contraseña vacía al actualizar para conservarla.", wraplength=260).grid(
            row=6, column=0, columnspan=2, sticky="w", pady=(0, 8)
        )

        actions = ttk.Frame(form)
        actions.grid(row=7, column=0, columnspan=2, sticky="ew", pady=(8, 0))
        for text, icon, command in (
            ("Registrar", "add", self.registrar_usuario),
            ("Actualizar", "update", self.actualizar_usuario),
            ("Eliminar", "delete", self.eliminar_usuario),
            ("Limpiar", "clear", self.limpiar_formulario_usuario),
        ):
            ttk.Button(actions, text=text, image=self._icons[icon], compound="left", command=command).pack(
                fill="x", pady=3
            )

        table_frame = ttk.LabelFrame(self.user_panel, text="Usuarios registrados", padding=10)
        table_frame.grid(row=0, column=1, sticky="nsew")
        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)
        columns = ("identificacion", "nombre", "correo", "rol")
        self.user_tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=16)
        for column, label, width in (
            ("identificacion", "Usuario / ID", 120),
            ("nombre", "Nombre", 160),
            ("correo", "Correo", 200),
            ("rol", "Rol", 110),
        ):
            self.user_tree.heading(column, text=label)
            self.user_tree.column(column, width=width, anchor="w")
        self.user_tree.grid(row=0, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.user_tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.user_tree.configure(yscrollcommand=scrollbar.set)
        self.user_tree.bind("<<TreeviewSelect>>", self._al_seleccionar_usuario)

        event_widgets = (
            self.usuario_id_entry,
            self.usuario_nombre_entry,
            self.usuario_correo_entry,
            self.usuario_password_entry,
            self.usuario_rol_combo,
            self.user_tree,
        )
        for widget in event_widgets:
            widget.bind("<Return>", self._al_presionar_enter)
            widget.bind("<Escape>", self._al_presionar_escape)

    def _crear_panel_ventas(self) -> None:
        self.sales_panel = ttk.Frame(self.content)
        self.sales_panel.columnconfigure(0, weight=1)
        self.sales_panel.rowconfigure(1, weight=1)
        form = ttk.LabelFrame(self.sales_panel, text="Registrar venta", padding=12)
        form.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        form.columnconfigure(1, weight=1)

        ttk.Label(form, text="Usuario:").grid(row=0, column=0, sticky="w", padx=(0, 10), pady=5)
        self.venta_usuario_var = tk.StringVar()
        self.venta_usuario_cb = ttk.Combobox(form, textvariable=self.venta_usuario_var, state="readonly")
        self.venta_usuario_cb.grid(row=0, column=1, sticky="ew", pady=5)
        ttk.Label(form, text="Producto (código):").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=5)
        self.venta_producto_var = tk.StringVar()
        self.venta_producto_cb = ttk.Combobox(form, textvariable=self.venta_producto_var, state="readonly")
        self.venta_producto_cb.grid(row=1, column=1, sticky="ew", pady=5)
        ttk.Label(form, text="Cantidad:").grid(row=2, column=0, sticky="w", padx=(0, 10), pady=5)
        self.venta_cantidad_var = tk.StringVar(value="1")
        ttk.Entry(form, textvariable=self.venta_cantidad_var).grid(row=2, column=1, sticky="ew", pady=5)
        ttk.Button(
            form,
            text="Registrar venta",
            image=self._icons["add"],
            compound="left",
            command=self.registrar_venta,
        ).grid(row=3, column=0, columnspan=2, pady=(10, 0), sticky="ew")

        table = ttk.LabelFrame(self.sales_panel, text="Ventas registradas", padding=10)
        table.grid(row=1, column=0, sticky="nsew")
        table.columnconfigure(0, weight=1)
        table.rowconfigure(0, weight=1)
        columns = ("fecha", "usuario", "producto", "cantidad")
        self.sales_tree = ttk.Treeview(table, columns=columns, show="headings")
        for column, label, width in (
            ("fecha", "Fecha", 180),
            ("usuario", "Usuario", 130),
            ("producto", "Producto", 140),
            ("cantidad", "Cantidad", 90),
        ):
            self.sales_tree.heading(column, text=label)
            self.sales_tree.column(column, width=width)
        self.sales_tree.grid(row=0, column=0, sticky="nsew")

    def _actualizar_tabla_productos(self) -> None:
        self.product_tree.delete(*self.product_tree.get_children())
        for producto in self.restaurante_servicio.listar_productos():
            self.product_tree.insert(
                "", tk.END, values=(
                    producto.codigo, producto.nombre, producto.categoria,
                    f"{producto.precio:.2f}", producto.stock,
                )
            )

    def _actualizar_tabla_usuarios(self) -> None:
        self.user_tree.delete(*self.user_tree.get_children())
        for usuario in self.restaurante_servicio.listar_usuarios():
            self.user_tree.insert(
                "", tk.END,
                values=(usuario.identificacion, usuario.nombre, usuario.correo, usuario.rol),
            )

    def _actualizar_tabla_ventas(self) -> None:
        self.sales_tree.delete(*self.sales_tree.get_children())
        for venta in self.restaurante_servicio.listar_ventas():
            self.sales_tree.insert(
                "", tk.END,
                values=(venta.fecha, venta.usuario_id, venta.producto_codigo, venta.cantidad),
            )

    def limpiar_formulario_producto(self) -> None:
        for variable in (self.codigo_var, self.nombre_var, self.categoria_var, self.precio_var, self.stock_var):
            variable.set("")

    def registrar_producto(self) -> None:
        try:
            codigo = self.codigo_var.get().strip()
            nombre = self.nombre_var.get().strip()
            categoria = self.categoria_var.get().strip()
            precio = self.precio_var.get().strip()
            stock = self.stock_var.get().strip()
            if not all((codigo, nombre, categoria, precio, stock)):
                raise ValueError("Debe completar todos los campos del producto.")
            self.restaurante_servicio.registrar_producto(codigo, nombre, categoria, float(precio), int(stock))
            self._actualizar_tabla_productos()
            self.limpiar_formulario_producto()
            messagebox.showinfo("Registro completado", "El producto fue registrado correctamente.")
        except ValueError as exc:
            messagebox.showerror("Error de validación", str(exc))

    def cargar_producto(self) -> None:
        codigo = self.codigo_var.get().strip()
        if not codigo:
            messagebox.showerror("Error", "Debe ingresar el código del producto a cargar.")
            return
        producto = self.restaurante_servicio.buscar_producto(codigo)
        if producto is None:
            messagebox.showerror("No encontrado", f"No existe el producto con código '{codigo}'.")
            return
        self.codigo_var.set(producto.codigo)
        self.nombre_var.set(producto.nombre)
        self.categoria_var.set(producto.categoria)
        self.precio_var.set(str(producto.precio))
        self.stock_var.set(str(producto.stock))

    def actualizar_producto(self) -> None:
        try:
            codigo = self.codigo_var.get().strip()
            if not codigo:
                raise ValueError("Debe ingresar el código del producto a actualizar.")
            precio = self.precio_var.get().strip()
            stock = self.stock_var.get().strip()
            self.restaurante_servicio.actualizar_producto(
                codigo, self.nombre_var.get().strip() or None,
                self.categoria_var.get().strip() or None,
                float(precio) if precio else None, int(stock) if stock else None,
            )
            self._actualizar_tabla_productos()
            messagebox.showinfo("Actualización completada", "El producto fue actualizado correctamente.")
        except ValueError as exc:
            messagebox.showerror("Error de validación", str(exc))

    def eliminar_producto(self) -> None:
        codigo = self.codigo_var.get().strip()
        if not codigo:
            messagebox.showerror("Error", "Debe ingresar el código del producto a eliminar.")
            return
        try:
            self.restaurante_servicio.eliminar_producto(codigo)
            self._actualizar_tabla_productos()
            self.limpiar_formulario_producto()
            messagebox.showinfo("Producto eliminado", f"Se eliminó el producto '{codigo}'.")
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))

    def limpiar_formulario_usuario(self) -> None:
        self.seleccion_usuario_id = None
        self.user_tree.selection_remove(self.user_tree.selection())
        self.usuario_id_entry.configure(state="normal")
        self.usuario_id_var.set("")
        self.usuario_nombre_var.set("")
        self.usuario_correo_var.set("")
        self.usuario_password_var.set("")
        self.usuario_rol_var.set("Cliente")
        self._al_seleccionar_rol()
        self.usuario_id_entry.focus_set()

    def _al_seleccionar_usuario(self, _event: tk.Event) -> None:
        selected = self.user_tree.selection()
        if not selected:
            return
        values = self.user_tree.item(selected[0], "values")
        if not values:
            return
        usuario = self.restaurante_servicio.buscar_usuario(values[0])
        if usuario is None:
            messagebox.showerror("Usuario no encontrado", "El registro seleccionado ya no está disponible.")
            self._actualizar_tabla_usuarios()
            return
        self.seleccion_usuario_id = usuario.identificacion
        self.usuario_id_var.set(usuario.identificacion)
        self.usuario_id_entry.configure(state="readonly")
        self.usuario_nombre_var.set(usuario.nombre)
        self.usuario_correo_var.set(usuario.correo)
        self.usuario_password_var.set("")
        self.usuario_rol_var.set(usuario.rol)
        self._al_seleccionar_rol()

    def _al_seleccionar_rol(self, _event: tk.Event | None = None) -> None:
        descripciones = {
            "Administrador": "Administrador: acceso administrativo a la gestión de usuarios.",
            "Empleado": "Empleado: usuario del equipo del restaurante.",
            "Cliente": "Cliente: cuenta de cliente del restaurante.",
        }
        self.rol_info_var.set(descripciones.get(self.usuario_rol_var.get(), "Seleccione un rol."))

    def _al_presionar_enter(self, _event: tk.Event) -> str:
        self.registrar_usuario()
        return "break"

    def _al_presionar_escape(self, _event: tk.Event) -> str:
        self.limpiar_formulario_usuario()
        return "break"

    def registrar_usuario(self) -> None:
        try:
            usuario = self.restaurante_servicio.registrar_usuario(
                self.usuario_id_var.get(),
                self.usuario_nombre_var.get(),
                self.usuario_correo_var.get(),
                self.usuario_password_var.get(),
                self.usuario_rol_var.get(),
                self.actor_id,
            )
            self._actualizar_tabla_usuarios()
            self.limpiar_formulario_usuario()
            messagebox.showinfo("Usuario registrado", f"Se registró a {usuario.nombre} correctamente.")
        except (ValueError, PermissionError) as exc:
            messagebox.showerror("No se pudo registrar", str(exc))

    def actualizar_usuario(self) -> None:
        if not self.seleccion_usuario_id:
            messagebox.showerror("Seleccione un usuario", "Seleccione una fila de la tabla para actualizar.")
            return
        try:
            usuario = self.restaurante_servicio.actualizar_usuario(
                self.seleccion_usuario_id,
                self.usuario_nombre_var.get(),
                self.usuario_correo_var.get(),
                self.usuario_password_var.get(),
                self.usuario_rol_var.get(),
                self.actor_id,
            )
            self._actualizar_tabla_usuarios()
            self.limpiar_formulario_usuario()
            messagebox.showinfo("Usuario actualizado", f"Se actualizaron los datos de {usuario.nombre}.")
        except (ValueError, PermissionError) as exc:
            messagebox.showerror("No se pudo actualizar", str(exc))

    def eliminar_usuario(self) -> None:
        if not self.seleccion_usuario_id:
            messagebox.showerror("Seleccione un usuario", "Seleccione una fila de la tabla para eliminar.")
            return
        if not messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Desea eliminar el usuario '{self.seleccion_usuario_id}'?",
        ):
            return
        try:
            usuario = self.restaurante_servicio.eliminar_usuario(self.seleccion_usuario_id, self.actor_id)
            self._actualizar_tabla_usuarios()
            self.limpiar_formulario_usuario()
            messagebox.showinfo("Usuario eliminado", f"Se eliminó a {usuario.nombre}.")
        except (ValueError, PermissionError) as exc:
            messagebox.showerror("No se pudo eliminar", str(exc))

    def registrar_venta(self) -> None:
        usuario_id = self.venta_usuario_var.get().strip()
        producto_codigo = self.venta_producto_var.get().strip()
        cantidad = self.venta_cantidad_var.get().strip()
        if not usuario_id or not producto_codigo or not cantidad:
            messagebox.showerror("Error", "Debe seleccionar usuario, producto y cantidad.")
            return
        try:
            venta = self.restaurante_servicio.registrar_venta(usuario_id, producto_codigo, int(cantidad))
            self._actualizar_tabla_ventas()
            self._actualizar_tabla_productos()
            messagebox.showinfo("Venta registrada", f"Venta registrada: {venta}")
        except ValueError as exc:
            messagebox.showerror("Error al registrar venta", str(exc))

    def mostrar_productos(self) -> None:
        self.title_var.set("Gestión de productos")
        self.user_panel.grid_remove()
        self.sales_panel.grid_remove()
        self.product_panel.grid(row=1, column=0, sticky="nsew")
        self._actualizar_tabla_productos()

    def mostrar_usuarios(self) -> None:
        if not self.restaurante_servicio.es_administrador(self.actor_id):
            messagebox.showerror("Acceso restringido", "Solo el Administrador puede gestionar usuarios.")
            return
        self.title_var.set("Gestión de usuarios")
        self.product_panel.grid_remove()
        self.sales_panel.grid_remove()
        self.user_panel.grid(row=1, column=0, sticky="nsew")
        self._actualizar_tabla_usuarios()

    def mostrar_ventas(self) -> None:
        self.title_var.set("Registro de ventas")
        self.product_panel.grid_remove()
        self.user_panel.grid_remove()
        self.sales_panel.grid(row=1, column=0, sticky="nsew")
        self.venta_usuario_cb["values"] = [
            usuario.identificacion for usuario in self.restaurante_servicio.listar_usuarios()
        ]
        self.venta_producto_cb["values"] = [
            producto.codigo for producto in self.restaurante_servicio.listar_productos()
        ]
        self._actualizar_tabla_ventas()
