# Punto de entrada del sistema de gestión de restaurante
# Importa los modelos y servicios necesarios


from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main() -> None:
    """Función principal que ejecuta el programa."""
    
    # Crear instancia del restaurante
    mi_restaurante = Restaurante(
        nombre_restaurante="Sabor Authentic",
        ubicacion="Calle Principal 123, Centro Comercial"
    )
    
    # Mostrar información general
    mi_restaurante.mostrar_informacion_general()
    
    # =====================================================
    # CREAR PRODUCTOS
    # =====================================================
    print("Creando productos...\n")
    
    # Producto 1: Entrada
    arepa_con_queso = Producto(
        identificador=1001,
        nombre="Arepa con Queso",
        descripcion="Arepa tradicional rellena de queso fresco de la región",
        precio=8500.00,
        disponible=True
    )
    
    # Producto 2: Plato Principal
    bandeja_paisa = Producto(
        identificador=1002,
        nombre="Bandeja Paisa",
        descripcion="Plato típico compuesto por frijoles, arroz, carne molida y más",
        precio=28000.00,
        disponible=True
    )
    
    # Producto 3: Bebida
    jugo_natural = Producto(
        identificador=1003,
        nombre="Jugo Natural de Frutas",
        descripcion="Jugo fresco preparado diariamente con frutas de la temporada",
        precio=6500.00,
        disponible=True
    )
    
    # Producto 4: Postre
    flan_casero = Producto(
        identificador=1004,
        nombre="Flan Casero",
        descripcion="Flan tradicional preparado con caramelo y vainilla",
        precio=7000.00,
        disponible=False
    )
    
    # Agregar productos al restaurante
    mi_restaurante.agregar_producto(arepa_con_queso)
    mi_restaurante.agregar_producto(bandeja_paisa)
    mi_restaurante.agregar_producto(jugo_natural)
    mi_restaurante.agregar_producto(flan_casero)
    
    # =====================================================
    # CREAR CLIENTES
    # =====================================================
    print("\nCreando clientes...\n")
    
    # Cliente 1: Cliente frecuente
    cliente_uno = Cliente(
        identificador=123456,
        nombre_completo="Carlos Rodríguez García",
        numero_contacto="3015672345",
        correo_electronico="carlos.rodriguez@email.com",
        es_cliente_frecuente=True,
        saldo_disponible=150000.00
    )
    
    # Cliente 2: Cliente regular
    cliente_dos = Cliente(
        identificador=789012,
        nombre_completo="María López Martínez",
        numero_contacto="3109876543",
        correo_electronico="maria.lopez@email.com",
        es_cliente_frecuente=False,
        saldo_disponible=75000.00
    )
    
    # Agregar clientes al restaurante
    mi_restaurante.agregar_cliente(cliente_uno)
    mi_restaurante.agregar_cliente(cliente_dos)
    
    # =====================================================
    # MOSTRAR INFORMACIÓN DEL SISTEMA
    # =====================================================
    
    # Listar todos los productos
    mi_restaurante.listar_productos()
    
    # Listar todos los clientes
    mi_restaurante.listar_clientes()
    
    # =====================================================
    # OPERACIONES ADICIONALES DEMOSTRATIVAS
    # =====================================================
    print(f"{'='*80}")
    print("OPERACIONES ADICIONALES DEL SISTEMA")
    print(f"{'='*80}\n")
    
    # Buscar un producto específico
    producto_buscado = mi_restaurante.obtener_producto_por_id(1002)
    if producto_buscado:
        print(f"Producto encontrado: {producto_buscado}\n")
    
    # Buscar un cliente específico
    cliente_buscado = mi_restaurante.obtener_cliente_por_id(123456)
    if cliente_buscado:
        print(f"Cliente encontrado: {cliente_buscado}\n")
    
    # Mostrar productos disponibles para venta
    print(f"Productos disponibles para venta:")
    for producto in mi_restaurante.productos_disponibles_para_venta():
        print(f"  - {producto.obtener_informacion_resumida()}")
    print()
    
    # Mostrar clientes frecuentes
    print(f"Clientes frecuentes:")
    for cliente in mi_restaurante.clientes_frecuentes():
        print(f"  - {cliente.obtener_informacion_contacto()}")
    print()
    
    # Cambiar estado de disponibilidad de un producto
    print("Actualizando disponibilidad del flan...")
    flan_casero.cambiar_disponibilidad(True)
    print(f"Nuevo estado: {flan_casero}\n")
    
    # Actualizar precio de un producto
    print("Actualizando precio de la arepa con queso...")
    arepa_con_queso.actualizar_precio(9000.00)
    print(f"Nuevo precio: ${arepa_con_queso.precio:.2f}\n")
    
    # Actualizar saldo de un cliente
    print("Realizando transacción con cliente...")
    monto_compra = 50000.00
    if cliente_uno.validar_saldo(monto_compra):
        cliente_uno.actualizar_saldo(-monto_compra)
        print(f"Compra exitosa. Nuevo saldo: ${cliente_uno.saldo_disponible:.2f}\n")
    
    # Mostrar información final
    mi_restaurante.mostrar_informacion_general()
    
    print(f"{'='*80}")
    print("FIN DEL PROGRAMA - SISTEMA DE GESTIÓN DE RESTAURANTE")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    main()
