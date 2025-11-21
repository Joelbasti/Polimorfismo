from figurageometrica import FiguraGeometrica
class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)
    def area(self):
        return self._alto * self._ancho
    def perimetro(self):
        return 2 * (self._ancho + self._alto)
    def __str__(self):
        return f'Rectangulo: {self.__dict__.__str__()}'
    