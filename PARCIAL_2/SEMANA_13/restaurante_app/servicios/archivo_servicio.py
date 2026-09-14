import json
import os
from typing import Any, Dict, List

class ArchivoServicio:
    def __init__(self, base_dir: str) -> None:
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)
        self.productos_path = os.path.join(self.base_dir, "productos.json")
        self.usuarios_path = os.path.join(self.base_dir, "usuarios.json")

    def cargar_productos(self) -> List[Dict[str, Any]]:
        try:
            with open(self.productos_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, list):
                raise json.JSONDecodeError("Se esperaba una lista", doc=str(data), pos=0)
            return data
        except FileNotFoundError:
            return []

    def guardar_productos(self, productos: List[Dict[str, Any]]) -> None:
        with open(self.productos_path, "w", encoding="utf-8") as file:
            json.dump(productos, file, ensure_ascii=False, indent=2)

    def cargar_usuarios(self) -> List[Dict[str, Any]]:
        try:
            with open(self.usuarios_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, list):
                raise json.JSONDecodeError("Se esperaba una lista", doc=str(data), pos=0)
            return data
        except FileNotFoundError:
            return []

    def guardar_usuarios(self, usuarios: List[Dict[str, Any]]) -> None:
        with open(self.usuarios_path, "w", encoding="utf-8") as file:
            json.dump(usuarios, file, ensure_ascii=False, indent=2)
