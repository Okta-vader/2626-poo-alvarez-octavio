import tkinter as tk
from tkinter import messagebox, ttk


class MainView(ttk.Frame):
    def __init__(self, parent: tk.Misc, restaurante_servicio, on_logout) -> None:
        super().__init__(parent)
        self.restaurante_servicio = restaurante_servicio
        self.on_logout = on_logout
        self.configure(padding=15)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        sidebar = ttk.Frame(self, padding=12)
        sidebar.grid(row=0, column=0, sticky="ns", padx=(0, 15))
        sidebar.columnconfigure(0, weight=1)

        ttk.Label(sidebar, text="Menú", font=("Segoe UI", 14, "bold")).grid(row=0, column=0, sticky="ew", pady=(0, 15))

        self.btn_productos = ttk.Button(sidebar, text="Productos", command=self.mostrar_productos)
        self.btn_productos.grid(row=1, column=0, sticky="ew", pady=4)

        self.btn_usuarios = ttk.Button(sidebar, text="Usuarios", command=self.mostrar_usuarios)
        self.btn_usuarios.grid(row=2, column=0, sticky="ew", pady=4)

        self.btn_logout = ttk.Button(sidebar, text="Cerrar sesión", command=self.on_logout)
        self.btn_logout.grid(row=3, column=0, sticky="ew", pady=(12, 0))

        self.content = ttk.Frame(self)
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.columnconfigure(0, weight=1)
        self.content.rowconfigure(1, weight=1)

        self.title_var = tk.StringVar(value="Gestión de productos")
        ttk.Label(self.content, textvariable=self.title_var, font=("Segoe UI", 18, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 12))

        self.product_panel = ttk.Frame(self.content)
        self.product_panel.grid(row=1, column=0, sticky="nsew")
        self.product_panel.columnconfigure(0, weight=1)

        form_frame = ttk.LabelFrame(self.product_panel, text="Formulario de producto", padding=12)
        form_frame.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        form_frame.columnconfigure(1, weight=1)

        ttk.Label(form_frame, text="Código:").grid(row=0, column=0, sticky="w", padx=(0, 10), pady=5)
        self.codigo_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.codigo_var).grid(row=0, column=1, sticky="ew", pady=5)

        ttk.Label(form_frame, text="Nombre:").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=5)
        self.nombre_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.nombre_var).grid(row=1, column=1, sticky="ew", pady=5)

        ttk.Label(form_frame, text="Categoría:").grid(row=2, column=0, sticky="w", padx=(0, 10), pady=5)
        self.categoria_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.categoria_var).grid(row=2, column=1, sticky="ew", pady=5)

        ttk.Label(form_frame, text="Precio:").grid(row=3, column=0, sticky="w", padx=(0, 10), pady=5)
        self.precio_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.precio_var).grid(row=3, column=1, sticky="ew", pady=5)

        ttk.Label(form_frame, text="Stock:").grid(row=4, column=0, sticky="w", padx=(0, 10), pady=5)
        self.stock_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.stock_var).grid(row=4, column=1, sticky="ew", pady=5)

        action_row = ttk.Frame(form_frame)
        action_row.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(12, 0))
        for text, command in [
            ("Registrar", self.registrar_producto),
            ("Cargar", self.cargar_producto),
            ("Actualizar", self.actualizar_producto),
            ("Eliminar", self.eliminar_producto),
            ("Limpiar", self.limpiar_formulario),
        ]:
            ttk.Button(action_row, text=text, command=command).pack(side="left", padx=(0, 8))

        table_frame = ttk.LabelFrame(self.product_panel, text="Listado de productos", padding=(10, 10, 10, 0))
        table_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 10))
        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(table_frame, columns=("codigo", "nombre", "categoria", "precio", "stock"), show="headings")
        self.tree.heading("codigo", text="Código")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("categoria", text="Categoría")
        self.tree.heading("precio", text="Precio")
        self.tree.heading("stock", text="Stock")
        self.tree.column("codigo", width=80, anchor="center")
        self.tree.column("nombre", width=180)
        self.tree.column("categoria", width=140)
        self.tree.column("precio", width=90, anchor="center")
        self.tree.column("stock", width=80, anchor="center")
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.user_panel = ttk.Frame(self.content)
        self.user_panel.grid(row=1, column=0, sticky="nsew")
        self.user_panel.columnconfigure(0, weight=1)
        self.user_panel.rowconfigure(0, weight=1)

        self.user_text = tk.Text(self.user_panel, wrap="word", state="disabled", font=("Segoe UI", 10))
        self.user_text.grid(row=0, column=0, sticky="nsew")

        self.mostrar_productos()

    def limpiar_formulario(self) -> None:
        self.codigo_var.set("")
        self.nombre_var.set("")
        self.categoria_var.set("")
        self.precio_var.set("")
        self.stock_var.set("")

    def _actualizar_tabla_productos(self) -> None:
        for item in self.tree.get_children():
            self.tree.delete(item)

        for producto in self.restaurante_servicio.listar_productos():
            self.tree.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"{producto.precio:.2f}",
                    producto.stock,
                ),
            )

    def registrar_producto(self) -> None:
        try:
            codigo = self.codigo_var.get().strip()
            nombre = self.nombre_var.get().strip()
            categoria = self.categoria_var.get().strip()
            precio = self.precio_var.get().strip()
            stock = self.stock_var.get().strip()

            if not codigo or not nombre or not categoria or not precio or not stock:
                raise ValueError("Debe completar todos los campos del producto.")

            self.restaurante_servicio.registrar_producto(codigo, nombre, categoria, float(precio), int(stock))
            self._actualizar_tabla_productos()
            self.limpiar_formulario()
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
            nombre = self.nombre_var.get().strip()
            categoria = self.categoria_var.get().strip()
            precio = self.precio_var.get().strip()
            stock = self.stock_var.get().strip()

            if not codigo:
                raise ValueError("Debe ingresar el código del producto a actualizar.")

            self.restaurante_servicio.actualizar_producto(
                codigo,
                nombre=nombre or None,
                categoria=categoria or None,
                precio=float(precio) if precio else None,
                stock=int(stock) if stock else None,
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
            self.limpiar_formulario()
            messagebox.showinfo("Producto eliminado", f"Se eliminó el producto '{codigo}'.")
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))

    def mostrar_productos(self) -> None:
        self.title_var.set("Gestión de productos")
        self.product_panel.grid()
        self.user_panel.grid_remove()
        self._actualizar_tabla_productos()

    def mostrar_usuarios(self) -> None:
        self.title_var.set("Usuarios registrados")
        self.product_panel.grid_remove()
        self.user_panel.grid()
        self.user_text.configure(state="normal")
        self.user_text.delete("1.0", tk.END)
        usuarios = self.restaurante_servicio.listar_usuarios()
        if not usuarios:
            self.user_text.insert(tk.END, "No hay usuarios registrados.")
        else:
            for usuario in usuarios:
                self.user_text.insert(tk.END, f"- {usuario}\n")
        self.user_text.configure(state="disabled")
