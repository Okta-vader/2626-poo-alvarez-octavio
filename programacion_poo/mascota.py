"""
================================================================================
PROGRAMA 2: SISTEMA DE REGISTRO DE MASCOTAS - PROGRAMACIÓN ORIENTADA A OBJETOS
================================================================================

Archivo: mascota.py
Descripción:
    Define la CLASE MASCOTA que representa una mascota en el sistema.
    Demuestra los conceptos fundamentales de la POO:
    - CLASE: Plantilla para crear objetos
    - OBJETO: Instancia específica de una clase
    - ATRIBUTOS: Características de cada objeto
    - MÉTODOS: Funciones asociadas a la clase
    - CONSTRUCTOR: Método especial para inicializar objetos
    - ENCAPSULACIÓN: Agrupar datos y comportamiento
    - ABSTRACCIÓN: Ocultar detalles de implementación

Diferencia con Programación Tradicional:
    ✗ TRADICIONAL: Variables globales + funciones independientes
    ✓ POO:         Clases que encapsulan datos y comportamiento
================================================================================
"""


class Mascota:
    """
    ========================================================================
    CLASE: Mascota
    ========================================================================

    Definición:
        Una CLASE es una plantilla o molde que define:
        - QUÉ datos tendrá cada objeto (atributos)
        - QUÉ acciones puede realizar cada objeto (métodos)

    Esta clase define a una mascota con sus caracteristicas y comportamientos.

    Atributos de la Clase Mascota:
        - nombre (str): El nombre de la mascota
        - especie (str): La especie (perro, gato, pájaro, etc.)
        - edad (int): La edad en años

    Métodos de la Clase Mascota:
        - __init__(): Constructor - inicializa los atributos
        - mostrar_informacion(): Muestra la información del objeto
        - hacer_sonido(): Produce un sonido según la especie
        - obtener_descripcion(): Retorna descripción de texto
        - envejecer(): Incrementa la edad del objeto
        - cambiar_nombre(): Modifica el nombre del objeto

    ENCAPSULACIÓN:
        Los datos (atributos) y funciones (métodos) están agrupados
        en una sola unidad cohesiva: la clase.

    Equivalente en Programación Tradicional:
        class Mascota sería reemplazado por:
        - Un diccionario con los datos
        - Funciones separadas que operan sobre ese diccionario
    ========================================================================
    """

    def __init__(self, nombre, especie, edad):
        """
        ====================================================================
        MÉTODO CONSTRUCTOR: __init__()
        ====================================================================

        Definición:
            El constructor es un MÉTODO ESPECIAL que se ejecuta AUTOMÁTICAMENTE
            cuando se crea un nuevo objeto (instancia) de la clase.

        Propósito:
            Inicializar los ATRIBUTOS del objeto con los valores proporcionados.

        Parámetros:
            self: Referencia al objeto actual (ES OBLIGATORIO)
                  Python lo proporciona automáticamente
            nombre (str): El nombre de la mascota
            especie (str): La especie de la mascota
            edad (int): La edad de la mascota en años

        Atributos de Instancia:
            Los atributos se crean con la notación self.nombre_atributo
            Cada objeto tiene sus propios valores de estos atributos

        Ejemplo de Uso:
            mascota1 = Mascota("Max", "Perro", 5)
            # El constructor se ejecuta automáticamente
            # Crea un objeto con nombre="Max", especie="Perro", edad=5

        En Programación Tradicional:
            Esto sería como crear un diccionario:
            mascota1 = {"nombre": "Max", "especie": "Perro", "edad": 5}
        ====================================================================
        """
        # Inicializar ATRIBUTOS de la instancia actual
        # self.nombre es un atributo de este objeto
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """
        ====================================================================
        MÉTODO: mostrar_informacion()
        ====================================================================

        Definición:
            Un MÉTODO es una función que pertenece a una CLASE.
            Solo puede ser ejecutado por objetos de esa clase.

        Propósito:
            Muestra la información completa del objeto de forma organizada.

        Parámetro:
            self: El objeto que ejecuta este método

        Retorna:
            Ninguno (imprime en pantalla)

        ABSTRACCIÓN:
            El usuario solo llama: objeto.mostrar_informacion()
            No necesita saber CÓMO se implementa internamente

        Ejemplo:
            mascota1.mostrar_informacion()
            # Muestra la información de mascota1

        En Programación Tradicional:
            Sería una función separada:
            def mostrar_mascota(mascota):
                print(f"Nombre: {mascota['nombre']}", ...)
        ====================================================================
        """
        print("\n" + "-" * 40)
        # Acceder a los atributos del objeto usando self.atributo
        print(f"Nombre:   {self.nombre}")
        print(f"Especie:  {self.especie}")
        print(f"Edad:     {self.edad} años")
        print("-" * 40)

    def hacer_sonido(self):
        """
        ====================================================================
        MÉTODO: hacer_sonido() - EJEMPLO DE ABSTRACCIÓN Y POLIMORFISMO
        ====================================================================

        ABSTRACCIÓN:
            Definición: Ocultar la complejidad detrás de una interfaz simple
            Aquí: El usuario solo llama "mascota.hacer_sonido()"
                  El método internamente decide qué sonido hacer
                  El usuario NO ve la lógica interna (el diccionario de sonidos)

        POLIMORFISMO:
            Definición: Un mismo método se comporta diferente según el objeto
            Aquí: hacer_sonido() produce:
                  - "Guau guau" si es un perro
                  - "Miau" si es un gato
                  - "Pío pío" si es un pájaro
                  etc.
            Mismo método, diferente comportamiento según la especie

        Proceso:
            1. Crea un diccionario con sonidos por especie
            2. Busca la especie del objeto en el diccionario
            3. Obtiene el sonido correspondiente
            4. Imprime: "{nombre} hace: {sonido}"

        En Programación Tradicional:
            def hacer_sonido(mascota):
                sonidos = {...}
                sonido = sonidos.get(mascota['especie'].lower(), ...)
                print(f"{mascota['nombre']} hace: {sonido}")

        ====================================================================
        """
        # Diccionario que mapea especie con su sonido
        # Este es un ejemplo de ENCAPSULACIÓN de lógica
        sonidos = {
            "perro": "¡Guau guau!",
            "gato": "¡Miau!",
            "pájaro": "¡Pío pío!",
            "vaca": "¡Muuu!",
            "cerdo": "¡Oink oink!",
            "caballo": "¡Relincho!",
            "oveja": "¡Beeee!",
            "ratón": "¡Chiiip!",
            "conejo": "¡Thump thump!"
        }

        # Obtener sonido según la especie del objeto (self.especie)
        # .get() retorna el valor si existe, si no retorna el default
        sonido = sonidos.get(self.especie.lower(), "¡Hace un sonido!")

        # Mostrar el resultado usando el nombre de este objeto
        print(f"\n{self.nombre} hace: {sonido}")
    
    def obtener_descripcion(self):
        """
        ====================================================================
        MÉTODO: obtener_descripcion()
        ====================================================================
        
        Propósito:
            Retorna una descripción en texto de la mascota.
            Combina los atributos del objeto en una cadena descriptiva.
        
        Retorna:
            str: Una descripción formateada del objeto
        
        ENCAPSULACIÓN:
            Este método encapsula la lógica de cómo se presenta la información.
            Si queremos cambiar el formato, solo modificamos aquí.
        
        Ejemplo:
            descripcion = mascota1.obtener_descripcion()
            # Retorna: "Max es un(a) perro de 5 años"
        ====================================================================
        """
        # Construir y retornar una descripción usando los atributos
        return f"{self.nombre} es un(a) {self.especie.lower()} de {self.edad} años"
    
    def envejecer(self):
        """
        ====================================================================
        MÉTODO: envejecer() - MODIFICACIÓN DE ATRIBUTOS
        ====================================================================
        
        Propósito:
            Incrementa la edad de la mascota en un año.
            Demuestra cómo un método puede MODIFICAR los atributos del objeto.
        
        Funcionamiento:
            1. Accede al atributo self.edad
            2. Le suma 1
            3. Guarda el nuevo valor en self.edad
            4. Muestra un mensaje
        
        NOTA IMPORTANTE:
            Esto es una MUTACIÓN del objeto. El objeto cambia su estado.
            El atributo 'edad' ahora tiene un valor diferente.
        
        Ejemplo:
            print(mascota1.edad)  # 5
            mascota1.envejecer()  # "¡Felicidades! Max cumplió 6 años."
            print(mascota1.edad)  # 6
        
        En Programación Tradicional:
            mascota['edad'] += 1
        ====================================================================
        """
        # Incrementar el atributo edad del objeto
        self.edad += 1
        print(f"\n¡Felicidades! {self.nombre} cumplió {self.edad} años.")
    
    def cambiar_nombre(self, nuevo_nombre):
        """
        ====================================================================
        MÉTODO: cambiar_nombre(nuevo_nombre) - PARÁMETROS Y ATRIBUTOS
        ====================================================================
        
        Propósito:
            Cambia el nombre de la mascota.
            Demuestra cómo los métodos pueden recibir parámetros.
        
        Parámetros:
            self: El objeto que ejecuta este método
            nuevo_nombre (str): El nuevo nombre para asignar
        
        Proceso:
            1. Guarda el nombre anterior
            2. Asigna el nuevo valor a self.nombre
            3. Muestra un mensaje con ambos nombres
        
        DIFERENCIA CON PROGRAMACIÓN TRADICIONAL:
            En POO: mascota1.cambiar_nombre("NewName")
            En Tradicional: cambiar_nombre(mascota1, "NewName")
            
            Con POO es más intuitivo: el objeto ejecuta el método sobre sí mismo
        
        Ejemplo:
            print(mascota1.nombre)  # "Max"
            mascota1.cambiar_nombre("Maxwell")
            # "Max ahora se llama Maxwell"
            print(mascota1.nombre)  # "Maxwell"
        ====================================================================
        """
        # Guardar el nombre anterior para el mensaje
        nombre_anterior = self.nombre
        # Asignar el nuevo nombre al atributo
        self.nombre = nuevo_nombre
        # Mostrar confirmación
        print(f"\n{nombre_anterior} ahora se llama {self.nombre}")



