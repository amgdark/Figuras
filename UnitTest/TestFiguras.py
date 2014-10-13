# -*- coding: utf-8 -*-
import unittest
from app.Figura import Figura

class TestEdad(unittest.TestCase):
	
	def test_figura_es_un_cuadrado_y_el_lado_es_6(self):
		fig = Figura("Cuadrado", 6)
		self.assertEqual(fig.getArea() == 6, 'área  cálculada {0} área esperada {1}'.format(fig.getArea(), 6))

if __name__ == '__main__':
	unittest.main()		
