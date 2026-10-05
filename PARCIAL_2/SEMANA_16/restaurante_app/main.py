from __future__ import annotations

import os
import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

# Estructura del proyecto (árbol)
# ```
# restaurante_app/
# ├── assets/
# │   ├── icon_*.png
# │   └── logo.png
# ├── datos/
# │   ├── productos.json
# │   ├── usuarios.json
# │   └── ventas.json
# ├── modelos/
# │   ├── __init__.py
# │   ├── producto.py
# │   ├── usuario.py
# │   └── venta.py
# ├── servicios/
# │   ├── __init__.py
# │   ├── archivo_servicio.py
# │   └── restaurante_servicio.py
# ├── ui/
# │   ├── __init__.py
# │   ├── login_view.py
# │   └── main_view.py
# └── main.py
# ```


class App:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Sistema de Restaurante")
        self.root.geometry("1100x650")
        self.root.minsize(900, 550)

        # Intentar cargar logo y establecer icono de la ventana
        assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets"))
        logo_path = os.path.join(assets_dir, "logo.png")
        self._logo_img = None
        try:
            self._logo_img = tk.PhotoImage(file=logo_path)
            self.root.iconphoto(True, self._logo_img)
        except Exception:
            # si no existe el logo, continuar sin icono
            self._logo_img = None

        base_dir = os.path.join(os.path.dirname(__file__), "datos")
        self.restaurante_servicio = RestauranteServicio(base_dir)

        self.login_view = LoginView(self.root, self.restaurante_servicio, self.mostrar_main_view)
        self.main_view = None
        self.usuario_actual = None

        self.mostrar_login_view()

    def mostrar_login_view(self) -> None:
        if self.main_view is not None:
            self.main_view.destroy()
            self.main_view = None
        self.usuario_actual = None
        self.login_view.pack(fill="both", expand=True)
        self.root.title("Sistema de Restaurante - Login")

    def mostrar_main_view(self, usuario_actual) -> None:
        self.usuario_actual = usuario_actual
        self.login_view.pack_forget()
        self.main_view = MainView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_login_view,
            usuario_actual,
        )
        self.main_view.pack(fill="both", expand=True)
        self.root.title("Sistema de Restaurante - Panel principal")


def main() -> None:
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
