# Punto de entrada del programa - Main
# Aquí se crean objetos, se agregan al restaurante y se muestra el menú

from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def main():
    """Función principal del programa."""
    
    # Crear instancia del restaurante
    restaurante = Restaurante("El Sabor Plenario")
    
    # Crear platillos
    # Cada Platillo hereda de Producto y agrega atributos específicos
    platillo1 = Platillo(
        nombre="Lomo a la Pimienta",
        precio=45.99,
        tipo_platillo="Plato Fuerte",
        tiempo_preparacion=20,
        calorias=650
    )
    
    platillo2 = Platillo(
        nombre="Ensalada César",
        precio=18.50,
        tipo_platillo="Entrada",
        tiempo_preparacion=10,
        calorias=320
    )
    
    platillo3 = Platillo(
        nombre="Tiramisú",
        precio=12.00,
        tipo_platillo="Postre",
        tiempo_preparacion=5,
        calorias=380
    )
    
    # Crear bebidas
    # Cada Bebida hereda de Producto y agrega atributos específicos
    bebida1 = Bebida(
        nombre="Coca Cola",
        precio=3.50,
        volumen_ml=350,
        tipo_bebida="Gaseosa",
        temperatura="Fría"
    )
    
    bebida2 = Bebida(
        nombre="Café Americano",
        precio=4.00,
        volumen_ml=240,
        tipo_bebida="Café",
        temperatura="Caliente"
    )
    
    bebida3 = Bebida(
        nombre="Jugo Natural de Naranja",
        precio=5.75,
        volumen_ml=400,
        tipo_bebida="Jugo Natural",
        temperatura="Fría"
    )
    
    # Agregar productos al restaurante
    restaurante.agregar_producto(platillo1)
    restaurante.agregar_producto(platillo2)
    restaurante.agregar_producto(platillo3)
    restaurante.agregar_producto(bebida1)
    restaurante.agregar_producto(bebida2)
    restaurante.agregar_producto(bebida3)
    
    # Mostrar el menú completo (demostrando polimorfismo)
    # El método mostrar_informacion() se ejecuta diferente para cada tipo de producto
    restaurante.mostrar_menu_completo()
    
    # Demostración de encapsulación y métodos de acceso
    print("=" * 50)
    print("DEMOSTRACIONES DE ENCAPSULACIÓN")
    print("=" * 50)
    
    print(f"\nPrecio actual del Lomo a la Pimienta: ${platillo1.obtener_precio():.2f}")
    print("Cambiando precio a $52.99...")
    platillo1.cambiar_precio(52.99)
    print(f"Nuevo precio: ${platillo1.obtener_precio():.2f}")
    
    # Intentar cambiar a un precio inválido
    print("\nIntentando cambiar precio a -10 (inválido)...")
    try:
        platillo1.cambiar_precio(-10)
    except ValueError as e:
        print(f"Error capturado: {e}")
    
    # Información de productos disponibles
    print("\n" + "=" * 50)
    print("PRODUCTOS DISPONIBLES")
    print("=" * 50 + "\n")
    disponibles = restaurante.listar_productos_disponibles()
    print(f"Cantidad de productos disponibles: {len(disponibles)}")
    
    # Buscar un producto específico
    print("\n" + "=" * 50)
    print("BÚSQUEDA DE PRODUCTO")
    print("=" * 50 + "\n")
    producto_buscado = restaurante.buscar_producto_por_nombre("Café Americano")
    if producto_buscado:
        print(f"Producto encontrado: {producto_buscado.nombre}")
        print(f"Precio: ${producto_buscado.obtener_precio():.2f}")
    
    # Precio promedio
    print("\n" + "=" * 50)
    print("ANÁLISIS DE PRECIOS")
    print("=" * 50 + "\n")
    promedio = restaurante.obtener_precio_promedio()
    print(f"Precio promedio de todos los productos: ${promedio:.2f}")


if __name__ == "__main__":
    main()
