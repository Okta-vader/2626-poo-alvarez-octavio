from typing import Dict, Any

class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        if not identificacion or not isinstance(identificacion, str):
            raise ValueError("Identificación inválida")
        if not nombre or not isinstance(nombre, str):
            raise ValueError("Nombre inválido")
        if not correo or not isinstance(correo, str):
            raise ValueError("Correo inválido")

        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def to_dict(self) -> Dict[str, Any]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Usuario":
        try:
            identificacion = data["identificacion"]
            nombre = data["nombre"]
            correo = data["correo"]
        except KeyError as e:
            raise KeyError(f"Falta la clave: {e.args[0]}")
        return cls(identificacion=identificacion, nombre=nombre, correo=correo)

    def __repr__(self) -> str:
        return f"Usuario(identificacion={self.identificacion!r}, nombre={self.nombre!r}, correo={self.correo!r})"

    def __str__(self) -> str:
        return f"{self.identificacion} - {self.nombre} <{self.correo}>"