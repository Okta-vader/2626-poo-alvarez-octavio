import os
import tkinter as tk
from tkinter import ttk


class LoginView(ttk.Frame):
    def __init__(self, parent: tk.Misc, restaurante_servicio, on_login) -> None:
        super().__init__(parent, padding=30)
        self.restaurante_servicio = restaurante_servicio
        self.on_login = on_login
        self.columnconfigure(0, weight=1)

        assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
        self.logo_img = tk.PhotoImage(file=os.path.join(assets_dir, "logo.png"))
        ttk.Label(self, image=self.logo_img).grid(row=0, column=0, pady=(0, 10))
        ttk.Label(self, text="Sistema de Restaurante", font=("Segoe UI", 20, "bold")).grid(
            row=1, column=0, pady=(0, 10), sticky="ew"
        )
        ttk.Label(self, text="Inicio de sesión", font=("Segoe UI", 12)).grid(
            row=2, column=0, pady=(0, 20), sticky="ew"
        )

        form = ttk.LabelFrame(self, text="Acceso al sistema", padding=20)
        form.grid(row=3, column=0, sticky="ew", padx=80)
        form.columnconfigure(1, weight=1)

        ttk.Label(form, text="Usuario:").grid(row=0, column=0, sticky="w", padx=(0, 10), pady=6)
        self.usuario_var = tk.StringVar()
        self.usuario_entry = ttk.Entry(form, textvariable=self.usuario_var)
        self.usuario_entry.grid(row=0, column=1, sticky="ew", pady=6)

        ttk.Label(form, text="Contraseña:").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=6)
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(form, textvariable=self.password_var, show="*")
        self.password_entry.grid(row=1, column=1, sticky="ew", pady=6)

        self.mensaje_var = tk.StringVar()
        ttk.Label(form, textvariable=self.mensaje_var, foreground="red").grid(
            row=2, column=0, columnspan=2, sticky="w", pady=(8, 0)
        )
        ttk.Button(form, text="Ingresar", command=self.login).grid(
            row=3, column=0, columnspan=2, pady=(16, 0), sticky="ew"
        )
        self.usuario_entry.bind("<Return>", self._on_return)
        self.password_entry.bind("<Return>", self._on_return)

    def _on_return(self, _event: tk.Event) -> str:
        self.login()
        return "break"

    def login(self) -> None:
        identificacion = self.usuario_var.get().strip()
        password = self.password_var.get().strip()
        if not identificacion or not password:
            self.mensaje_var.set("Debe ingresar usuario y contraseña.")
            return
        if not self.restaurante_servicio.validar_acceso(identificacion, password):
            self.mensaje_var.set("Credenciales incorrectas.")
            return

        usuario = self.restaurante_servicio.buscar_usuario(identificacion)
        if usuario is None:
            self.mensaje_var.set("No se pudo cargar el usuario.")
            return
        self.mensaje_var.set("")
        self.usuario_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.on_login(usuario)
