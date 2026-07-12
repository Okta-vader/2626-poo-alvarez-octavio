"""
Módulo que define la clase Cliente.
Implementa el uso del decorador @dataclass para simplificar la creación de la clase.
"""

from dataclasses import dataclass


@dataclass
class Cliente:
    """
    Clase que representa un cliente del restaurante.
    Implementada usando el decorador @dataclass para simplificar su definición.
    """
    
    nombre: str
    correo: str
    id_cliente: str

    def mostrar_informacion(self) -> str:
        """
        Retorna la información del cliente en formato legible.
        
        Returns:
            str: Información formateada del cliente
        """
        return (f"Cliente: {self.nombre}\n"
                f"  Correo: {self.correo}\n"
                f"  ID: {self.id_cliente}")

    def __str__(self) -> str:
        """Retorna una representación en string del cliente."""
        return f"{self.nombre} ({self.id_cliente})"
