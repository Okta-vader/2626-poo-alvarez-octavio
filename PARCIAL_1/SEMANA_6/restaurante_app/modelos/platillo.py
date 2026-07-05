# Clase hija Platillo
# Hereda de Producto y agrega atributos específicos de platillos

from .producto import Producto


class Platillo(Producto):
    """Clase que representa un platillo (comida) del restaurante.
    
    Atributos heredados:
        nombre (str): Nombre del platillo
        __precio (float): Precio del platillo (encapsulado)
        disponibilidad (bool): Disponibilidad del platillo
    
    Atributos propios:
        tipo_platillo (str): Tipo de platillo (entrada, plato fuerte, postre)
        tiempo_preparacion (int): Tiempo de preparación en minutos
        calorias (int): Calorías del platillo
    """
    
    def __init__(self, nombre, precio, tipo_platillo, tiempo_preparacion, calorias, disponibilidad=True):
        """Inicializa un platillo.
        
        Args:
            nombre (str): Nombre del platillo
            precio (float): Precio del platillo
            tipo_platillo (str): Tipo de platillo
            tiempo_preparacion (int): Tiempo de preparación en minutos
            calorias (int): Calorías del platillo
            disponibilidad (bool): Disponibilidad del platillo (por defecto True)
        """
        # Utiliza super() para reutilizar el constructor de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        self.tipo_platillo = tipo_platillo
        self.tiempo_preparacion = tiempo_preparacion
        self.calorias = calorias
    
    def mostrar_informacion(self):
        """Sobrescribe el método mostrar_informacion() para platillos.
        
        Demuestra polimorfismo al mostrar información específica del platillo.
        
        Returns:
            str: Información formateada del platillo
        """
        estado = "Disponible" if self.disponibilidad else "No disponible"
        return (f"===================================\n"
                f"PLATILLO\n"
                f"Nombre: {self.nombre}\n"
                f"Tipo: {self.tipo_platillo}\n"
                f"Precio: ${self.obtener_precio():.2f}\n"
                f"Tiempo de preparacion: {self.tiempo_preparacion} min\n"
                f"Calorias: {self.calorias} kcal\n"
                f"Estado: {estado}\n"
                f"===================================")
