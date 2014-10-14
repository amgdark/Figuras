# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../')
from app.Figura import Figura


class TestEdad(unittest.TestCase):

    def test_figura_es_un_cuadrado_con_lado_6(self):
        fig = Figura(["Cuadrado", 6, 0, 0])
        self.assertEqual(
            fig.getArea(), 36, 'área  cálculada {0} área esperada {1}'.format(fig.getArea(), 36))

    def test_figura_es_un_triangulo_de_base_8_y_altura_10(self):
        fig = Figura(["Triangulo", 8, 10, 0])
        self.assertEqual(
            fig.getArea(), 40, 'área  cálculada {0} área esperada {1}'.format(fig.getArea(), 40))

    def test_figura_es_un_ciculo_de_radio_es_6(self):
        fig = Figura(["Circulo", 6, 0, 0])
        self.assertEqual(fig.getArea(
        ), 113.10, 'área  cálculada {0} área esperada {1}'.format(fig.getArea(), 113.10))

    def test_figura_es_un_trapecio_base_mayor_6_base_menor_4_altura_6(self):
        fig = Figura(["Trapecio", 6, 4, 6])
        self.assertEqual(fig.getArea(
        ), 30.0, 'área  cálculada {0} área esperada {1}'.format(fig.getArea(), 30.0))
if __name__ == '__main__':
    unittest.main()
