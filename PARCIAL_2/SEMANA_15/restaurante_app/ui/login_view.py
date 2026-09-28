import tkinter as tk
from tkinter import ttk


class LoginView(ttk.Frame):
    def __init__(self, parent: tk.Misc, restaurante_servicio, on_login) -> None:
        super().__init__(parent)
        self.restaurante_servicio = restaurante_servicio
        self.on_login = on_login
        self.configure(padding=30)

        self.columnconfigure(0, weight=1)

        title = ttk.Label(self, text="Sistema de Restaurante", font=("Segoe UI", 20, "bold"))
        title.grid(row=0, column=0, pady=(0, 10), sticky="ew")

        subtitle = ttk.Label(self, text="Inicio de sesión", font=("Segoe UI", 12))
        subtitle.grid(row=1, column=0, pady=(0, 20), sticky="ew")

        form = ttk.Frame(self, padding=20)
        form.grid(row=2, column=0, sticky="nsew")
        form.columnconfigure(1, weight=1)

        ttk.Label(form, text="Usuario:").grid(row=0, column=0, sticky="w", padx=(0, 10), pady=(0, 8))
        self.usuario_var = tk.StringVar()
        self.usuario_entry = ttk.Entry(form, textvariable=self.usuario_var)
        self.usuario_entry.grid(row=0, column=1, sticky="ew", pady=(0, 8))

        ttk.Label(form, text="Contraseña:").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(0, 8))
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(form, textvariable=self.password_var, show="*")
        self.password_entry.grid(row=1, column=1, sticky="ew", pady=(0, 8))

        self.mensaje_var = tk.StringVar()
        self.mensaje_label = ttk.Label(form, textvariable=self.mensaje_var, foreground="red")
        self.mensaje_label.grid(row=2, column=0, columnspan=2, sticky="w", pady=(10, 0))

        ttk.Button(form, text="Ingresar", command=self.login).grid(row=3, column=0, columnspan=2, pady=(20, 0), sticky="ew")

    def login(self) -> None:
        usuario = self.usuario_var.get().strip()
        password = self.password_var.get().strip()

        if not usuario or not password:
            self.mensaje_var.set("Debe ingresar usuario y contraseña.")
            return

        if self.restaurante_servicio.validar_acceso(usuario, password):
            self.mensaje_var.set("")
            self.usuario_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.on_login()
            return

        self.mensaje_var.set("Credenciales incorrectas.")
