"""
Servicio Restaurante
Gestiona productos, clientes y operaciones básicas (registrar, listar, crear pedidos).
"""
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    def __init__(self, nombre: str):
        """Inicializa el restaurante con listas vacías de productos y clientes."""
        self.nombre = nombre
        self.productos = []  # lista de Producto
        self.clientes = []   # lista de Cliente

    # ----- Gestión de productos -----
    def registrar_producto(self, producto: Producto):
        """Registra un producto en el catálogo."""
        if not isinstance(producto, Producto):
            raise TypeError("Se esperaba un objeto Producto")
        self.productos.append(producto)

    def listar_productos(self):
        """Devuelve la lista de productos registrados."""
        return self.productos

    def buscar_producto_por_id(self, id_producto: int):
        for p in self.productos:
            if p.id == id_producto:
                return p
        return None

    def buscar_producto_por_nombre(self, nombre: str):
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    # ----- Gestión de clientes -----
    def registrar_cliente(self, cliente: Cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("Se esperaba un objeto Cliente")
        self.clientes.append(cliente)

    def listar_clientes(self):
        return self.clientes

    def buscar_cliente_por_id(self, id_cliente: int):
        for c in self.clientes:
            if c.id == id_cliente:
                return c
        return None

    # ----- Pedidos -----
    def crear_pedido(self, id_cliente: int, lista_ids_productos: list):
        """Crea un pedido para un cliente dado una lista de ids de productos.

        Devuelve el total del pedido.
        """
        cliente = self.buscar_cliente_por_id(id_cliente)
        if cliente is None:
            raise ValueError("Cliente no encontrado")

        productos_pedido = []
        for pid in lista_ids_productos:
            prod = self.buscar_producto_por_id(pid)
            if prod is None:
                raise ValueError(f"Producto con id {pid} no encontrado")
            productos_pedido.append(prod)

        cliente.agregar_pedido(productos_pedido)
        total = sum(p.precio for p in productos_pedido)
        return round(total, 2)

    def mostrar_pedidos_cliente(self, id_cliente: int):
        cliente = self.buscar_cliente_por_id(id_cliente)
        if cliente is None:
            raise ValueError("Cliente no encontrado")
        if not cliente.pedidos:
            return f"El cliente {cliente.nombre} no tiene pedidos registrados."

        salida = [f"Pedidos de {cliente.nombre}:"]
        for i, pedido in enumerate(cliente.pedidos, start=1):
            salida.append(f"  Pedido {i}:")
            for prod in pedido:
                salida.append(f"    - {prod}")
        salida.append(f"  Total gastado: ${cliente.monto_total():.2f}")
        return "\n".join(salida)

