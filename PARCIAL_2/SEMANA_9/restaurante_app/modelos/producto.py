from __future__ import annotations

class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def actualizar(self, nombre: str | None = None, categoria: str | None = None, precio: float | None = None) -> None:
        if nombre is not None:
            self.nombre = nombre
        if categoria is not None:
            self.categoria = categoria
        if precio is not None:
            self.precio = precio

    def __repr__(self) -> str:
        return f"Producto(codigo={self.codigo!r}, nombre={self.nombre!r}, categoria={self.categoria!r}, precio={self.precio!r})"

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} ({self.categoria}) : ${self.precio:.2f}"
