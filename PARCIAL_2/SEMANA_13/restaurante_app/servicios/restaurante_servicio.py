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
