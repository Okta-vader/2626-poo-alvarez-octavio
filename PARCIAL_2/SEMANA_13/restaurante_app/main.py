from __future__ import annotations
import os
import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class App:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Sistema de Restaurante")
        self.root.geometry("900x520")

        base_dir = os.path.join(os.path.dirname(__file__), "datos")
        self.restaurante_servicio = RestauranteServicio(base_dir)

        self.login_view = LoginView(self.root, self.restaurante_servicio, self.mostrar_main_view)
        self.main_view = MainView(self.root, self.restaurante_servicio, self.mostrar_login_view)

        self.mostrar_login_view()

    def mostrar_login_view(self) -> None:
        self.main_view.pack_forget()
        self.login_view.pack(fill="both", expand=True)
        self.root.title("Sistema de Restaurante - Login")

    def mostrar_main_view(self) -> None:
        self.login_view.pack_forget()
        self.main_view.pack(fill="both", expand=True)
        self.root.title("Sistema de Restaurante - Panel principal")


def main() -> None:
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
