"""
Módulo que define la clase Producto.
Implementa el uso de constructor tradicional __init__, decoradores @property y @setter
para el control de atributos con validaciones básicas.
"""


class Producto:
    """
    Clase que representa un producto del restaurante.
    Utiliza constructor tradicional y decoradores @property/@setter para controlar atributos.
    """

    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        """
        Constructor del producto.
        
        Args:
            nombre (str): Nombre del producto
            categoria (str): Categoría del producto
            precio (float): Precio del producto
            disponible (bool): Disponibilidad del producto (por defecto True)
        
        Raises:
            ValueError: Si algún parámetro no cumple las validaciones
        """
        self._nombre = ""
        self._categoria = ""
        self._precio = 0.0
        self._disponible = disponible

        # Usar setters para aplicar validaciones
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    @property
    def nombre(self) -> str:
        """Retorna el nombre del producto."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        """
        Establece el nombre del producto con validación.
        
        Args:
            valor (str): Nuevo nombre del producto
        
        Raises:
            ValueError: Si el nombre está vacío
        """
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def categoria(self) -> str:
        """Retorna la categoría del producto."""
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        """
        Establece la categoría del producto con validación.
        
        Args:
            valor (str): Nueva categoría del producto
        
        Raises:
            ValueError: Si la categoría está vacía
        """
        if not valor or not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor.strip()

    @property
    def precio(self) -> float:
        """Retorna el precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        """
        Establece el precio del producto con validación.
        
        Args:
            valor (float): Nuevo precio del producto
        
        Raises:
            ValueError: Si el precio no es mayor a cero
        """
        try:
            precio_float = float(valor)
            if precio_float <= 0:
                raise ValueError("El precio del producto debe ser mayor que cero.")
            self._precio = precio_float
        except (ValueError, TypeError):
            raise ValueError("El precio debe ser un número válido mayor que cero.")

    @property
    def disponible(self) -> bool:
        """Retorna la disponibilidad del producto."""
        return self._disponible

    @disponible.setter
    def disponible(self, valor: bool) -> None:
        """
        Establece la disponibilidad del producto.
        
        Args:
            valor (bool): Nuevo estado de disponibilidad
        """
        self._disponible = bool(valor)

    def mostrar_informacion(self) -> str:
        """
        Retorna la información del producto en formato legible.
        
        Returns:
            str: Información formateada del producto
        """
        estado = "Disponible" if self.disponible else "No disponible"
        return (f"Producto: {self.nombre}\n"
                f"  Categoría: {self.categoria}\n"
                f"  Precio: ${self.precio:.2f}\n"
                f"  Estado: {estado}")

    def __str__(self) -> str:
        """Retorna una representación en string del producto."""
        return f"{self.nombre} ({self.categoria}) - ${self.precio:.2f}"

    def __repr__(self) -> str:
        """Retorna una representación oficial del producto."""
        return f"Producto(nombre='{self.nombre}', categoria='{self.categoria}', precio={self.precio}, disponible={self.disponible})"
