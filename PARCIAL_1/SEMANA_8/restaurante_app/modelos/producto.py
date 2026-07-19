"""
Modulo que define la clase Producto.
Clase base que representa un producto general del restaurante.
Implementa el principio de responsabilidad unica.
"""


class Producto:
    """
    Clase que representa un producto del restaurante.
    Sirve como clase base para otros tipos de productos como Bebida.
    Cada producto tiene codigo, nombre, categoria y precio.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> None:
        """
        Constructor del producto.
        
        Args:
            codigo (str): Codigo identificador unico del producto
            nombre (str): Nombre del producto
            categoria (str): Categoria a la que pertenece
            precio (float): Precio unitario del producto
        
        Raises:
            ValueError: Si alguno de los parametros es invalido
        """
        self._validar_parametros(codigo, nombre, categoria, precio)
        
        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio

    @staticmethod
    def _validar_parametros(
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> None:
        """
        Valida que los parametros sean correctos.
        
        Args:
            codigo (str): Codigo del producto
            nombre (str): Nombre del producto
            categoria (str): Categoria del producto
            precio (float): Precio del producto
        
        Raises:
            ValueError: Si alguno de los parametros no cumple las validaciones
        """
        if not codigo or not codigo.strip():
            raise ValueError("El codigo del producto no puede estar vacio.")
        
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacio.")
        
        if not categoria or not categoria.strip():
            raise ValueError("La categoria del producto no puede estar vacia.")
        
        try:
            precio_float = float(precio)
            if precio_float <= 0:
                raise ValueError("El precio debe ser mayor que cero.")
        except (ValueError, TypeError):
            raise ValueError("El precio debe ser un numero valido mayor que cero.")

    @property
    def codigo(self) -> str:
        """Retorna el codigo del producto."""
        return self._codigo

    @property
    def nombre(self) -> str:
        """Retorna el nombre del producto."""
        return self._nombre

    @property
    def categoria(self) -> str:
        """Retorna la categoria del producto."""
        return self._categoria

    @property
    def precio(self) -> float:
        """Retorna el precio del producto."""
        return self._precio

    def mostrar_informacion(self) -> str:
        """
        Retorna la informacion del producto en formato legible.
        Este metodo puede ser sobrescrito por clases hijas.
        
        Returns:
            str: Informacion formateada del producto
        """
        return (
            f"Producto: {self.nombre}\n"
            f"  Codigo: {self.codigo}\n"
            f"  Categoria: {self.categoria}\n"
            f"  Precio: ${self.precio:.2f}"
        )

    def __str__(self) -> str:
        """Retorna una representacion en string del producto."""
        return f"{self.nombre} ({self.codigo}) - ${self.precio:.2f}"

    def __repr__(self) -> str:
        """Retorna una representacion oficial del producto."""
        return (
            f"Producto(codigo='{self.codigo}', nombre='{self.nombre}', "
            f"categoria='{self.categoria}', precio={self.precio})"
        )

    def __eq__(self, otro: object) -> bool:
        """
        Compara dos productos por codigo.
        
        Args:
            otro (object): Objeto a comparar
        
        Returns:
            bool: True si tienen el mismo codigo
        """
        if isinstance(otro, Producto):
            return self.codigo == otro.codigo
        return False

    def __hash__(self) -> int:
        """Permite usar Producto en conjuntos y diccionarios."""
        return hash(self.codigo)
