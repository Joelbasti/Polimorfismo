class FiguraGeometrica:
    #Esta clase representa un objeto figura geometrica
    def __init__(self, ancho: float, alto: float):
        self._alto = None
        self._ancho = None
        self.alto = alto
        self.ancho = ancho
    #Métodos getter/setter & str
    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, nuevo_alto: float):
        if nuevo_alto < 0:
            raise ValueError("ERROR el alto debe ser mayor a 0")
        self._alto = nuevo_alto
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, nuevo_ancho: float):
        if nuevo_ancho < 0:
            raise ValueError("ERROR el ancho debe ser mayor a 0")
        self._ancho = nuevo_ancho
    def __str__(self):
        return f'FiguraGeometrica: {self.__dict__.__str__()}'

    #Metodo que calcula y devuleve el calor del area
    def area(self):
        return self._alto * self._ancho
    def perimetro(self):
        pass
