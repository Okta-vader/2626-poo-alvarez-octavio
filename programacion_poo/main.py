"""
================================================================================
PROGRAMA 2: ARCHIVO PRINCIPAL - PROGRAMACIÓN ORIENTADA A OBJETOS
================================================================================

Archivo: main.py
Descripción:
    Demuestra el uso práctico de la CLASE MASCOTA.
    Crea objetos (INSTANCIAS) de la clase y ejecuta sus MÉTODOS.
    Evidencia todos los conceptos fundamentales de POO.

Conceptos POO Demostrados:
    1. IMPORTACIÓN: Importar la clase desde otro módulo
    2. CREACIÓN DE OBJETOS: Instanciar la clase Mascota
    3. ACCESO A ATRIBUTOS: Acceder a propiedades del objeto
    4. LLAMADA A MÉTODOS: Ejecutar funciones del objeto
    5. ABSTRACCIÓN: La complejidad está oculta en la clase
    6. ENCAPSULACIÓN: Los datos están agrupados en la clase

Comparación con Programa Tradicional:
    TRADICIONAL: 1 archivo con funciones y variables globales
    POO:         2 archivos: clase (mascota.py) y main (main.py)
================================================================================
"""

# ============================================================================
# IMPORTACIÓN DE MÓDULOS
# ============================================================================
# Importar la clase Mascota desde el archivo mascota.py
# Con esto tenemos acceso a la clase para crear objetos
from mascota import Mascota


def main():
    """
    ========================================================================
    FUNCIÓN PRINCIPAL: main()
    ========================================================================

    Propósito:
        Demostrar de forma práctica todos los conceptos de POO.
        Crear objetos, acceder a sus atributos y ejecutar sus métodos.

    Estructura:
        1. Crear objetos (instancias de la clase Mascota)
        2. Mostrar atributos de los objetos
        3. Ejecutar métodos
        4. Modificar atributos mediante métodos
        5. Resumen de conceptos POO demostrados
    ========================================================================
    """

    print("\n" + "="*50)
    print("DEMO: PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("Sistema de Mascotas")
    print("="*50)

    # ========================================================================
    # [1] CREACIÓN DE OBJETOS (INSTANCIAS)
    # ========================================================================
    # INSTANCIA = Un objeto específico creado a partir de una clase
    # Sintaxis: nombre_objeto = NombreClase(parámetros)
    #
    # Cada objeto creado es INDEPENDIENTE:
    # - mascota1 tiene sus propios valores de atributos
    # - mascota2 tiene sus propios valores de atributos (diferentes)
    # - mascota3 tiene sus propios valores de atributos (diferentes)
    #
    # Aunque todos son de la MISMA CLASE (Mascota), son objetos DISTINTOS
    # ========================================================================

    print("\n[1] Creando objetos de la clase Mascota:")
    print("-" * 50)

    # Objeto 1: Perro
    mascota1 = Mascota("Max", "Perro", 5)
    print(f"✓ Objeto creado: {mascota1.obtener_descripcion()}")

    # Objeto 2: Gato
    mascota2 = Mascota("Mittens", "Gato", 3)
    print(f"✓ Objeto creado: {mascota2.obtener_descripcion()}")

    # Objeto 3: Pájaro (ejemplo adicional)
    mascota3 = Mascota("Tweety", "Pájaro", 2)
    print(f"✓ Objeto creado: {mascota3.obtener_descripcion()}")

    # ========================================================================
    # [2] ACCESO A ATRIBUTOS
    # ========================================================================
    # ATRIBUTO = Una característica o propiedad de un objeto
    # Se accede mediante: objeto.nombre_atributo
    #
    # Cada objeto tiene sus PROPIOS valores de atributos:
    # - mascota1.nombre = "Max" (diferente de mascota2.nombre = "Mittens")
    # - mascota1.edad = 5 (diferente de mascota3.edad = 2)
    #
    # Los atributos se inicializan en el CONSTRUCTOR (__init__)
    # ========================================================================

    print("\n" + "="*50)
    print("[2] Atributos de los objetos:")
    print("="*50)

    print(f"\nAtributos de mascota1:")
    print(f"  - nombre: {mascota1.nombre}")      # Acceso a atributo nombre
    print(f"  - especie: {mascota1.especie}")    # Acceso a atributo especie
    print(f"  - edad: {mascota1.edad}")          # Acceso a atributo edad

    # ========================================================================
    # [3] LLAMADA A MÉTODOS: mostrar_informacion()
    # ========================================================================
    # MÉTODO = Una función que pertenece a una clase/objeto
    # Se ejecuta mediante: objeto.nombre_metodo()
    #
    # Los métodos pueden:
    # - Mostrar información (como mostrar_informacion)
    # - Modificar atributos (como envejecer)
    # - Retornar valores
    #
    # Este método muestra toda la información del objeto de forma organizada
    # ========================================================================

    print("\n" + "="*50)
    print("[3] Ejecutando métodos: mostrar_informacion()")
    print("="*50)

    mascota1.mostrar_informacion()
    mascota2.mostrar_informacion()
    mascota3.mostrar_informacion()

    # ========================================================================
    # [4] ABSTRACCIÓN Y POLIMORFISMO
    # ========================================================================
    # ABSTRACCIÓN: Ocultar complejidad detrás de una interfaz simple
    #   - El usuario solo llama: mascota.hacer_sonido()
    #   - No ve la lógica interna (el diccionario de sonidos)
    #   - No necesita saber CÓMO se decide el sonido
    #
    # POLIMORFISMO: Un mismo método se comporta diferente según el objeto
    #   - mascota1 (Perro).hacer_sonido() → "Guau guau"
    #   - mascota2 (Gato).hacer_sonido() → "Miau"
    #   - mascota3 (Pájaro).hacer_sonido() → "Pío pío"
    #   - Mismo método, diferentes comportamientos
    # ========================================================================

    print("\n" + "="*50)
    print("[4] Ejecutando métodos: hacer_sonido()")
    print("="*50)

    mascota1.hacer_sonido()
    mascota2.hacer_sonido()
    mascota3.hacer_sonido()

    # ========================================================================
    # [5] MODIFICACIÓN DE ATRIBUTOS MEDIANTE MÉTODOS
    # ========================================================================
    # Los métodos pueden MODIFICAR los atributos del objeto
    # Esto se demuestra con envejecer() que incrementa la edad
    # y cambiar_nombre() que modifica el nombre
    # ========================================================================

    print("\n" + "="*50)
    print("[5] Ejecutando otros métodos:")
    print("="*50)

    # Método envejecer: modifica el atributo edad
    mascota1.envejecer()

    # Método cambiar_nombre: modifica el atributo nombre
    mascota2.cambiar_nombre("Luna")

    # ========================================================================
    # [6] INFORMACIÓN ACTUALIZADA DESPUÉS DE MODIFICACIONES
    # ========================================================================
    # Como los atributos fueron modificados, ahora tienen diferentes valores
    # mascota1.edad cambió de 5 a 6
    # mascota2.nombre cambió de "Mittens" a "Luna"
    # ========================================================================

    print("\n[6] Información actualizada:")
    print("-" * 50)

    print(f"\nDescripción actualizada de mascota1:")
    print(f"  {mascota1.obtener_descripcion()}")

    print(f"\nDescripción actualizada de mascota2:")
    print(f"  {mascota2.obtener_descripcion()}")

    # ========================================================================
    # [7] RESUMEN - CONCEPTOS POO DEMOSTRADOS
    # ========================================================================
    print("\n" + "="*50)
    print("[RESUMEN - CONCEPTOS DE POO DEMOSTRADOS]")
    print("="*50)

    print("""
1. CLASE: Mascota
   Definición: Plantilla o molde para crear objetos
   Propósito: Define la estructura y comportamiento común
   Uso: class Mascota:
   
2. OBJETOS: mascota1, mascota2, mascota3
   Definición: Instancias específicas de la clase
   Propósito: Representar mascotas individuales
   Uso: mascota1 = Mascota("Max", "Perro", 5)
   
3. ATRIBUTOS: nombre, especie, edad
   Definición: Características de cada objeto
   Propósito: Almacenar datos del objeto
   Acceso: objeto.nombre / objeto.especie / objeto.edad
   
4. MÉTODOS: mostrar_informacion(), hacer_sonido(), etc.
   Definición: Funciones asociadas a la clase
   Propósito: Definir comportamiento del objeto
   Ejecución: objeto.metodo()
   
5. CONSTRUCTOR (__init__):
   Definición: Método especial que se ejecuta al crear un objeto
   Propósito: Inicializar los atributos
   Parámetro especial: self (representa la instancia actual)
   
6. ENCAPSULACIÓN:
   Definición: Agrupar datos (atributos) y comportamiento (métodos)
   Propósito: Organizar código relacionado en una unidad cohesiva
   Ventaja: Fácil de mantener y usar
   
7. ABSTRACCIÓN:
   Definición: Ocultar complejidad detrás de interfaz simple
   Ejemplo: mascota.hacer_sonido() (no mostrar la lógica interna)
   Ventaja: Usuario usa sin necesidad de comprender la implementación
   
8. POLIMORFISMO:
   Definición: Un mismo método se comporta diferente según el objeto
   Ejemplo: hacer_sonido() produce sonidos diferentes por especie
   Ventaja: Código flexible y reutilizable
   
9. HERENCIA (No implementada en este ejemplo):
   Definición: Crear nuevas clases basadas en clases existentes
   Ejemplo: class Gato(Mascota): ...
   Ventaja: Reutilización de código mediante jerarquías
    """)

    print("="*50)
    print("✓ ¡Fin de la demostración!")
    print("="*50 + "\n")


# ============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================================
# En Python, se verifica si el archivo se ejecuta directamente o se importa
# __name__ == "__main__" es True solo cuando el archivo se ejecuta directamente
# Esto permite usar este módulo como biblioteca en otros programas
if __name__ == "__main__":
    main()





