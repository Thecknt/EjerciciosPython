class Rectangulo:
    def __init__(self):
        self.altura=0
        self.base=0

    def calcular_area(self):
        area = self.base * self.altura
        print(f'El resultado del area es {area}')
        return area

    def calcular_perimetro(self):
        perimetro = (self.base * 2) + (self.altura *2)
        print(f'El resultado del perimetro es {perimetro}')
        return perimetro

calculo = Rectangulo()

calculo.base = 20
calculo.altura = 30
calculo.calcular_area()
calculo.calcular_perimetro()

