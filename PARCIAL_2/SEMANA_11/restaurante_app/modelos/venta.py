from typing import Dict, Any
from datetime import datetime

class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int, fecha: str | None = None) -> None:
        if not usuario_id or not isinstance(usuario_id, str):
            raise ValueError("usuario_id inválido")
        if not producto_codigo or not isinstance(producto_codigo, str):
            raise ValueError("producto_codigo inválido")
        cantidad_val = int(cantidad)
        if cantidad_val <= 0:
            raise ValueError("Cantidad inválida")

        self.usuario_id: str = usuario_id
        self.producto_codigo: str = producto_codigo
        self.cantidad: int = cantidad_val
        self.fecha: str = fecha or datetime.utcnow().isoformat()

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
            usuario_id = data["usuario_id"]
            producto_codigo = data["producto_codigo"]
            cantidad = data["cantidad"]
            fecha = data.get("fecha")
        except KeyError as e:
            raise KeyError(f"Falta la clave: {e.args[0]}")
        return cls(usuario_id=usuario_id, producto_codigo=producto_codigo, cantidad=cantidad, fecha=fecha)

    def __repr__(self) -> str:
        return f"Venta(usuario_id={self.usuario_id!r}, producto_codigo={self.producto_codigo!r}, cantidad={self.cantidad!r}, fecha={self.fecha!r})"

    def __str__(self) -> str:
        return f"{self.fecha}: Usuario {self.usuario_id} compró {self.cantidad} x {self.producto_codigo}"