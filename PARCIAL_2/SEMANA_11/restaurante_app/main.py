from __future__ import annotations
import os
import json
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

MENU_OPTIONS = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Vender producto",
    "9. Listar ventas por usuario",
    "10. Salir",
)

DATA_DIR = os.path.join(os.path.dirname(__file__), "datos")
archivo = ArchivoServicio(DATA_DIR)

# cargar datos
raw_products = []
raw_users = []
raw_sales = []
try:
    raw_products = archivo.cargar_productos()
    raw_users = archivo.cargar_usuarios()
    raw_sales = archivo.cargar_ventas()
except json.JSONDecodeError:
    print("Advertencia: alguno de los archivos JSON contiene formato inválido. Iniciando con colecciones vacías.")
except PermissionError:
    print("Error: sin permiso para leer archivos de datos. Iniciando con colecciones vacías.")

productos_iniciales = []
for rec in raw_products:
    try:
        productos_iniciales.append(Producto.from_dict(rec))
    except (KeyError, ValueError) as e:
        print(f"Registro de producto inválido omitido: {e}")

usuarios_iniciales = []
for rec in raw_users:
    try:
        usuarios_iniciales.append(Usuario.from_dict(rec))
    except (KeyError, ValueError) as e:
        print(f"Registro de usuario inválido omitido: {e}")

ventas_iniciales = []
for rec in raw_sales:
    try:
        ventas_iniciales.append(Venta.from_dict(rec))
    except (KeyError, ValueError) as e:
        print(f"Registro de venta inválido omitido: {e}")

restaurante = Restaurante(productos=productos_iniciales, usuarios=usuarios_iniciales, ventas=ventas_iniciales)

def guardar_todo() -> None:
    try:
        archivo.guardar_productos([p.to_dict() for p in restaurante.listar_productos()])
        archivo.guardar_usuarios([u.to_dict() for u in restaurante.listar_usuarios()])
        archivo.guardar_ventas([v.to_dict() for v in restaurante.listar_ventas()])
    except PermissionError:
        print("Error: no se pudieron guardar los datos (permiso denegado).")
    except Exception as e:
        print(f"Error al guardar datos: {e}")


def registrar_producto() -> None:
    try:
        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()
        precio_str = input("Precio: ").strip()
        stock_str = input("Stock: ").strip()
        precio = float(precio_str)
        stock = int(stock_str)
        prod = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio, stock=stock)
        restaurante.registrar_producto(prod)
        archivo.guardar_productos([p.to_dict() for p in restaurante.listar_productos()])
        print("Producto registrado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def buscar_producto() -> None:
    codigo = input("Código a buscar: ").strip()
    prod = restaurante.buscar_producto(codigo)
    if prod:
        print(prod)
    else:
        print("Producto no encontrado.")


def actualizar_producto() -> None:
    codigo = input("Código a actualizar: ").strip()
    prod = restaurante.buscar_producto(codigo)
    if not prod:
        print("Producto no encontrado.")
        return
    print(f"Producto actual: {prod}")
    nombre = input("Nuevo nombre (enter para mantener): ").strip() or None
    categoria = input("Nueva categoría (enter para mantener): ").strip() or None
    precio_input = input("Nuevo precio (enter para mantener): ").strip()
    precio = float(precio_input) if precio_input else None
    stock_input = input("Nuevo stock (enter para mantener): ").strip()
    stock = int(stock_input) if stock_input else None
    try:
        ok = restaurante.actualizar_producto(codigo, nombre=nombre, categoria=categoria, precio=precio, stock=stock)
        if ok:
            archivo.guardar_productos([p.to_dict() for p in restaurante.listar_productos()])
        print("Actualización exitosa." if ok else "No se pudo actualizar.")
    except ValueError as e:
        print(f"Error: {e}")


def eliminar_producto() -> None:
    codigo = input("Código a eliminar: ").strip()
    ok = restaurante.eliminar_producto(codigo)
    if ok:
        archivo.guardar_productos([p.to_dict() for p in restaurante.listar_productos()])
    print("Producto eliminado." if ok else "Producto no encontrado.")


def listar_productos() -> None:
    prods = restaurante.listar_productos()
    if not prods:
        print("No hay productos registrados.")
        return
    for p in prods:
        print(p)


def registrar_usuario() -> None:
    try:
        identificacion = input("Identificación: ").strip()
        nombre = input("Nombre: ").strip()
        correo = input("Correo: ").strip()
        user = Usuario(identificacion=identificacion, nombre=nombre, correo=correo)
        restaurante.registrar_usuario(user)
        archivo.guardar_usuarios([u.to_dict() for u in restaurante.listar_usuarios()])
        print("Usuario registrado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")


def listar_usuarios() -> None:
    users = restaurante.listar_usuarios()
    if not users:
        print("No hay usuarios registrados.")
        return
    for u in users:
        print(u)


def vender_producto() -> None:
    identificacion = input("Identificación del usuario: ").strip()
    codigo = input("Código del producto: ").strip()
    cantidad_input = input("Cantidad a vender: ").strip()
    try:
        cantidad = int(cantidad_input)
    except ValueError:
        print("Cantidad inválida.")
        return
    ok = restaurante.vender_producto(codigo, identificacion, cantidad)
    if ok:
        archivo.guardar_ventas([v.to_dict() for v in restaurante.listar_ventas()])
        archivo.guardar_productos([p.to_dict() for p in restaurante.listar_productos()])
        print("Venta registrada correctamente.")
    else:
        print("No se pudo registrar la venta. Verifique usuario, producto o stock.")


def listar_ventas_por_usuario() -> None:
    identificacion = input("Identificación del usuario: ").strip()
    ventas = restaurante.listar_ventas_por_usuario(identificacion)
    if not ventas:
        print("No hay ventas para este usuario.")
        return
    for v in ventas:
        producto = restaurante.buscar_producto(v.producto_codigo)
        nombre_prod = producto.nombre if producto else "(producto no disponible)"
        print(f"{v.cantidad} x {v.producto_codigo} - {nombre_prod} (fecha: {v.fecha})")


MENU_FUNCIONES = {
    "1": registrar_producto,
    "2": buscar_producto,
    "3": actualizar_producto,
    "4": eliminar_producto,
    "5": listar_productos,
    "6": registrar_usuario,
    "7": listar_usuarios,
    "8": vender_producto,
    "9": listar_ventas_por_usuario,
}


def main() -> None:
    while True:
        print("\n========================================")
        print("        SISTEMA DE RESTAURANTE")
        print("========================================")
        for opt in MENU_OPTIONS:
            print(opt)
        elec = input("Seleccione una opción: ").strip()
        if elec == "10":
            print("Saliendo...")
            break
        funcion = MENU_FUNCIONES.get(elec)
        if funcion:
            try:
                funcion()
            except Exception as e:
                print(f"Ocurrió un error: {e}")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
