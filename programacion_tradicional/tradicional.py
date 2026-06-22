"""
================================================================================
PROGRAMA 1: SISTEMA DE REGISTRO DE MASCOTAS - PROGRAMACIÓN TRADICIONAL
================================================================================

Descripción:
    Solución que utiliza VARIABLES y FUNCIONES para gestionar información
    de mascotas sin usar clases ni objetos.

Paradigma de Programación:
    - Programación PROCEDURAL/ESTRUCTURADA (Tradicional)
    - No utiliza orientación a objetos
    - Usa funciones y variables globales

Elementos Utilizados:
    ✓ Variables globales (mascotas)
    ✓ Funciones (registrar, mostrar, buscar, eliminar, etc.)
    ✓ Estructuras de datos (listas y diccionarios)
    ✓ Entradas/salidas por teclado

Ventajas:
    • Simple y directo de entender
    • Bajo acoplamiento inicial
    • Ideal para programas pequeños
    • Fácil de depurar

Desventajas:
    • Difícil mantener en proyectos grandes
    • Código repetitivo
    • Poca reutilización de código
    • Variables globales problemáticas en escalas grandes
================================================================================
"""

# ============================================================================
# VARIABLES GLOBALES
# ============================================================================
# Lista global que almacena TODAS las mascotas como diccionarios
# Esta es una estructura simple (lista de diccionarios) sin usar clases
mascotas = []


def registrar_mascota():
    """
    FUNCIÓN: registrar_mascota()

    Propósito:
        Registra una nueva mascota solicitando datos por teclado.
        Estos datos se almacenan en un DICCIONARIO.

    Proceso:
        1. Solicita datos del usuario (nombre, tipo, edad, raza, color, peso)
        2. Valida que los datos sean correctos
        3. Crea un diccionario con los datos
        4. Agrega el diccionario a la lista global 'mascotas'

    Parámetros: Ninguno
    Retorna: Ninguno (modifica la variable global 'mascotas')

    Nota: Este es el enfoque tradicional sin usar clases.
          En POO, esto sería un método de una clase Mascota.
    """
    print("\n" + "="*50)
    print("REGISTRAR NUEVA MASCOTA")
    print("="*50)

    # ========== ENTRADA DE DATOS POR TECLADO ==========
    # En programación tradicional, solicitamos datos directamente
    nombre = input("Ingrese el nombre de la mascota: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    tipo = input("Ingrese el tipo de mascota (perro, gato, pájaro, etc.): ").strip()
    if not tipo:
        print("Error: El tipo no puede estar vacío.")
        return

    # Validación de entrada: convertir a número entero
    try:
        edad = int(input("Ingrese la edad de la mascota (en años): "))
        if edad < 0:
            print("Error: La edad no puede ser negativa.")
            return
    except ValueError:
        print("Error: La edad debe ser un número entero.")
        return

    raza = input("Ingrese la raza de la mascota: ").strip()
    if not raza:
        raza = "No especificada"

    color = input("Ingrese el color de la mascota: ").strip()
    if not color:
        color = "No especificado"

    peso = input("Ingrese el peso de la mascota (en kg): ").strip()
    if not peso:
        peso = "No especificado"
    else:
        try:
            peso = float(peso)
        except ValueError:
            peso = "Inválido"

    # ========== CREACIÓN DE ESTRUCTURA DE DATOS ==========
    # En lugar de usar un objeto (como en POO), usamos un DICCIONARIO
    # La clave es un string y el valor es la información
    mascota = {
        "nombre": nombre,      # Atributo: nombre
        "tipo": tipo,          # Atributo: tipo/especie
        "edad": edad,          # Atributo: edad
        "raza": raza,          # Atributo: raza
        "color": color,        # Atributo: color
        "peso": peso           # Atributo: peso
    }

    # ========== ALMACENAMIENTO EN VARIABLE GLOBAL ==========
    # Agregamos el diccionario a la lista global 'mascotas'
    # Esto permite guardar múltiples mascotas
    mascotas.append(mascota)
    print(f"\n✓ ¡Mascota '{nombre}' registrada correctamente!")


def mostrar_todas_mascotas():
    """
    FUNCIÓN: mostrar_todas_mascotas()

    Propósito:
        Muestra la información de TODAS las mascotas registradas
        de forma organizada y fácil de leer.

    Processo:
        1. Verifica si la lista 'mascotas' tiene elementos
        2. Itera sobre cada mascota en la lista
        3. Llama a mostrar_mascota_individual para cada una

    En POO, esto sería similar a un método de iteración sobre objetos.
    """
    print("\n" + "="*50)
    print("LISTADO DE MASCOTAS REGISTRADAS")
    print("="*50)

    # Validación: verificar si hay mascotas registradas
    if not mascotas:
        print("\nNo hay mascotas registradas.")
        return

    # Iterar sobre cada mascota (diccionario) en la lista
    for indice, mascota in enumerate(mascotas, 1):
        # Llamar a función para mostrar cada mascota individual
        mostrar_mascota_individual(mascota, indice)


def mostrar_mascota_individual(mascota, numero=None):
    """
    FUNCIÓN: mostrar_mascota_individual()

    Propósito:
        Muestra la información de UNA mascota de forma organizada.
        Recibe un DICCIONARIO con los datos de la mascota.

    Parámetros:
        mascota (dict): Diccionario con los datos de la mascota
        numero (int): Número de orden (opcional)

    En POO, esto sería similar al método mostrar_informacion() de una clase.
    """
    # Mostrar número de mascota si se proporciona
    if numero:
        print(f"\n--- MASCOTA {numero} ---")
    else:
        print("\n" + "-"*40)

    # Acceder a los valores del diccionario usando sus claves
    # En POO, accedemos a atributos como objeto.nombre
    # Aquí accedemos como diccionario['clave']
    print(f"Nombre:  {mascota['nombre']}")
    print(f"Tipo:    {mascota['tipo']}")
    print(f"Edad:    {mascota['edad']} años")
    print(f"Raza:    {mascota['raza']}")
    print(f"Color:   {mascota['color']}")

    # Validación de tipo de dato para el peso
    if isinstance(mascota['peso'], (int, float)):
        print(f"Peso:    {mascota['peso']} kg")
    else:
        print(f"Peso:    {mascota['peso']}")

    print("-"*40)


def buscar_mascota_por_nombre():
    """
    Busca una mascota por su nombre y muestra su información.
    """
    print("\n" + "="*50)
    print("BUSCAR MASCOTA POR NOMBRE")
    print("="*50)

    if not mascotas:
        print("\nNo hay mascotas registradas.")
        return

    nombre_buscar = input("\nIngrese el nombre de la mascota a buscar: ").strip().lower()

    encontrada = False
    for mascota in mascotas:
        if mascota['nombre'].lower() == nombre_buscar:
            print(f"\n✓ Mascota encontrada:")
            mostrar_mascota_individual(mascota)
            encontrada = True
            break

    if not encontrada:
        print(f"\n✗ No se encontró una mascota con el nombre '{nombre_buscar}'.")


def contar_mascotas_por_tipo():
    """
    Cuenta y muestra cuántas mascotas hay por tipo.
    """
    print("\n" + "="*50)
    print("CANTIDAD DE MASCOTAS POR TIPO")
    print("="*50)

    if not mascotas:
        print("\nNo hay mascotas registradas.")
        return

    tipos = {}
    for mascota in mascotas:
        tipo = mascota['tipo']
        if tipo in tipos:
            tipos[tipo] += 1
        else:
            tipos[tipo] = 1

    print("\n")
    for tipo, cantidad in sorted(tipos.items()):
        print(f"  {tipo.capitalize()}: {cantidad}")

    print(f"\nTotal de mascotas: {len(mascotas)}")


def calcular_edad_promedio():
    """
    Calcula y muestra la edad promedio de las mascotas.
    """
    print("\n" + "="*50)
    print("EDAD PROMEDIO DE MASCOTAS")
    print("="*50)

    if not mascotas:
        print("\nNo hay mascotas registradas.")
        return

    suma_edades = sum(mascota['edad'] for mascota in mascotas)
    edad_promedio = suma_edades / len(mascotas)

    print(f"\nEdad promedio: {edad_promedio:.2f} años")


def eliminar_mascota():
    """
    Elimina una mascota por su nombre.
    """
    print("\n" + "="*50)
    print("ELIMINAR MASCOTA")
    print("="*50)

    if not mascotas:
        print("\nNo hay mascotas registradas.")
        return

    nombre_eliminar = input("\nIngrese el nombre de la mascota a eliminar: ").strip().lower()

    for indice, mascota in enumerate(mascotas):
        if mascota['nombre'].lower() == nombre_eliminar:
            nombre_mascota = mascota['nombre']
            mascotas.pop(indice)
            print(f"\n✓ Mascota '{nombre_mascota}' eliminada correctamente.")
            return

    print(f"\n✗ No se encontró una mascota con el nombre '{nombre_eliminar}'.")


def mostrar_menu():
    """
    Muestra el menú principal del programa.
    """
    print("\n" + "="*50)
    print("SISTEMA DE REGISTRO DE MASCOTAS")
    print("="*50)
    print("\n1. Registrar nueva mascota")
    print("2. Mostrar todas las mascotas")
    print("3. Buscar mascota por nombre")
    print("4. Ver cantidad de mascotas por tipo")
    print("5. Calcular edad promedio")
    print("6. Eliminar mascota")
    print("7. Salir")
    print("\n" + "="*50)


def main():
    """
    FUNCIÓN PRINCIPAL: main()
    
    Propósito:
        Controla el flujo principal del programa.
        Muestra un menú interactivo y ejecuta las funciones según la selección.
    
    Flujo:
        1. Muestra el menú
        2. Lee la opción del usuario
        3. Llama a la función correspondiente
        4. Repite hasta que el usuario elige "Salir"
    
    Este es el enfoque PROCEDIMENTAL/ESTRUCTURADO:
    - El programa es un flujo lineal de funciones
    - No hay encapsulación de datos en objetos
    - Las funciones operan sobre variables globales
    
    Comparación con POO:
    - En POO, el flujo estaría controlado por clases
    - Los datos estarían encapsulados en objetos
    - Las funciones serían métodos de clases
    """
    print("\n¡Bienvenido al Sistema de Registro de Mascotas!")
    print("(Versión Tradicional - Sin Objetos)\n")
    
    # Bucle principal - continúa hasta que se selecciona "Salir"
    while True:
        # Mostrar opciones disponibles
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-7): ").strip()
        
        # Estructura condicional para ejecutar función según opción
        if opcion == "1":
            registrar_mascota()
        elif opcion == "2":
            mostrar_todas_mascotas()
        elif opcion == "3":
            buscar_mascota_por_nombre()
        elif opcion == "4":
            contar_mascotas_por_tipo()
        elif opcion == "5":
            calcular_edad_promedio()
        elif opcion == "6":
            eliminar_mascota()
        elif opcion == "7":
            print("\n¡Gracias por usar el Sistema de Registro de Mascotas!")
            print("¡Hasta luego!\n")
            # Salir del bucle y terminar el programa
            break
        else:
            print("\n✗ Opción no válida. Por favor, seleccione una opción entre 1 y 7.")


# ============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================================
# En Python, se verifica si el archivo se ejecuta directamente o se importa
if __name__ == "__main__":
    main()




