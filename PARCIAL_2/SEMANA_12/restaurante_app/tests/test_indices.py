import os
import sys
import tempfile
import unittest

BASE = os.path.dirname(os.path.dirname(__file__))
if BASE not in sys.path:
    sys.path.insert(0, BASE)

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.usuario import Usuario

class IndicesTests(unittest.TestCase):
    def test_indices_sync_and_sell(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            archivo = ArchivoServicio(tmpdir)
            # crear y guardar usuario y producto
            u = Usuario(identificacion='U100', nombre='User', correo='u@example.com')
            p = Producto(codigo='C100', nombre='Prod', categoria='Cat', precio=5.0, stock=10)
            archivo.guardar_usuarios([u.to_dict()])
            archivo.guardar_productos([p.to_dict()])

            # cargar desde archivo y crear servicio
            productos = [Producto.from_dict(d) for d in archivo.cargar_productos()]
            usuarios = [Usuario.from_dict(d) for d in archivo.cargar_usuarios()]
            r = Restaurante(productos=productos, usuarios=usuarios)

            # índices deben estar reconstruidos
            self.assertTrue(r.existe_producto_codigo('C100'))
            self.assertTrue(r.existe_usuario('U100'))

            # realizar venta
            ok = r.vender_producto('C100', 'U100', 3)
            self.assertTrue(ok)
            self.assertEqual(r.contar_ventas_usuario('U100'), 1)
            # stock actualizado
            prod = r.buscar_producto('C100')
            self.assertEqual(prod.stock, 7)

    def test_index_updates_on_register_and_delete(self):
        r = Restaurante()
        p = Producto(codigo='X1', nombre='P', categoria='g', precio=1.0, stock=2)
        r.registrar_producto(p)
        self.assertTrue(r.existe_producto_codigo('X1'))
        r.eliminar_producto('X1')
        self.assertFalse(r.existe_producto_codigo('X1'))

if __name__ == '__main__':
    unittest.main()
