import json
import os
from typing import List, Dict, Any

class ArchivoServicio:
    def __init__(self, ruta: str) -> None:
        self.ruta = ruta

    def cargar(self) -> List[Dict[str, Any]]:
        """Intenta leer y devolver la lista de productos en formato dict.
        Si el archivo no existe, devuelve lista vacía.
        Lanza json.JSONDecodeError si el contenido no es JSON válido.
        Propaga PermissionError si no hay permisos.
        """
        try:
            with open(self.ruta, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list):
                raise json.JSONDecodeError("Se esperaba una lista de productos", doc=str(data), pos=0)
            return data
        except FileNotFoundError:
            return []

    def guardar(self, productos: List[Dict[str, Any]]) -> None:
        """Escribe la lista de productos (como diccionarios) en el archivo JSON.
        Propaga PermissionError si no hay permisos.
        """
        dirpath = os.path.dirname(self.ruta)
        os.makedirs(dirpath, exist_ok=True)
        with open(self.ruta, "w", encoding="utf-8") as f:
            json.dump(productos, f, ensure_ascii=False, indent=2)
