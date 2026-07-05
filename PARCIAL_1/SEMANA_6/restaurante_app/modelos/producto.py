# Clase padre Producto
# Representa un producto general del restaurante con atributos comunes

class Producto:
    """Clase padre que representa un producto general del restaurante.
    
    Atributos:
        nombre (str): Nombre del producto
        __precio (float): Precio del producto (encapsulado)
        disponibilidad (bool): Indica si el producto está disponible
    """
    
    def __init__(self, nombre, precio, disponibilidad=True):
        """Inicializa un producto.
        
        Args:
            nombre (str): Nombre del producto
            precio (float): Precio del producto (debe ser positivo)
            disponibilidad (bool): Disponibilidad del producto (por defecto True)
            
        Raises:
            ValueError: Si el precio es negativo o igual a cero
        """
        self.nombre = nombre
        self.__precio = self._validar_precio(precio)
        self.disponibilidad = disponibilidad
    
    def _validar_precio(self, precio):
        """Valida que el precio sea positivo y mayor a cero.
        
        Args:
            precio (float): Precio a validar
            
        Returns:
            float: Precio validado
            
        Raises:
            ValueError: Si el precio es negativo o igual a cero
        """
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        return precio
    
    def obtener_precio(self):
        """Obtiene el precio del producto.
        
        Returns:
            float: Precio del producto
        """
        return self.__precio
    
    def cambiar_precio(self, nuevo_precio):
        """Cambia el precio del producto con validación.
        
        Args:
            nuevo_precio (float): Nuevo precio del producto
            
        Raises:
            ValueError: Si el nuevo precio es negativo o igual a cero
        """
        self.__precio = self._validar_precio(nuevo_precio)
    
    def mostrar_informacion(self):
        """Muestra la información del producto.
        
        Este método será sobrescrito en las clases hijas para mostrar
        información específica de cada tipo de producto.
        """
        estado = "Disponible" if self.disponibilidad else "No disponible"
        return f"Producto: {self.nombre}\nPrecio: ${self.__precio:.2f}\nEstado: {estado}"
