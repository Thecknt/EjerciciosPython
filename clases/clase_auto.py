# Crea una clase Coche que tenga atributos como marca, modelo
# y velocidad máxima. Implementa un metodo para mostrar información del coche.

class Automovil:
    def __init__(self,marca, modelo,velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad Máxima: {self.velocidad_maxima} km/h")

coche = Automovil("Toyota", "Corolla", 180)

coche.mostrar_informacion()