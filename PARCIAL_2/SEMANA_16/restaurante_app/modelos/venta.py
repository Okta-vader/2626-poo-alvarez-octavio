from __future__ import annotations
from typing import Any, Dict
from datetime import datetime


class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int, fecha: str | None = None) -> None:
        if not usuario_id or not isinstance(usuario_id, str):
            raise ValueError("Identificación de usuario inválida para la venta")
        if not producto_codigo or not isinstance(producto_codigo, str):
            raise ValueError("Código de producto inválido para la venta")
        try:
            cantidad_val = int(cantidad)
        except (TypeError, ValueError) as exc:
            raise ValueError("Cantidad inválida") from exc
        if cantidad_val <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        self.usuario_id: str = usuario_id
        self.producto_codigo: str = producto_codigo
        self.cantidad: int = cantidad_val
        self.fecha: str = fecha or datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
            "fecha": self.fecha,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Venta":
        try:
            return cls(
                usuario_id=data["usuario_id"],
                producto_codigo=data["producto_codigo"],
                cantidad=data.get("cantidad", 1),
                fecha=data.get("fecha"),
            )
        except KeyError as exc:
            raise KeyError(f"Falta la clave en venta: {exc.args[0]}") from exc

    def __str__(self) -> str:
        return f"{self.fecha} - Usuario: {self.usuario_id} - Producto: {self.producto_codigo} - Cantidad: {self.cantidad}"
