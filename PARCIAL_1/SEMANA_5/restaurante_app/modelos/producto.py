# Módulo que define la clase Producto
# Representa un plato, bebida o artículo disponible en el restaurante


class Producto:
    """
    Clase que representa un producto disponible en el restaurante.
    
    Atributos:
        identificador (int): Número único que identifica el producto
        nombre (str): Nombre descriptivo del producto
        descripcion (str): Breve descripción del producto
        precio (float): Precio unitario del producto en pesos
        disponible (bool): Indica si el producto está disponible para venta
    """
    
    def __init__(
        self,
        identificador: int,
        nombre: str,
        descripcion: str,
        precio: float,
        disponible: bool = True
    ):
        """
        Inicializa una instancia de Producto.
        
        Args:
            identificador: ID único del producto
            nombre: Nombre del producto
            descripcion: Descripción del producto
            precio: Precio unitario
            disponible: Estado de disponibilidad (por defecto True)
        """
        self.identificador = identificador
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.disponible = disponible
    
    def __str__(self) -> str:
        """Retorna una representación en texto del producto."""
        estado = "Disponible" if self.disponible else "No disponible"
        return (
            f"Producto ID: {self.identificador} | "
            f"Nombre: {self.nombre} | "
            f"Descripción: {self.descripcion} | "
            f"Precio: ${self.precio:.2f} | "
            f"Estado: {estado}"
        )
    
    def cambiar_disponibilidad(self, disponible: bool) -> None:
        """Cambia el estado de disponibilidad del producto."""
        self.disponible = disponible
    
    def actualizar_precio(self, nuevo_precio: float) -> None:
        """Actualiza el precio del producto."""
        if nuevo_precio > 0:
            self.precio = nuevo_precio
        else:
            print("Error: El precio debe ser mayor a 0")
    
    def obtener_informacion_resumida(self) -> str:
        """Retorna información resumida del producto."""
        return f"{self.nombre} - ${self.precio:.2f}"
