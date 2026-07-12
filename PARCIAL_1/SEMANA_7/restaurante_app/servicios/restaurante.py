"""
Módulo que define la clase Restaurante.
Actúa como servicio central para administrar productos y clientes del restaurante.
"""

from typing import List, Optional
from modelos import Producto, Cliente


class Restaurante:
    """
    Clase de servicio encargada de administrar los productos y clientes del restaurante.
    Proporciona métodos para registrar, listar y buscar productos y clientes.
    """

    def __init__(self, nombre: str = "Mi Restaurante"):
        """
        Constructor del restaurante.
        
        Args:
            nombre (str): Nombre del restaurante (por defecto "Mi Restaurante")
        """
        self.nombre = nombre
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    # ================== MÉTODOS PARA PRODUCTOS ==================

    def registrar_producto(self, producto: Producto) -> None:
        """
        Registra un nuevo producto en el restaurante.
        
        Args:
            producto (Producto): Objeto producto a registrar
        """
        if producto not in self._productos:
            self._productos.append(producto)
            print("[OK] Producto '{}' registrado exitosamente.".format(producto.nombre))
        else:
            print("[ADVERTENCIA] El producto '{}' ya esta registrado.".format(producto.nombre))

    def listar_productos(self) -> List[Producto]:
        """
        Retorna la lista de todos los productos registrados.
        
        Returns:
            List[Producto]: Lista de productos
        """
        return self._productos

    def buscar_producto(self, nombre: str) -> Optional[Producto]:
        """
        Busca un producto por nombre.
        
        Args:
            nombre (str): Nombre del producto a buscar
        
        Returns:
            Optional[Producto]: El producto encontrado o None
        """
        nombre_busqueda = nombre.strip().lower()
        for producto in self._productos:
            if producto.nombre.lower() == nombre_busqueda:
                return producto
        return None

    def obtener_productos_disponibles(self) -> List[Producto]:
        """
        Retorna la lista de productos disponibles.
        
        Returns:
            List[Producto]: Lista de productos disponibles
        """
        return [p for p in self._productos if p.disponible]

    # ================== MÉTODOS PARA CLIENTES ==================

    def registrar_cliente(self, cliente: Cliente) -> None:
        """
        Registra un nuevo cliente en el restaurante.
        
        Args:
            cliente (Cliente): Objeto cliente a registrar
        """
        if not self.buscar_cliente_por_id(cliente.id_cliente):
            self._clientes.append(cliente)
            print("[OK] Cliente '{}' registrado exitosamente.".format(cliente.nombre))
        else:
            print("[ADVERTENCIA] El cliente con ID '{}' ya esta registrado.".format(cliente.id_cliente))

    def listar_clientes(self) -> List[Cliente]:
        """
        Retorna la lista de todos los clientes registrados.
        
        Returns:
            List[Cliente]: Lista de clientes
        """
        return self._clientes

    def buscar_cliente(self, nombre: str) -> Optional[Cliente]:
        """
        Busca un cliente por nombre.
        
        Args:
            nombre (str): Nombre del cliente a buscar
        
        Returns:
            Optional[Cliente]: El cliente encontrado o None
        """
        nombre_busqueda = nombre.strip().lower()
        for cliente in self._clientes:
            if cliente.nombre.lower() == nombre_busqueda:
                return cliente
        return None

    def buscar_cliente_por_id(self, id_cliente: str) -> Optional[Cliente]:
        """
        Busca un cliente por su identificador.
        
        Args:
            id_cliente (str): ID del cliente a buscar
        
        Returns:
            Optional[Cliente]: El cliente encontrado o None
        """
        id_busqueda = id_cliente.strip().lower()
        for cliente in self._clientes:
            if cliente.id_cliente.lower() == id_busqueda:
                return cliente
        return None

    def obtener_total_productos(self) -> int:
        """Retorna el total de productos registrados."""
        return len(self._productos)

    def obtener_total_clientes(self) -> int:
        """Retorna el total de clientes registrados."""
        return len(self._clientes)
