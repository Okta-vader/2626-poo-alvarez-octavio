from typing import Optional, List, Set
from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    def __init__(self, productos: Optional[List[Producto]] = None) -> None:
        self.productos: List[Producto] = list(productos) if productos else []  # lista dinámica de productos
        self.usuarios: List[Usuario] = []    # lista dinámica de usuarios

    # Productos
    def registrar_producto(self, producto: Producto) -> None:
        if any(p.codigo == producto.codigo for p in self.productos):
            raise ValueError(f"Código de producto duplicado: {producto.codigo}")
        self.productos.append(producto)

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nombre: Optional[str] = None, categoria: Optional[str] = None, precio: Optional[float] = None) -> bool:
        prod = self.buscar_producto(codigo)
        if prod is None:
            return False
        prod.actualizar(nombre=nombre, categoria=categoria, precio=precio)
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        prod = self.buscar_producto(codigo)
        if prod is None:
            return False
        self.productos.remove(prod)
        return True

    def listar_productos(self) -> List[Producto]:
        return list(self.productos)  # devolver copia para no exponer la lista interna

    # Usuarios
    def registrar_usuario(self, usuario: Usuario) -> None:
        if any(u.identificacion == usuario.identificacion for u in self.usuarios):
            raise ValueError(f"Identificación de usuario duplicada: {usuario.identificacion}")
        self.usuarios.append(usuario)

    def listar_usuarios(self) -> List[Usuario]:
        return list(self.usuarios)

    # Estructuras auxiliares
    def categorias_unicas(self) -> Set[str]:
        # set para obtener categorías únicas sin duplicados
        return set(p.categoria for p in self.productos)
