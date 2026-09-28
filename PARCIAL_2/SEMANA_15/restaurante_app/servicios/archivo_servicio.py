import json
import os
from typing import Any, Dict, List


class ArchivoServicio:
    def __init__(self, base_dir: str) -> None:
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)
        self.productos_path = os.path.join(self.base_dir, "productos.json")
        self.usuarios_path = os.path.join(self.base_dir, "usuarios.json")
        self.ventas_path = os.path.join(self.base_dir, "ventas.json")

    def _cargar_lista(self, path: str) -> List[Dict[str, Any]]:
        try:
            with open(path, "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
            if not isinstance(data, list):
                raise json.JSONDecodeError("Se esperaba una lista", doc=str(data), pos=0)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _guardar_lista(self, path: str, data: List[Dict[str, Any]]) -> None:
        with open(path, "w", encoding="utf-8") as archivo:
            json.dump(data, archivo, ensure_ascii=False, indent=2)

    def cargar_productos(self) -> List[Dict[str, Any]]:
        return self._cargar_lista(self.productos_path)

    def guardar_productos(self, productos: List[Dict[str, Any]]) -> None:
        self._guardar_lista(self.productos_path, productos)

    def cargar_usuarios(self) -> List[Dict[str, Any]]:
        return self._cargar_lista(self.usuarios_path)

    def guardar_usuarios(self, usuarios: List[Dict[str, Any]]) -> None:
        self._guardar_lista(self.usuarios_path, usuarios)

    def cargar_ventas(self) -> List[Dict[str, Any]]:
        return self._cargar_lista(self.ventas_path)

    def guardar_ventas(self, ventas: List[Dict[str, Any]]) -> None:
        self._guardar_lista(self.ventas_path, ventas)
