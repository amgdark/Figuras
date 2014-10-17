# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('..')
from app.Figura2 import Figura


class TestEdad(unittest.TestCase):

    def test_figura_es_un_cuadrado_con_lado_6(self):
        fig = Figura("Cuadrado")
        result = fig.cuadrado(6)
        self.assertEqual(result, 36, 'área  cálculada {0} área esperada {1}'.format(result, 36))

    def test_figura_es_un_triangulo_de_base_8_y_altura_10(self):
        fig = Figura("Triangulo")
        result = fig.triangulo(8, 10)
        self.assertEqual(result, 40, 'área  cálculada {0} área esperada {1}'.format(result, 40))

    def test_figura_es_un_ciculo_de_radio_es_6(self):
        fig = Figura("Circulo")
        result = fig.circulo(6)
        self.assertEqual(result, 113.10, 'área  cálculada {0} área esperada {1}'.format(result, 113.10))

    def test_figura_es_un_trapecio_base_mayor_6_base_menor_4_altura_6(self):
        fig = Figura("Trapecio")
        result = fig.trapecio(6, 4, 6)
        self.assertEqual(result, 30.0, 'área  cálculada {0} área esperada {1}'.format(result, 30.0))
if __name__ == '__main__':
    unittest.main()
