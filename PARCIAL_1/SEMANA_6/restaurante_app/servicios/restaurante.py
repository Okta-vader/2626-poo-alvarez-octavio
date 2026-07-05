# Clase de servicio Restaurante
# Administra una lista de productos (Platillos y Bebidas)

class Restaurante:
    """Clase de servicio que administra los productos del restaurante.
    
    Atributos:
        nombre (str): Nombre del restaurante
        productos (list): Lista de productos registrados en el restaurante
    """
    
    def __init__(self, nombre):
        """Inicializa el restaurante.
        
        Args:
            nombre (str): Nombre del restaurante
        """
        self.nombre = nombre
        self.productos = []
    
    def agregar_producto(self, producto):
        """Agrega un producto a la lista del restaurante.
        
        Args:
            producto: Objeto de tipo Producto (Platillo o Bebida)
        """
        self.productos.append(producto)
    
    def mostrar_menu_completo(self):
        """Muestra toda la información de los productos del restaurante.
        
        Demuestra polimorfismo al recorrer la lista de productos y ejecutar
        mostrar_informacion() según el tipo de objeto (Platillo o Bebida).
        """
        print(f"\n{'*' * 50}")
        print(f"MENU DEL RESTAURANTE: {self.nombre}")
        print(f"{'*' * 50}\n")
        
        if not self.productos:
            print("No hay productos registrados en el restaurante.\n")
            return
        
        # Polimorfismo: cada producto ejecuta su propia versión de mostrar_informacion()
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto.mostrar_informacion()}\n")
        
        print(f"{'*' * 50}")
        print(f"Total de productos: {len(self.productos)}")
        print(f"{'*' * 50}\n")
    
    def listar_productos_disponibles(self):
        """Lista solo los productos disponibles.
        
        Returns:
            list: Lista de productos disponibles
        """
        disponibles = [p for p in self.productos if p.disponibilidad]
        return disponibles
    
    def buscar_producto_por_nombre(self, nombre):
        """Busca un producto por su nombre.
        
        Args:
            nombre (str): Nombre del producto a buscar
            
        Returns:
            Producto: El producto encontrado o None si no existe
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    def obtener_precio_promedio(self):
        """Calcula el precio promedio de todos los productos.
        
        Returns:
            float: Precio promedio o 0 si no hay productos
        """
        if not self.productos:
            return 0.0
        suma_precios = sum(p.obtener_precio() for p in self.productos)
        return suma_precios / len(self.productos)
