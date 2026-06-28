# Módulo que define la clase Restaurante
# Gestiona productos y clientes del sistema


from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase que administra los productos y clientes del restaurante.
    
    Atributos:
        nombre_restaurante (str): Nombre del restaurante
        ubicacion (str): Ubicación o dirección del restaurante
        productos (list[Producto]): Lista de productos disponibles
        clientes_registrados (list[Cliente]): Lista de clientes registrados
    """
    
    def __init__(self, nombre_restaurante: str, ubicacion: str):
        """
        Inicializa una instancia de Restaurante.
        
        Args:
            nombre_restaurante: Nombre del restaurante
            ubicacion: Ubicación del restaurante
        """
        self.nombre_restaurante = nombre_restaurante
        self.ubicacion = ubicacion
        self.productos: list[Producto] = []
        self.clientes_registrados: list[Cliente] = []
    
    def agregar_producto(self, producto: Producto) -> None:
        """Añade un producto a la lista del restaurante."""
        self.productos.append(producto)
        print(f"✓ Producto '{producto.nombre}' agregado exitosamente")
    
    def agregar_cliente(self, cliente: Cliente) -> None:
        """Registra un cliente en el sistema del restaurante."""
        self.clientes_registrados.append(cliente)
        print(f"✓ Cliente '{cliente.nombre_completo}' registrado exitosamente")
    
    def obtener_producto_por_id(self, identificador: int) -> Producto | None:
        """Busca un producto por su identificador."""
        for producto in self.productos:
            if producto.identificador == identificador:
                return producto
        return None
    
    def obtener_cliente_por_id(self, identificador: int) -> Cliente | None:
        """Busca un cliente por su identificador."""
        for cliente in self.clientes_registrados:
            if cliente.identificador == identificador:
                return cliente
        return None
    
    def listar_productos(self) -> None:
        """Muestra todos los productos disponibles."""
        print(f"\n{'='*80}")
        print(f"PRODUCTOS DISPONIBLES EN {self.nombre_restaurante.upper()}")
        print(f"{'='*80}")
        if self.productos:
            for producto in self.productos:
                print(f"  {producto}")
        else:
            print("  No hay productos registrados")
        print(f"{'='*80}\n")
    
    def listar_clientes(self) -> None:
        """Muestra todos los clientes registrados."""
        print(f"\n{'='*80}")
        print(f"CLIENTES REGISTRADOS EN {self.nombre_restaurante.upper()}")
        print(f"{'='*80}")
        if self.clientes_registrados:
            for cliente in self.clientes_registrados:
                print(f"  {cliente}")
        else:
            print("  No hay clientes registrados")
        print(f"{'='*80}\n")
    
    def productos_disponibles_para_venta(self) -> list[Producto]:
        """Retorna solo los productos disponibles."""
        return [p for p in self.productos if p.disponible]
    
    def clientes_frecuentes(self) -> list[Cliente]:
        """Retorna solo los clientes frecuentes."""
        return [c for c in self.clientes_registrados if c.es_cliente_frecuente]
    
    def obtener_total_inventario(self) -> int:
        """Retorna la cantidad total de productos en el inventario."""
        return len(self.productos)
    
    def obtener_total_clientes(self) -> int:
        """Retorna la cantidad total de clientes registrados."""
        return len(self.clientes_registrados)
    
    def mostrar_informacion_general(self) -> None:
        """Muestra información general del restaurante."""
        print(f"\n{'='*80}")
        print(f"INFORMACIÓN DEL RESTAURANTE")
        print(f"{'='*80}")
        print(f"Nombre: {self.nombre_restaurante}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Total de productos: {self.obtener_total_inventario()}")
        print(f"Productos disponibles: {len(self.productos_disponibles_para_venta())}")
        print(f"Total de clientes: {self.obtener_total_clientes()}")
        print(f"Clientes frecuentes: {len(self.clientes_frecuentes())}")
        print(f"{'='*80}\n")
