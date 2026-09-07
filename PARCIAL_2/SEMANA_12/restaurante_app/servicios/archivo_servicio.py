import json
import os
from typing import List, Dict, Any

class ArchivoServicio:
    def __init__(self, base_dir: str) -> None:
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)
        self.productos_path = os.path.join(self.base_dir, "productos.json")
        self.usuarios_path = os.path.join(self.base_dir, "usuarios.json")
        self.ventas_path = os.path.join(self.base_dir, "ventas.json")

    def _cargar(self, ruta: str) -> List[Dict[str, Any]]:
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list):
                raise json.JSONDecodeError("Se esperaba una lista", doc=str(data), pos=0)
            return data
        except FileNotFoundError:
            return []

    def _guardar(self, ruta: str, elementos: List[Dict[str, Any]]) -> None:
        dirpath = os.path.dirname(ruta)
        os.makedirs(dirpath, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(elementos, f, ensure_ascii=False, indent=2)

    # Productos
    def cargar_productos(self) -> List[Dict[str, Any]]:
        return self._cargar(self.productos_path)

    def guardar_productos(self, productos: List[Dict[str, Any]]) -> None:
        self._guardar(self.productos_path, productos)

    # Usuarios
    def cargar_usuarios(self) -> List[Dict[str, Any]]:
        return self._cargar(self.usuarios_path)

    def guardar_usuarios(self, usuarios: List[Dict[str, Any]]) -> None:
        self._guardar(self.usuarios_path, usuarios)

    # Ventas
    def cargar_ventas(self) -> List[Dict[str, Any]]:
        return self._cargar(self.ventas_path)

    def guardar_ventas(self, ventas: List[Dict[str, Any]]) -> None:
        self._guardar(self.ventas_path, ventas)
