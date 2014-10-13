class Figura:
	def __init__(self, args):
		self.figura=args[0]
		self.parametros=args[1:]

	def getArea(self):
		figuras={"Cuadrado" : self.cuadrado(), 
				"Triangulo" : self.triangulo(), 
				"Circulo" : self.circulo(),
				"Trapecio" : self.trapecio()}

		return figuras[self.figura]			

	def cuadrado(self):
		return self.parametros[0]*self.parametros[0]

	def circulo(self):
		return round(3.1416 * float(self.parametros[0]) ** 2, 2)

	def triangulo(self):
		return round(float(self.parametros[0])*float(self.parametros[1])/2, 2)

	def trapecio(self):
		return round(((float(self.parametros[0])+float(self.parametros[1]))/2*self.parametros[2]), 2)
