from typing import Optional, List, Set
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class Restaurante:
    def __init__(self, productos: Optional[List[Producto]] = None, usuarios: Optional[List[Usuario]] = None, ventas: Optional[List[Venta]] = None) -> None:
        self.productos: List[Producto] = list(productos) if productos else []
        self.usuarios: List[Usuario] = list(usuarios) if usuarios else []
        self._ventas: List[Venta] = list(ventas) if ventas else []

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

    def actualizar_producto(self, codigo: str, nombre: Optional[str] = None, categoria: Optional[str] = None, precio: Optional[float] = None, stock: Optional[int] = None) -> bool:
        prod = self.buscar_producto(codigo)
        if prod is None:
            return False
        prod.actualizar(nombre=nombre, categoria=categoria, precio=precio, stock=stock)
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        prod = self.buscar_producto(codigo)
        if prod is None:
            return False
        self.productos.remove(prod)
        return True

    def listar_productos(self) -> List[Producto]:
        return list(self.productos)

    # Usuarios
    def registrar_usuario(self, usuario: Usuario) -> None:
        if any(u.identificacion == usuario.identificacion for u in self.usuarios):
            raise ValueError(f"Identificación de usuario duplicada: {usuario.identificacion}")
        self.usuarios.append(usuario)

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        for u in self.usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    def listar_usuarios(self) -> List[Usuario]:
        return list(self.usuarios)

    # Ventas
    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)
        if usuario is None or producto is None:
            return False
        try:
            if cantidad <= 0:
                return False
            if producto.stock < cantidad:
                return False
            # crear venta
            venta = Venta(usuario.identificacion, producto.codigo, cantidad)
            self._ventas.append(venta)
            producto.vender(cantidad)
            return True
        except ValueError:
            return False

    def listar_ventas_por_usuario(self, identificacion_usuario: str) -> List[Venta]:
        return [v for v in self._ventas if v.usuario_id == identificacion_usuario]

    def listar_ventas(self) -> List[Venta]:
        return list(self._ventas)

    # Estructuras auxiliares
    def categorias_unicas(self) -> Set[str]:
        return set(p.categoria for p in self.productos)
