"""
Archivo principal del sistema de restaurante.
Implementa un menu interactivo que permite registrar y listar productos, bebidas y clientes.
Coordina la interaccion entre el usuario y el servicio Restaurante.
"""

from modelos import Producto, Bebida, Cliente
from servicios import Restaurante


def mostrar_menu() -> None:
    """Muestra el menu principal del sistema."""
    print("\n" + "=" * 50)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 50)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-" * 50)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-" * 50)
    print("6. Salir")
    print("=" * 50)


def registrar_producto(restaurante: Restaurante) -> None:
    """
    Solicita datos al usuario y registra un nuevo producto.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- Registrar Nuevo Producto ---")
    try:
        codigo = input("Codigo del producto: ").strip()
        nombre = input("Nombre del producto: ").strip()
        categoria = input("Categoria (ej: Comida, Acompañamientos): ").strip()
        precio = float(input("Precio (ej: 10.50): "))

        # Crear objeto Producto mediante constructor
        producto = Producto(codigo, nombre, categoria, precio)
        
        # Registrar en el servicio
        if restaurante.registrar_producto(producto):
            print("[OK] Producto '{}' registrado exitosamente.".format(nombre))
        else:
            print("[ADVERTENCIA] Ya existe un producto con codigo '{}'.".format(codigo))

    except ValueError as e:
        print("[ERROR] {}".format(e))
    except Exception as e:
        print("[ERROR] Error inesperado: {}".format(e))


def registrar_bebida(restaurante: Restaurante) -> None:
    """
    Solicita datos al usuario y registra una nueva bebida.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- Registrar Nueva Bebida ---")
    try:
        codigo = input("Codigo de la bebida: ").strip()
        nombre = input("Nombre de la bebida: ").strip()
        categoria = input("Categoria (ej: Bebidas Frias, Bebidas Calientes): ").strip()
        precio = float(input("Precio (ej: 3.50): "))
        tamaño = input("Tamaño (ej: Pequeño, Mediano, Grande): ").strip()
        tipo_envase = input("Tipo de envase (ej: Botella, Lata, Vaso): ").strip()

        # Crear objeto Bebida mediante constructor
        bebida = Bebida(codigo, nombre, categoria, precio, tamaño, tipo_envase)
        
        # Registrar en el servicio
        if restaurante.registrar_producto(bebida):
            print("[OK] Bebida '{}' registrada exitosamente.".format(nombre))
        else:
            print("[ADVERTENCIA] Ya existe una bebida con codigo '{}'.".format(codigo))

    except ValueError as e:
        print("[ERROR] {}".format(e))
    except Exception as e:
        print("[ERROR] Error inesperado: {}".format(e))


def registrar_cliente(restaurante: Restaurante) -> None:
    """
    Solicita datos al usuario y registra un nuevo cliente.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- Registrar Nuevo Cliente ---")
    try:
        identificacion = input("Identificacion del cliente: ").strip()
        nombre = input("Nombre del cliente: ").strip()
        correo = input("Correo electronico: ").strip()

        # Crear objeto Cliente mediante constructor
        cliente = Cliente(identificacion, nombre, correo)
        
        # Registrar en el servicio
        if restaurante.registrar_cliente(cliente):
            print("[OK] Cliente '{}' registrado exitosamente.".format(nombre))
        else:
            print("[ADVERTENCIA] Ya existe un cliente con identificacion '{}'.".format(identificacion))

    except ValueError as e:
        print("[ERROR] {}".format(e))
    except Exception as e:
        print("[ERROR] Error inesperado: {}".format(e))


def listar_productos(restaurante: Restaurante) -> None:
    """
    Lista todos los productos y bebidas registrados en el restaurante.
    Demuestra polimorfismo: cada objeto usa su propio mostrar_informacion().
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- Lista de Productos y Bebidas ---")
    productos = restaurante.listar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    print("Total de productos: {}\n".format(restaurante.obtener_total_productos()))
    for idx, producto in enumerate(productos, 1):
        print("{}. {}".format(idx, producto))
        print("   {}".format(producto.mostrar_informacion()))
        print()


def listar_clientes(restaurante: Restaurante) -> None:
    """
    Lista todos los clientes registrados en el restaurante.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- Lista de Clientes ---")
    clientes = restaurante.listar_clientes()

    if not clientes:
        print("No hay clientes registrados.")
        return

    print("Total de clientes: {}\n".format(restaurante.obtener_total_clientes()))
    for idx, cliente in enumerate(clientes, 1):
        print("{}. {}".format(idx, cliente))
        print("   {}".format(cliente.mostrar_informacion()))
        print()


def main() -> None:
    """
    Funcion principal que ejecuta el sistema de restaurante.
    Muestra un menu interactivo y procesa las opciones del usuario.
    """
    # Crear instancia del restaurante
    restaurante = Restaurante(nombre="Restaurante SEMANA_8")

    print("\n[BIENVENIDA] Bienvenido al Sistema de Restaurante!")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            registrar_bebida(restaurante)
        elif opcion == "3":
            registrar_cliente(restaurante)
        elif opcion == "4":
            listar_productos(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            print("\n[SALIDA] Gracias por usar el Sistema de Restaurante! Hasta luego.")
            break
        else:
            print("[ERROR] Opcion no valida. Por favor, seleccione una opcion del 1 al 6.")


if __name__ == "__main__":
    main()
