import tkinter as tk
from tkinter import ttk

class LoginView(ttk.Frame):
    def __init__(self, parent: tk.Misc, restaurante_servicio, on_login) -> None:
        super().__init__(parent)
        self.restaurante_servicio = restaurante_servicio
        self.on_login = on_login

        self.configure(padding=20)

        tk.Label(self, text="Sistema de Restaurante", font=("Arial", 18, "bold")).pack(pady=(0, 20))
        tk.Label(self, text="Iniciar sesión", font=("Arial", 12)).pack(pady=(0, 10))

        tk.Label(self, text="Usuario:").pack(anchor="w")
        self.usuario_var = tk.StringVar()
        self.usuario_entry = tk.Entry(self, textvariable=self.usuario_var, width=30)
        self.usuario_entry.pack(pady=(0, 10), fill="x")

        tk.Label(self, text="Contraseña:").pack(anchor="w")
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(self, textvariable=self.password_var, width=30, show="*")
        self.password_entry.pack(pady=(0, 10), fill="x")

        self.mensaje_var = tk.StringVar()
        self.mensaje_label = tk.Label(self, textvariable=self.mensaje_var, fg="red", wraplength=300)
        self.mensaje_label.pack(pady=(0, 10))

        tk.Button(self, text="Ingresar", command=self.login, width=20).pack(pady=(10, 0))

    def login(self) -> None:
        usuario = self.usuario_var.get().strip()
        password = self.password_var.get().strip()

        if not usuario or not password:
            self.mensaje_var.set("Debe ingresar usuario y contraseña.")
            return

        if self.restaurante_servicio.validar_acceso(usuario, password):
            self.mensaje_var.set("")
            self.on_login()
            return

        self.mensaje_var.set("Credenciales incorrectas.")
