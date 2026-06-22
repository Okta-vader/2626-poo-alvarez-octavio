"""
Modelo Cliente
Representa a un cliente que realiza/o recibe pedidos en el restaurante.
"""

class Cliente:
    def __init__(self, id_cliente: int, nombre: str, telefono: str = None, mesa: int = None):
        """Inicializa un cliente.

        Args:
            id_cliente: identificador numérico del cliente
            nombre: nombre completo
            telefono: número de contacto (opcional)
            mesa: número de mesa asignada (opcional)
        """
        self.id = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.mesa = mesa
        # Cada pedido es una lista de objetos Producto
        self.pedidos = []

    def agregar_pedido(self, lista_productos):
        """Agrega un pedido (lista de productos) al historial del cliente."""
        if not isinstance(lista_productos, list):
            raise TypeError("El pedido debe ser una lista de productos")
        self.pedidos.append(lista_productos)

    def monto_total(self):
        """Calcula el total gastado por el cliente sumando todos los pedidos."""
        total = 0.0
        for pedido in self.pedidos:
            for producto in pedido:
                total += producto.precio
        return round(total, 2)

    def __str__(self):
        mesa_info = f", mesa {self.mesa}" if self.mesa is not None else ""
        return f"Cliente[{self.id}] {self.nombre}{mesa_info} - Pedidos: {len(self.pedidos)}"

