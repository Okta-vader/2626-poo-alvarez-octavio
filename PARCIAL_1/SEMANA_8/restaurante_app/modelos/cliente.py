"""
Modulo que define la clase Cliente.
Clase que representa a un cliente registrado en el restaurante.
"""


class Cliente:
    """
    Clase que representa un cliente del restaurante.
    Mantiene informacion basica del cliente como identificacion, nombre y correo.
    """

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ) -> None:
        """
        Constructor del cliente.
        
        Args:
            identificacion (str): Identificacion unica del cliente
            nombre (str): Nombre completo del cliente
            correo (str): Correo electronico del cliente
        
        Raises:
            ValueError: Si alguno de los parametros es invalido
        """
        self._validar_parametros(identificacion, nombre, correo)
        
        self._identificacion = identificacion
        self._nombre = nombre
        self._correo = correo

    @staticmethod
    def _validar_parametros(
        identificacion: str,
        nombre: str,
        correo: str
    ) -> None:
        """
        Valida que los parametros sean correctos.
        
        Args:
            identificacion (str): Identificacion del cliente
            nombre (str): Nombre del cliente
            correo (str): Correo electronico
        
        Raises:
            ValueError: Si alguno de los parametros no es valido
        """
        if not identificacion or not identificacion.strip():
            raise ValueError("La identificacion no puede estar vacia.")
        
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del cliente no puede estar vacio.")
        
        if not correo or not correo.strip():
            raise ValueError("El correo no puede estar vacio.")

    @property
    def identificacion(self) -> str:
        """Retorna la identificacion del cliente."""
        return self._identificacion

    @property
    def nombre(self) -> str:
        """Retorna el nombre del cliente."""
        return self._nombre

    @property
    def correo(self) -> str:
        """Retorna el correo del cliente."""
        return self._correo

    def mostrar_informacion(self) -> str:
        """
        Retorna la informacion del cliente en formato legible.
        
        Returns:
            str: Informacion formateada del cliente
        """
        return (
            f"Cliente: {self.nombre}\n"
            f"  Identificacion: {self.identificacion}\n"
            f"  Correo: {self.correo}"
        )

    def __str__(self) -> str:
        """Retorna una representacion en string del cliente."""
        return f"{self.nombre} ({self.identificacion})"

    def __repr__(self) -> str:
        """Retorna una representacion oficial del cliente."""
        return (
            f"Cliente(identificacion='{self.identificacion}', "
            f"nombre='{self.nombre}', correo='{self.correo}')"
        )

    def __eq__(self, otro: object) -> bool:
        """
        Compara dos clientes por identificacion.
        
        Args:
            otro (object): Objeto a comparar
        
        Returns:
            bool: True si tienen la misma identificacion
        """
        if isinstance(otro, Cliente):
            return self.identificacion == otro.identificacion
        return False

    def __hash__(self) -> int:
        """Permite usar Cliente en conjuntos y diccionarios."""
        return hash(self.identificacion)
