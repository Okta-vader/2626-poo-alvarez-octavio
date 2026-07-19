"""
Modulo que define la clase Restaurante.
Servicio central encargado de administrar productos y clientes.
Implementa el principio de responsabilidad unica.
"""

from typing import List, Optional
from modelos import Producto, Bebida, Cliente


class Restaurante:
    """
    Clase de servicio encargada de administrar productos y clientes del restaurante.
    Demuestra los principios SOLID:
    - Responsabilidad Unica: administra productos y clientes
    - Abierto/Cerrado: puede trabajar con nuevas clases que hereden de Producto
    - Sustitution de Liskov: Bebida puede usarse donde se espera Producto
    """

    def __init__(self, nombre: str = "Mi Restaurante") -> None:
        """
        Constructor del restaurante.
        
        Args:
            nombre (str): Nombre del restaurante (por defecto "Mi Restaurante")
        """
        self._nombre = nombre
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    @property
    def nombre(self) -> str:
        """Retorna el nombre del restaurante."""
        return self._nombre

    # ================== METODOS PARA PRODUCTOS ==================

    def registrar_producto(self, producto: Producto) -> bool:
        """
        Registra un nuevo producto en el restaurante.
        Valida que no exista otro producto con el mismo codigo.
        
        Args:
            producto (Producto): Objeto producto a registrar (puede ser Bebida)
        
        Returns:
            bool: True si fue registrado exitosamente, False si ya existe
        """
        if self._producto_existe(producto.codigo):
            return False
        
        self._productos.append(producto)
        return True

    def _producto_existe(self, codigo: str) -> bool:
        """
        Verifica si un producto con el codigo dado ya existe.
        
        Args:
            codigo (str): Codigo del producto a verificar
        
        Returns:
            bool: True si existe, False en caso contrario
        """
        return any(p.codigo == codigo for p in self._productos)

    def listar_productos(self) -> List[Producto]:
        """
        Retorna la lista de todos los productos registrados.
        Tanto productos como bebidas se almacenan juntos.
        
        Returns:
            List[Producto]: Lista de productos (incluyendo bebidas)
        """
        return self._productos.copy()

    def obtener_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        """
        Busca un producto por su codigo.
        
        Args:
            codigo (str): Codigo del producto a buscar
        
        Returns:
            Optional[Producto]: El producto encontrado o None
        """
        codigo_busqueda = codigo.strip().lower()
        for producto in self._productos:
            if producto.codigo.lower() == codigo_busqueda:
                return producto
        return None

    def obtener_total_productos(self) -> int:
        """Retorna el total de productos registrados."""
        return len(self._productos)

    # ================== METODOS PARA CLIENTES ==================

    def registrar_cliente(self, cliente: Cliente) -> bool:
        """
        Registra un nuevo cliente en el restaurante.
        Valida que no exista otro cliente con la misma identificacion.
        
        Args:
            cliente (Cliente): Objeto cliente a registrar
        
        Returns:
            bool: True si fue registrado exitosamente, False si ya existe
        """
        if self._cliente_existe(cliente.identificacion):
            return False
        
        self._clientes.append(cliente)
        return True

    def _cliente_existe(self, identificacion: str) -> bool:
        """
        Verifica si un cliente con la identificacion dada ya existe.
        
        Args:
            identificacion (str): Identificacion del cliente a verificar
        
        Returns:
            bool: True si existe, False en caso contrario
        """
        return any(c.identificacion == identificacion for c in self._clientes)

    def listar_clientes(self) -> List[Cliente]:
        """
        Retorna la lista de todos los clientes registrados.
        
        Returns:
            List[Cliente]: Lista de clientes
        """
        return self._clientes.copy()

    def obtener_cliente_por_identificacion(
        self,
        identificacion: str
    ) -> Optional[Cliente]:
        """
        Busca un cliente por su identificacion.
        
        Args:
            identificacion (str): Identificacion del cliente a buscar
        
        Returns:
            Optional[Cliente]: El cliente encontrado o None
        """
        identificacion_busqueda = identificacion.strip().lower()
        for cliente in self._clientes:
            if cliente.identificacion.lower() == identificacion_busqueda:
                return cliente
        return None

    def obtener_total_clientes(self) -> int:
        """Retorna el total de clientes registrados."""
        return len(self._clientes)
