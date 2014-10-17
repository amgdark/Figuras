class Figura:

    def __init__(self, figura):
        self.figura = figura

    def cuadrado(self, lado):
        return lado * lado

    def circulo(self, radio):
        return round(float(3.1416 * radio ** 2), 2)

    def triangulo(self, base, altura):
        return round(float(base * altura / 2), 2)

    def trapecio(self, base_mayor, base_menor, altura):
        return round(float((base_mayor + base_menor) / 2 * altura), 2)
