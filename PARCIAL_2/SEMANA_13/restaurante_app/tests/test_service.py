import os
import sys
import unittest

BASE = os.path.dirname(os.path.dirname(__file__))
if BASE not in sys.path:
    sys.path.insert(0, BASE)

from servicios.restaurante_servicio import RestauranteServicio

class RestauranteServicioTest(unittest.TestCase):
    def test_validar_acceso(self):
        servicio = RestauranteServicio(os.path.join(BASE, "datos"))
        self.assertTrue(servicio.validar_acceso("admin", "1234"))
        self.assertFalse(servicio.validar_acceso("admin", "incorrecta"))

    def test_listar_productos_y_usuarios(self):
        servicio = RestauranteServicio(os.path.join(BASE, "datos"))
        self.assertGreater(len(servicio.listar_productos()), 0)
        self.assertGreater(len(servicio.listar_usuarios()), 0)

if __name__ == "__main__":
    unittest.main()
