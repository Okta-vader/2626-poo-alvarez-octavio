from __future__ import annotations

from typing import List

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    def __init__(self, base_dir: str) -> None:
        self.archivo_servicio = ArchivoServicio(base_dir)
        self.productos: List[Producto] = self._cargar_productos()
        self.usuarios: List[Usuario] = self._cargar_usuarios()

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

    def listar_productos(self) -> List[Producto]:
        return list(self.productos)

    def listar_usuarios(self) -> List[Usuario]:
        return list(self.usuarios)

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
