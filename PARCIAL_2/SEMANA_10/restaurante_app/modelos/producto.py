from __future__ import annotations
from typing import Dict, Any

class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        # validaciones básicas
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

        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio_val

    def actualizar(self, nombre: str | None = None, categoria: str | None = None, precio: float | None = None) -> None:
        if nombre is not None:
            if not nombre:
                raise ValueError("Nombre inválido")
            self.nombre = nombre
        if categoria is not None:
            if not categoria:
                raise ValueError("Categoría inválida")
            self.categoria = categoria
        if precio is not None:
            precio_val = float(precio)
            if precio_val < 0:
                raise ValueError("Precio no puede ser negativo")
            self.precio = precio_val

    def to_dict(self) -> Dict[str, Any]:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Producto":
        try:
            codigo = data["codigo"]
            nombre = data["nombre"]
            categoria = data["categoria"]
            precio = data["precio"]
        except KeyError as e:
            raise KeyError(f"Falta la clave: {e.args[0]}")
        return cls(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)

    def __repr__(self) -> str:
        return f"Producto(codigo={self.codigo!r}, nombre={self.nombre!r}, categoria={self.categoria!r}, precio={self.precio!r})"

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} ({self.categoria}) : ${self.precio:.2f}"
