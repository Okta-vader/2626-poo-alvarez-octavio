from __future__ import annotations

from typing import List

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    def __init__(self, base_dir: str) -> None:
        self.archivo_servicio = ArchivoServicio(base_dir)
        self.productos: List[Producto] = self._cargar_productos()
        self.usuarios: List[Usuario] = self._cargar_usuarios()
        self.ventas: List[Venta] = self._cargar_ventas()

    def _cargar_productos(self) -> List[Producto]:
        data = self.archivo_servicio.cargar_productos()
        productos: List[Producto] = []
        for item in data:
            try:
                productos.append(Producto.from_dict(item))
            except (KeyError, ValueError) as exc:
                print(f"Producto inválido omitido: {exc}")
        return productos

    def _cargar_usuarios(self) -> List[Usuario]:
        data = self.archivo_servicio.cargar_usuarios()
        usuarios: List[Usuario] = []
        for item in data:
            try:
                usuarios.append(Usuario.from_dict(item))
            except (KeyError, ValueError) as exc:
                print(f"Usuario inválido omitido: {exc}")
        return usuarios

    def _cargar_ventas(self) -> List[Venta]:
        data = self.archivo_servicio.cargar_ventas()
        ventas: List[Venta] = []
        for item in data:
            try:
                ventas.append(Venta.from_dict(item))
            except (KeyError, ValueError) as exc:
                print(f"Venta inválida omitida: {exc}")
        return ventas

    def listar_productos(self) -> List[Producto]:
        return list(self.productos)

    def listar_usuarios(self) -> List[Usuario]:
        return list(self.usuarios)

    def listar_ventas(self) -> List[Venta]:
        return list(self.ventas)

    def validar_acceso(self, identificacion: str, password: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False
        return usuario.password == password

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def buscar_producto(self, codigo: str) -> Producto | None:
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> Producto:
        if self.buscar_producto(codigo):
            raise ValueError(f"El producto con código '{codigo}' ya existe.")

        producto = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio, stock=stock)
        self.productos.append(producto)
        self.archivo_servicio.guardar_productos([item.to_dict() for item in self.productos])
        return producto

    def actualizar_producto(self, codigo: str, nombre: str | None = None, categoria: str | None = None, precio: float | None = None, stock: int | None = None) -> Producto:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError(f"No existe un producto con código '{codigo}'.")

        if nombre is not None:
            producto.nombre = nombre.strip()
        if categoria is not None:
            producto.categoria = categoria.strip()
        if precio is not None:
            producto.precio = float(precio)
        if stock is not None:
            producto.stock = int(stock)

        self.archivo_servicio.guardar_productos([item.to_dict() for item in self.productos])
        return producto

    def eliminar_producto(self, codigo: str) -> Producto:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError(f"No existe un producto con código '{codigo}'.")

        self.productos.remove(producto)
        self.archivo_servicio.guardar_productos([item.to_dict() for item in self.productos])
        return producto

    def registrar_venta(self, usuario_id: str, producto_codigo: str, cantidad: int) -> Venta:
        usuario = self.buscar_usuario(usuario_id)
        if usuario is None:
            raise ValueError(f"Usuario '{usuario_id}' no encontrado.")
        producto = self.buscar_producto(producto_codigo)
        if producto is None:
            raise ValueError(f"Producto '{producto_codigo}' no encontrado.")
        try:
            cantidad_val = int(cantidad)
        except (TypeError, ValueError):
            raise ValueError("Cantidad inválida para la venta.")
        if cantidad_val <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if producto.stock < cantidad_val:
            raise ValueError("Stock insuficiente para realizar la venta.")

        # Reducir stock y crear venta
        producto.stock -= cantidad_val
        venta = Venta(usuario_id=usuario_id, producto_codigo=producto_codigo, cantidad=cantidad_val)
        self.ventas.append(venta)

        # Persistir cambios
        self.archivo_servicio.guardar_productos([p.to_dict() for p in self.productos])
        self.archivo_servicio.guardar_ventas([v.to_dict() for v in self.ventas])

        return venta
