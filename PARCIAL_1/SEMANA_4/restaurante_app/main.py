"""
Punto de entrada del sistema de restaurante.

Desde aquí se crean productos, clientes y se simulan pedidos para demostrar
el funcionamiento del sistema. Ejecute este archivo para ver la salida en consola.
"""
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    # Crear servicio principal
    restaurante = Restaurante("La Buena Mesa")

    # Crear productos
    p1 = Producto(1, "Lomo Saltado", "plato", 12.50, "Plato tradicional peruano")
    p2 = Producto(2, "Jugo de Maracuyá", "bebida", 3.00, "Refrescante natural")
    p3 = Producto(3, "Ceviche", "plato", 10.00, "Ceviche de pescado fresco")

    # Registrar productos en el restaurante
    restaurante.registrar_producto(p1)
    restaurante.registrar_producto(p2)
    restaurante.registrar_producto(p3)

    # Crear clientes
    c1 = Cliente(1, "Ana Pérez", telefono="555-1234", mesa=5)
    c2 = Cliente(2, "Luis Gómez", telefono="555-5678")

    # Registrar clientes
    restaurante.registrar_cliente(c1)
    restaurante.registrar_cliente(c2)

    # Mostrar productos registrados
    print("--- Productos en el menú ---")
    for prod in restaurante.listar_productos():
        print(prod)

    # Crear pedidos
    total1 = restaurante.crear_pedido(1, [1, 2])  # Ana pide Lomo Saltado + Jugo
    total2 = restaurante.crear_pedido(2, [3])     # Luis pide Ceviche

    print()
    print(f"Pedido 1 (Cliente 1) total: ${total1:.2f}")
    print(f"Pedido 2 (Cliente 2) total: ${total2:.2f}")

    # Mostrar clientes y sus pedidos
    print()
    print("--- Clientes registrados ---")
    for cliente in restaurante.listar_clientes():
        print(cliente)

    print()
    print(restaurante.mostrar_pedidos_cliente(1))
    print()
    print(restaurante.mostrar_pedidos_cliente(2))


if __name__ == "__main__":
    main()

