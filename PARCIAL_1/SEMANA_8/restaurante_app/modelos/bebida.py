"""
Modulo que define la clase Bebida.
Clase hija de Producto que incorpora informacion especifica de bebidas.
Demuestra herencia y polimorfismo (Sustitution de Liskov).
"""

from .producto import Producto


class Bebida(Producto):
    """
    Clase que representa una bebida del restaurante.
    Hereda de Producto e incorpora atributos especificos de bebidas.
    Esta clase puede utilizarse en cualquier contexto donde se espere un Producto.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamaño: str,
        tipo_envase: str
    ) -> None:
        """
        Constructor de la bebida.
        
        Args:
            codigo (str): Codigo identificador unico
            nombre (str): Nombre de la bebida
            categoria (str): Categoria (debe estar relacionada a bebidas)
            precio (float): Precio unitario
            tamaño (str): Tamaño de la bebida (ej: Pequeño, Mediano, Grande)
            tipo_envase (str): Tipo de envase (ej: Botella, Lata, Vaso)
        
        Raises:
            ValueError: Si alguno de los parametros es invalido
        """
        # Llamar al constructor de la clase padre
        super().__init__(codigo, nombre, categoria, precio)
        
        # Validar atributos especificos de bebida
        self._validar_atributos_bebida(tamaño, tipo_envase)
        
        self._tamaño = tamaño
        self._tipo_envase = tipo_envase

    @staticmethod
    def _validar_atributos_bebida(tamaño: str, tipo_envase: str) -> None:
        """
        Valida los atributos especificos de la bebida.
        
        Args:
            tamaño (str): Tamaño de la bebida
            tipo_envase (str): Tipo de envase
        
        Raises:
            ValueError: Si alguno de los atributos no es valido
        """
        if not tamaño or not tamaño.strip():
            raise ValueError("El tamaño de la bebida no puede estar vacio.")
        
        if not tipo_envase or not tipo_envase.strip():
            raise ValueError("El tipo de envase no puede estar vacio.")

    @property
    def tamaño(self) -> str:
        """Retorna el tamaño de la bebida."""
        return self._tamaño

    @property
    def tipo_envase(self) -> str:
        """Retorna el tipo de envase."""
        return self._tipo_envase

    def mostrar_informacion(self) -> str:
        """
        Retorna la informacion de la bebida en formato legible.
        Sobrescribe el metodo de la clase padre para incluir atributos especificos.
        
        Returns:
            str: Informacion formateada de la bebida
        """
        return (
            f"Bebida: {self.nombre}\n"
            f"  Codigo: {self.codigo}\n"
            f"  Categoria: {self.categoria}\n"
            f"  Precio: ${self.precio:.2f}\n"
            f"  Tamaño: {self.tamaño}\n"
            f"  Tipo de envase: {self.tipo_envase}"
        )

    def __str__(self) -> str:
        """Retorna una representacion en string de la bebida."""
        return (
            f"{self.nombre} ({self.tamaño}, {self.tipo_envase}) "
            f"({self.codigo}) - ${self.precio:.2f}"
        )

    def __repr__(self) -> str:
        """Retorna una representacion oficial de la bebida."""
        return (
            f"Bebida(codigo='{self.codigo}', nombre='{self.nombre}', "
            f"categoria='{self.categoria}', precio={self.precio}, "
            f"tamaño='{self.tamaño}', tipo_envase='{self.tipo_envase}')"
        )
