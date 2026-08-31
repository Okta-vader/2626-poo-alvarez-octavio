import os
import sys
import json
import tempfile
import unittest

BASE = os.path.dirname(os.path.dirname(__file__))
if BASE not in sys.path:
    sys.path.insert(0, BASE)

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class SalesTests(unittest.TestCase):
    def test_sell_and_persistence(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base = tmpdir
            archivo = ArchivoServicio(base)

            # crear usuario y producto
            u = Usuario(identificacion="U1", nombre="Test", correo="t@e.com")
            p = Producto(codigo="P1", nombre="Prod", categoria="Cat", precio=2.5, stock=5)

            # guardar usuarios y productos
            archivo.guardar_usuarios([u.to_dict()])
            archivo.guardar_productos([p.to_dict()])

            # cargar y reconstruir
            r_products = [Producto.from_dict(d) for d in archivo.cargar_productos()]
            r_users = [Usuario.from_dict(d) for d in archivo.cargar_usuarios()]
            restaurante = Restaurante(productos=r_products, usuarios=r_users)

            # vender 2 unidades
            ok = restaurante.vender_producto("P1", "U1", 2)
            self.assertTrue(ok)
            # guardar ventas and productos
            archivo.guardar_ventas([v.to_dict() for v in restaurante.listar_ventas()])
            archivo.guardar_productos([p.to_dict() for p in restaurante.listar_productos()])

            # reload products and sales
            loaded_products = [Producto.from_dict(d) for d in archivo.cargar_productos()]
            self.assertEqual(loaded_products[0].stock, 3)
            loaded_sales = archivo.cargar_ventas()
            self.assertEqual(len(loaded_sales), 1)

    def test_sell_insufficient_stock(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base = tmpdir
            archivo = ArchivoServicio(base)
            u = Usuario(identificacion="U2", nombre="Test2", correo="t2@e.com")
            p = Producto(codigo="P2", nombre="Prod2", categoria="Cat2", precio=1.0, stock=1)
            archivo.guardar_usuarios([u.to_dict()])
            archivo.guardar_productos([p.to_dict()])
            r_products = [Producto.from_dict(d) for d in archivo.cargar_productos()]
            r_users = [Usuario.from_dict(d) for d in archivo.cargar_usuarios()]
            restaurante = Restaurante(productos=r_products, usuarios=r_users)
            ok = restaurante.vender_producto("P2", "U2", 5)
            self.assertFalse(ok)

if __name__ == "__main__":
    unittest.main()
