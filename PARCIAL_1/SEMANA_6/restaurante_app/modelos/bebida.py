# Clase hija Bebida
# Hereda de Producto y agrega atributos específicos de bebidas

from .producto import Producto


class Bebida(Producto):
    """Clase que representa una bebida del restaurante.
    
    Atributos heredados:
        nombre (str): Nombre de la bebida
        __precio (float): Precio de la bebida (encapsulado)
        disponibilidad (bool): Disponibilidad de la bebida
    
    Atributos propios:
        volumen_ml (int): Volumen de la bebida en mililitros
        tipo_bebida (str): Tipo de bebida (gaseosa, zumo, té, café, etc.)
        temperatura (str): Temperatura de servicio (fría, caliente, temperatura ambiente)
    """
    
    def __init__(self, nombre, precio, volumen_ml, tipo_bebida, temperatura, disponibilidad=True):
        """Inicializa una bebida.
        
        Args:
            nombre (str): Nombre de la bebida
            precio (float): Precio de la bebida
            volumen_ml (int): Volumen en mililitros
            tipo_bebida (str): Tipo de bebida
            temperatura (str): Temperatura de servicio
            disponibilidad (bool): Disponibilidad de la bebida (por defecto True)
        """
        # Utiliza super() para reutilizar el constructor de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        self.volumen_ml = volumen_ml
        self.tipo_bebida = tipo_bebida
        self.temperatura = temperatura
    
    def mostrar_informacion(self):
        """Sobrescribe el método mostrar_informacion() para bebidas.
        
        Demuestra polimorfismo al mostrar información específica de la bebida.
        
        Returns:
            str: Información formateada de la bebida
        """
        estado = "Disponible" if self.disponibilidad else "No disponible"
        return (f"-----------------------------------\n"
                f"BEBIDA\n"
                f"Nombre: {self.nombre}\n"
                f"Tipo: {self.tipo_bebida}\n"
                f"Precio: ${self.obtener_precio():.2f}\n"
                f"Volumen: {self.volumen_ml} ml\n"
                f"Temperatura: {self.temperatura}\n"
                f"Estado: {estado}\n"
                f"-----------------------------------")
