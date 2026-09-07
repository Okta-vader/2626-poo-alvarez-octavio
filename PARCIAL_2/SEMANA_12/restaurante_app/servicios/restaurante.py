from typing import Optional, List, Set, Dict
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class Restaurante:
    def __init__(self, productos: Optional[List[Producto]] = None, usuarios: Optional[List[Usuario]] = None, ventas: Optional[List[Venta]] = None) -> None:
        # listas principales
        self.productos: List[Producto] = list(productos) if productos else []
        self.usuarios: List[Usuario] = list(usuarios) if usuarios else []
        self._ventas: List[Venta] = list(ventas) if ventas else []

        # índices auxiliares para acelerar búsquedas
        self.productos_por_codigo: Dict[str, Producto] = {}
        self.usuarios_por_id: Dict[str, Usuario] = {}
        self.ventas_por_usuario: Dict[str, List[Venta]] = {}

        # construir índices iniciales
        self._rebuild_indices()

    # Índices
    def _rebuild_indices(self) -> None:
        self.productos_por_codigo = {p.codigo: p for p in self.productos}
        self.usuarios_por_id = {u.identificacion: u for u in self.usuarios}
        self.ventas_por_usuario = {}
        for v in self._ventas:
            self.ventas_por_usuario.setdefault(v.usuario_id, []).append(v)

    # Productos
    def registrar_producto(self, producto: Producto) -> None:
        if producto.codigo in self.productos_por_codigo:
            raise ValueError(f"Código de producto duplicado: {producto.codigo}")
        self.productos.append(producto)
        self.productos_por_codigo[producto.codigo] = producto

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        return self.productos_por_codigo.get(codigo)

    def actualizar_producto(self, codigo: str, nombre: Optional[str] = None, categoria: Optional[str] = None, precio: Optional[float] = None, stock: Optional[int] = None) -> bool:
        prod = self.buscar_producto(codigo)
        if prod is None:
            return False
        prod.actualizar(nombre=nombre, categoria=categoria, precio=precio, stock=stock)
        # índice ya referencia el objeto; no es necesario actualizar la clave si no cambia
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        prod = self.buscar_producto(codigo)
        if prod is None:
            return False
        self.productos.remove(prod)
        self.productos_por_codigo.pop(codigo, None)
        return True

    def listar_productos(self) -> List[Producto]:
        return list(self.productos)

    # Usuarios
    def registrar_usuario(self, usuario: Usuario) -> None:
        if usuario.identificacion in self.usuarios_por_id:
            raise ValueError(f"Identificación de usuario duplicada: {usuario.identificacion}")
        self.usuarios.append(usuario)
        self.usuarios_por_id[usuario.identificacion] = usuario

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        return self.usuarios_por_id.get(identificacion)

    def listar_usuarios(self) -> List[Usuario]:
        return list(self.usuarios)

    def eliminar_usuario(self, identificacion: str) -> bool:
        user = self.buscar_usuario(identificacion)
        if user is None:
            return False
        self.usuarios.remove(user)
        self.usuarios_por_id.pop(identificacion, None)
        # también limpiar ventas asociadas? se mantiene el historial en _ventas
        return True

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
            venta = Venta(usuario.identificacion, producto.codigo, cantidad)
            self._ventas.append(venta)
            self.ventas_por_usuario.setdefault(usuario.identificacion, []).append(venta)
            producto.vender(cantidad)
            return True
        except ValueError:
            return False

    def listar_ventas_por_usuario(self, identificacion_usuario: str) -> List[Venta]:
        # uso índice para evitar recorrer toda la colección en cada consulta
        return list(self.ventas_por_usuario.get(identificacion_usuario, []))

    def listar_ventas(self) -> List[Venta]:
        return list(self._ventas)

    # Métodos auxiliares útiles para pruebas / verificación
    def existe_producto_codigo(self, codigo: str) -> bool:
        return codigo in self.productos_por_codigo

    def existe_usuario(self, identificacion: str) -> bool:
        return identificacion in self.usuarios_por_id

    def contar_ventas_usuario(self, identificacion: str) -> int:
        return len(self.ventas_por_usuario.get(identificacion, []))

    # Estructuras auxiliares
    def categorias_unicas(self) -> Set[str]:
        return set(p.categoria for p in self.productos)
