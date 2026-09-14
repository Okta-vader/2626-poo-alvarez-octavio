from __future__ import annotations
from typing import Any, Dict

class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> None:
        if not codigo or not isinstance(codigo, str):
            raise ValueError("Código de producto inválido")
        if not nombre or not isinstance(nombre, str):
            raise ValueError("Nombre de producto inválido")
        if not categoria or not isinstance(categoria, str):
            raise ValueError("Categoría de producto inválida")
        try:
            precio_val = float(precio)
        except (TypeError, ValueError):
            raise ValueError("Precio inválido")
        if precio_val < 0:
            raise ValueError("Precio no puede ser negativo")
        try:
            stock_val = int(stock)
        except (TypeError, ValueError):
            raise ValueError("Stock inválido")
        if stock_val < 0:
            raise ValueError("Stock no puede ser negativo")

        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio_val
        self.stock: int = stock_val

    def to_dict(self) -> Dict[str, Any]:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Producto":
        try:
            return cls(
                codigo=data["codigo"],
                nombre=data["nombre"],
                categoria=data["categoria"],
                precio=data["precio"],
                stock=data.get("stock", 0),
            )
        except KeyError as exc:
            raise KeyError(f"Falta la clave: {exc.args[0]}")

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} ({self.categoria}) : ${self.precio:.2f} [stock: {self.stock}]"
