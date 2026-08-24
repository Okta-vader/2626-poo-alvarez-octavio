import os
import sys
import json
import tempfile
import unittest

# Asegurar que el paquete restaurante_app esté importable
BASE = os.path.dirname(os.path.dirname(__file__))  # carpeta restaurante_app
if BASE not in sys.path:
    sys.path.insert(0, BASE)

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante
from modelos.producto import Producto

class PersistenceTests(unittest.TestCase):
    def test_persistence_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "productos.json")
            archivo = ArchivoServicio(path)

            # iniciar con archivo vacío
            self.assertEqual(archivo.cargar(), [])

            # crear restaurante y registrar producto
            r = Restaurante()
            p = Producto(codigo="P01", nombre="Café", categoria="Bebida", precio=1.5)
            r.registrar_producto(p)

            # guardar usando archivo
            archivo.guardar([x.to_dict() for x in r.listar_productos()])

            # cargar nuevamente y reconstruir objetos
            loaded = archivo.cargar()
            self.assertIsInstance(loaded, list)
            self.assertEqual(len(loaded), 1)
            p2 = Producto.from_dict(loaded[0])
            self.assertEqual(p2.codigo, p.codigo)
            self.assertEqual(p2.nombre, p.nombre)
            self.assertEqual(p2.categoria, p.categoria)
            self.assertAlmostEqual(p2.precio, p.precio)

    def test_invalid_json_raises(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "productos.json")
            # escribir contenido inválido
            with open(path, "w", encoding="utf-8") as f:
                f.write("{ not valid json }")
            archivo = ArchivoServicio(path)
            with self.assertRaises(json.JSONDecodeError):
                archivo.cargar()

if __name__ == "__main__":
    unittest.main()
