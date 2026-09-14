from __future__ import annotations
from typing import Any, Dict

class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str, password: str = "1234") -> None:
        if not identificacion or not isinstance(identificacion, str):
            raise ValueError("Identificación inválida")
        if not nombre or not isinstance(nombre, str):
            raise ValueError("Nombre inválido")
        if not correo or not isinstance(correo, str):
            raise ValueError("Correo inválido")
        if not password or not isinstance(password, str):
            raise ValueError("Password inválido")

        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo
        self.password: str = password

    def to_dict(self) -> Dict[str, Any]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "password": self.password,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Usuario":
        try:
            return cls(
                identificacion=data["identificacion"],
                nombre=data["nombre"],
                correo=data["correo"],
                password=data.get("password", "1234"),
            )
        except KeyError as exc:
            raise KeyError(f"Falta la clave: {exc.args[0]}")

    def __str__(self) -> str:
        return f"{self.identificacion} - {self.nombre} <{self.correo}>"