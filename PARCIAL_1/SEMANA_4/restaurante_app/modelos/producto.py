"""
Modelo Producto
Representa un producto del restaurante (plato, bebida u otro).
"""

class Producto:
    def __init__(self, id_producto: int, nombre: str, tipo: str, precio: float, descripcion: str = ""):
        """Inicializa un producto.

        Args:
            id_producto: identificador numérico del producto
            nombre: nombre del producto
            tipo: tipo de producto (por ejemplo: 'plato', 'bebida')
            precio: precio unitario
            descripcion: descripción breve
        """
        self.id = id_producto
        self.nombre = nombre
        self.tipo = tipo
        self.precio = float(precio)
        self.descripcion = descripcion

    def aplicar_descuento(self, porcentaje: float):
        """Aplica un descuento porcentual al precio del producto.

        porcentaje: 0-100
        """
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        self.precio = round(self.precio * (1 - porcentaje / 100), 2)

    def __str__(self):
        return f"Producto[{self.id}] {self.nombre} ({self.tipo}) - ${self.precio:.2f} - {self.descripcion}"

