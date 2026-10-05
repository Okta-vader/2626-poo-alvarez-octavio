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
        productos: List[Producto] = []
        for item in self.archivo_servicio.cargar_productos():
            try:
                productos.append(Producto.from_dict(item))
            except (KeyError, ValueError) as exc:
                print(f"Producto inválido omitido: {exc}")
        return productos

    def _cargar_usuarios(self) -> List[Usuario]:
        usuarios: List[Usuario] = []
        for item in self.archivo_servicio.cargar_usuarios():
            try:
                usuarios.append(Usuario.from_dict(item))
            except (KeyError, ValueError) as exc:
                print(f"Usuario inválido omitido: {exc}")
        return usuarios

    def _cargar_ventas(self) -> List[Venta]:
        ventas: List[Venta] = []
        for item in self.archivo_servicio.cargar_ventas():
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
        return usuario is not None and usuario.password == password

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def es_administrador(self, identificacion: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        return usuario is not None and usuario.rol == "Administrador"

    def _exigir_administrador(self, identificacion: str) -> None:
        if not self.es_administrador(identificacion):
            raise PermissionError("Solo un usuario Administrador puede gestionar usuarios.")

    def registrar_usuario(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        password: str,
        rol: str,
        actor_id: str,
    ) -> Usuario:
        self._exigir_administrador(actor_id)
        if rol not in Usuario.ROLES_GESTIONABLES:
            raise ValueError("Solo se pueden registrar usuarios Empleado o Cliente.")
        if self.buscar_usuario(identificacion):
            raise ValueError(f"Ya existe el usuario '{identificacion}'.")

        usuario = Usuario(identificacion, nombre, correo, password, rol)
        nuevos_usuarios = [*self.usuarios, usuario]
        self.archivo_servicio.guardar_usuarios([item.to_dict() for item in nuevos_usuarios])
        self.usuarios = nuevos_usuarios
        return usuario

    def actualizar_usuario(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        password: str,
        rol: str,
        actor_id: str,
    ) -> Usuario:
        self._exigir_administrador(actor_id)
        usuario_actual = self.buscar_usuario(identificacion)
        if usuario_actual is None:
            raise ValueError(f"No existe el usuario '{identificacion}'.")
        es_cuenta_administradora_actual = identificacion == actor_id and usuario_actual.rol == "Administrador"
        if rol not in Usuario.ROLES_GESTIONABLES and not (
            es_cuenta_administradora_actual and rol == "Administrador"
        ):
            raise ValueError("Solo puede asignar los roles Empleado o Cliente.")
        if usuario_actual.rol == "Administrador" and identificacion != actor_id:
            raise ValueError("La gestión de usuarios solo permite modificar Empleados y Clientes.")
        if identificacion == actor_id and rol != "Administrador":
            raise ValueError("No puede cambiar el rol de su propia cuenta administrativa.")

        usuario_actualizado = Usuario(
            identificacion,
            nombre,
            correo,
            password or usuario_actual.password,
            rol,
        )
        nuevos_usuarios = [
            usuario_actualizado if usuario.identificacion == identificacion else usuario
            for usuario in self.usuarios
        ]
        self.archivo_servicio.guardar_usuarios([item.to_dict() for item in nuevos_usuarios])
        self.usuarios = nuevos_usuarios
        return usuario_actualizado

    def eliminar_usuario(self, identificacion: str, actor_id: str) -> Usuario:
        self._exigir_administrador(actor_id)
        if identificacion == actor_id:
            raise ValueError("No puede eliminar la cuenta administrativa con la que inició sesión.")
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            raise ValueError(f"No existe el usuario '{identificacion}'.")
        if usuario.rol == "Administrador":
            raise ValueError("La gestión de usuarios solo permite eliminar Empleados y Clientes.")

        nuevos_usuarios = [item for item in self.usuarios if item.identificacion != identificacion]
        self.archivo_servicio.guardar_usuarios([item.to_dict() for item in nuevos_usuarios])
        self.usuarios = nuevos_usuarios
        return usuario

    def buscar_producto(self, codigo: str) -> Producto | None:
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> Producto:
        if self.buscar_producto(codigo):
            raise ValueError(f"El producto con código '{codigo}' ya existe.")
        producto = Producto(codigo, nombre, categoria, precio, stock)
        self.productos.append(producto)
        self.archivo_servicio.guardar_productos([item.to_dict() for item in self.productos])
        return producto

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str | None = None,
        categoria: str | None = None,
        precio: float | None = None,
        stock: int | None = None,
    ) -> Producto:
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
        if self.buscar_usuario(usuario_id) is None:
            raise ValueError(f"Usuario '{usuario_id}' no encontrado.")
        producto = self.buscar_producto(producto_codigo)
        if producto is None:
            raise ValueError(f"Producto '{producto_codigo}' no encontrado.")
        try:
            cantidad_val = int(cantidad)
        except (TypeError, ValueError) as exc:
            raise ValueError("Cantidad inválida para la venta.") from exc
        if cantidad_val <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if producto.stock < cantidad_val:
            raise ValueError("Stock insuficiente para realizar la venta.")

        producto.stock -= cantidad_val
        venta = Venta(usuario_id, producto_codigo, cantidad_val)
        ventas_actualizadas = [*self.ventas, venta]
        self.archivo_servicio.guardar_productos([item.to_dict() for item in self.productos])
        self.archivo_servicio.guardar_ventas([item.to_dict() for item in ventas_actualizadas])
        self.ventas = ventas_actualizadas
        return venta
