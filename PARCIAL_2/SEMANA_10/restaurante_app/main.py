from __future__ import annotations
import os
import json
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto
from modelos.usuario import Usuario

MENU_OPTIONS = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías",
    "9. Salir",
)

DATA_PATH = os.path.join(os.path.dirname(__file__), "datos", "productos.json")

archivo = ArchivoServicio(DATA_PATH)

# Cargar registros desde JSON y reconstruir objetos Producto
raw_records = []
try:
    raw_records = archivo.cargar()
except json.JSONDecodeError:
    print("Advertencia: productos.json contiene JSON inválido. Iniciando con lista vacía.")
except PermissionError:
    print("Error: sin permiso para leer productos.json. Iniciando con lista vacía.")

productos_iniciales = []
for rec in raw_records:
    try:
        prod = Producto.from_dict(rec)
        productos_iniciales.append(prod)
    except (KeyError, ValueError) as e:
        print(f"Registro inválido omitido: {e}")

restaurante = Restaurante(productos=productos_iniciales)

# helper para guardar
def guardar_productos() -> None:
    try:
        lista = [p.to_dict() for p in restaurante.listar_productos()]
        archivo.guardar(lista)
    except PermissionError:
        print("Error: no se pudieron guardar los productos (permiso denegado).")
    except Exception as e:
        print(f"Error al guardar productos: {e}")


def registrar_producto() -> None:
    try:
        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()
        precio_str = input("Precio: ").strip()
        precio = float(precio_str)
        prod = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
        restaurante.registrar_producto(prod)
        guardar_productos()
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
    try:
        ok = restaurante.actualizar_producto(codigo, nombre=nombre, categoria=categoria, precio=precio)
        if ok:
            guardar_productos()
        print("Actualización exitosa." if ok else "No se pudo actualizar.")
    except ValueError as e:
        print(f"Error: {e}")


def eliminar_producto() -> None:
    codigo = input("Código a eliminar: ").strip()
    ok = restaurante.eliminar_producto(codigo)
    if ok:
        guardar_productos()
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


def mostrar_categorias() -> None:
    categorias = restaurante.categorias_unicas()
    if not categorias:
        print("No hay categorías para mostrar.")
        return
    for c in sorted(categorias):
        print(c)

MENU_FUNCIONES = {
    "1": registrar_producto,
    "2": buscar_producto,
    "3": actualizar_producto,
    "4": eliminar_producto,
    "5": listar_productos,
    "6": registrar_usuario,
    "7": listar_usuarios,
    "8": mostrar_categorias,
}


def main() -> None:
    while True:
        print("\n========================================")
        print("        SISTEMA DE RESTAURANTE")
        print("========================================")
        for opt in MENU_OPTIONS:
            print(opt)
        elec = input("Seleccione una opción: ").strip()
        if elec == "9":
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
