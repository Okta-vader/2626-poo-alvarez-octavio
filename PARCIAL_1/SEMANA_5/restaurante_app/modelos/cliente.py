# Módulo que define la clase Cliente
# Representa un cliente registrado en el sistema del restaurante


class Cliente:
    """
    Clase que representa un cliente del restaurante.
    
    Atributos:
        identificador (int): Número de documento único del cliente
        nombre_completo (str): Nombre completo del cliente
        numero_contacto (str): Teléfono o número de contacto
        correo_electronico (str): Correo electrónico del cliente
        es_cliente_frecuente (bool): Indica si es cliente frecuente
        saldo_disponible (float): Saldo en cuenta del cliente
    """
    
    def __init__(
        self,
        identificador: int,
        nombre_completo: str,
        numero_contacto: str,
        correo_electronico: str,
        es_cliente_frecuente: bool = False,
        saldo_disponible: float = 0.0
    ):
        """
        Inicializa una instancia de Cliente.
        
        Args:
            identificador: Documento de identidad único
            nombre_completo: Nombre completo del cliente
            numero_contacto: Teléfono o número de contacto
            correo_electronico: Correo electrónico
            es_cliente_frecuente: Si es cliente frecuente (por defecto False)
            saldo_disponible: Saldo inicial en cuenta
        """
        self.identificador = identificador
        self.nombre_completo = nombre_completo
        self.numero_contacto = numero_contacto
        self.correo_electronico = correo_electronico
        self.es_cliente_frecuente = es_cliente_frecuente
        self.saldo_disponible = saldo_disponible
    
    def __str__(self) -> str:
        """Retorna una representación en texto del cliente."""
        estado_cliente = "Frecuente" if self.es_cliente_frecuente else "Regular"
        return (
            f"Cliente ID: {self.identificador} | "
            f"Nombre: {self.nombre_completo} | "
            f"Contacto: {self.numero_contacto} | "
            f"Email: {self.correo_electronico} | "
            f"Tipo: {estado_cliente} | "
            f"Saldo: ${self.saldo_disponible:.2f}"
        )
    
    def marcar_como_frecuente(self) -> None:
        """Marca el cliente como cliente frecuente."""
        self.es_cliente_frecuente = True
    
    def actualizar_saldo(self, cantidad: float) -> None:
        """Actualiza el saldo del cliente (positivo para agregar, negativo para restar)."""
        self.saldo_disponible += cantidad
    
    def obtener_informacion_contacto(self) -> str:
        """Retorna la información de contacto del cliente."""
        return f"{self.nombre_completo} - {self.numero_contacto} - {self.correo_electronico}"
    
    def validar_saldo(self, monto_requerido: float) -> bool:
        """Verifica si el cliente tiene suficiente saldo."""
        return self.saldo_disponible >= monto_requerido
