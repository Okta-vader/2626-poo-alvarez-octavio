import tkinter as tk
from tkinter import ttk

class MainView(ttk.Frame):
    def __init__(self, parent: tk.Misc, restaurante_servicio, on_logout) -> None:
        super().__init__(parent)
        self.restaurante_servicio = restaurante_servicio
        self.on_logout = on_logout

        self.configure(padding=20)

        header = tk.Label(self, text="Panel principal del restaurante", font=("Arial", 18, "bold"))
        header.pack(pady=(0, 15))

        btn_frame = tk.Frame(self)
        btn_frame.pack(fill="x", pady=(0, 10))

        tk.Button(btn_frame, text="Productos", command=self.mostrar_productos, width=18).pack(side="left", padx=(0, 10))
        tk.Button(btn_frame, text="Usuarios", command=self.mostrar_usuarios, width=18).pack(side="left", padx=(0, 10))
        tk.Button(btn_frame, text="Ventas (pendiente)", width=18, state="disabled").pack(side="left", padx=(0, 10))
        tk.Button(btn_frame, text="Cerrar sesión", command=self.on_logout, width=18, fg="red").pack(side="left")

        self.info_text = tk.Text(self, width=100, height=20, wrap="word")
        self.info_text.pack(fill="both", expand=True)

        self.mostrar_productos()

    def _set_text(self, title: str, items: list[str]) -> None:
        self.info_text.configure(state="normal")
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, f"{title}\n\n")
        if not items:
            self.info_text.insert(tk.END, "No hay información disponible.")
        else:
            for item in items:
                self.info_text.insert(tk.END, f"- {item}\n")
        self.info_text.configure(state="disabled")

    def mostrar_productos(self) -> None:
        productos = self.restaurante_servicio.listar_productos()
        if not productos:
            self._set_text("Productos registrados", [])
            return
        datos = [str(producto) for producto in productos]
        self._set_text("Productos registrados", datos)

    def mostrar_usuarios(self) -> None:
        usuarios = self.restaurante_servicio.listar_usuarios()
        if not usuarios:
            self._set_text("Usuarios registrados", [])
            return
        datos = [str(usuario) for usuario in usuarios]
        self._set_text("Usuarios registrados", datos)
