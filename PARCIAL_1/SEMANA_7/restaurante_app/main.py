"""
Archivo principal del sistema de restaurante.
Implementa un menú interactivo que permite al usuario registrar, listar y buscar
productos y clientes mediante entrada de datos desde consola.
"""

from modelos import Producto, Cliente
from servicios import Restaurante


def mostrar_menu() -> None:
    """Muestra el menú principal del sistema."""
    print("\n" + "=" * 50)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 50)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 50)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 50)
    print("7. Salir")
    print("=" * 50)


def registrar_producto(restaurante: Restaurante) -> None:
    """
    Solicita datos al usuario y registra un nuevo producto.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- Registrar Nuevo Producto ---")
    try:
        nombre = input("Nombre del producto: ").strip()
        categoria = input("Categoria (ej: Bebidas, Comida, Postres): ").strip()
        precio = float(input("Precio (ej: 5.99): "))
        disponible = input("[S/N] Disponible? (por defecto 's'): ").strip().lower() != 'n'

        # Crear objeto Producto mediante constructor
        producto = Producto(nombre, categoria, precio, disponible)
        restaurante.registrar_producto(producto)

    except ValueError as e:
        print("[ERROR] {}".format(e))
    except Exception as e:
        print("[ERROR] Error inesperado: {}".format(e))


def listar_productos(restaurante: Restaurante) -> None:
    """
    Lista todos los productos registrados en el restaurante.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- Lista de Productos ---")
    productos = restaurante.listar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    print("Total de productos: {}\n".format(restaurante.obtener_total_productos()))
    for idx, producto in enumerate(productos, 1):
        print("{}. {}".format(idx, producto))
        print("   {}\n".format(producto.mostrar_informacion()))


def buscar_producto(restaurante: Restaurante) -> None:
    """
    Busca un producto por nombre.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- Buscar Producto ---")
    nombre_busqueda = input("Ingrese el nombre del producto a buscar: ").strip()

    producto = restaurante.buscar_producto(nombre_busqueda)

    if producto:
        print("\n[OK] Producto encontrado:\n")
        print(producto.mostrar_informacion())
    else:
        print("[ADVERTENCIA] No se encontro producto con el nombre '{}'.".format(nombre_busqueda))


def registrar_cliente(restaurante: Restaurante) -> None:
    """
    Solicita datos al usuario y registra un nuevo cliente.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- Registrar Nuevo Cliente ---")
    try:
        nombre = input("Nombre del cliente: ").strip()
        correo = input("Correo electrónico: ").strip()
        id_cliente = input("ID del cliente: ").strip()

        # Crear objeto Cliente mediante constructor (@dataclass)
        cliente = Cliente(nombre=nombre, correo=correo, id_cliente=id_cliente)
        restaurante.registrar_cliente(cliente)

    except Exception as e:
        print(f"❌ Error: {e}")


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
        print("   {}\n".format(cliente.mostrar_informacion()))


def buscar_cliente(restaurante: Restaurante) -> None:
    """
    Busca un cliente por nombre.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- Buscar Cliente ---")
    nombre_busqueda = input("Ingrese el nombre del cliente a buscar: ").strip()

    cliente = restaurante.buscar_cliente(nombre_busqueda)

    if cliente:
        print("\n[OK] Cliente encontrado:\n")
        print(cliente.mostrar_informacion())
    else:
        print("[ADVERTENCIA] No se encontro cliente con el nombre '{}'.".format(nombre_busqueda))


def main() -> None:
    """
    Función principal que ejecuta el sistema de restaurante.
    Muestra un menú interactivo y procesa las opciones del usuario.
    """
    # Crear instancia del restaurante
    restaurante = Restaurante(nombre="Restaurante Mi Casa")

    print("\n[BIENVENIDA] Bienvenido al Sistema de Restaurante!")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            listar_productos(restaurante)
        elif opcion == "3":
            buscar_producto(restaurante)
        elif opcion == "4":
            registrar_cliente(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            buscar_cliente(restaurante)
        elif opcion == "7":
            print("\n[SALIDA] Gracias por usar el Sistema de Restaurante! Hasta luego.")
            break
        else:
            print("[ERROR] Opcion no valida. Por favor, seleccione una opcion del 1 al 7.")


if __name__ == "__main__":
    main()
