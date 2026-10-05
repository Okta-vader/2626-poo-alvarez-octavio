from __future__ import annotations

from typing import Any, Dict


class Usuario:
    ROLES = ("Administrador", "Empleado", "Cliente")
    ROLES_GESTIONABLES = ("Empleado", "Cliente")

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        password: str = "1234",
        rol: str = "Cliente",
    ) -> None:
        identificacion = identificacion.strip() if isinstance(identificacion, str) else ""
        nombre = nombre.strip() if isinstance(nombre, str) else ""
        correo = correo.strip() if isinstance(correo, str) else ""
        password = password.strip() if isinstance(password, str) else ""

        if not identificacion:
            raise ValueError("El usuario/identificación es obligatorio.")
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        if not correo or "@" not in correo:
            raise ValueError("Ingrese un correo válido.")
        if not password:
            raise ValueError("La contraseña es obligatoria.")
        if rol not in self.ROLES:
            raise ValueError("El rol seleccionado no es válido.")

        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.password = password
        self.rol = rol

    def to_dict(self) -> Dict[str, Any]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "password": self.password,
            "rol": self.rol,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Usuario":
        identificacion = data["identificacion"]
        # Roles por defecto para conservar las cuentas heredadas de Semana 15.
        roles_anteriores = {"admin": "Administrador", "mesero": "Empleado"}
        rol = data.get("rol", roles_anteriores.get(identificacion, "Cliente"))
        return cls(
            identificacion=identificacion,
            nombre=data["nombre"],
            correo=data["correo"],
            password=data.get("password", "1234"),
            rol=rol,
        )

    def __str__(self) -> str:
        return f"{self.identificacion} - {self.nombre} <{self.correo}> ({self.rol})"
