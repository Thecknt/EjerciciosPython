class Vehiculo:
    def __init__(self):
        self.marca=""
        self.modelo=""
        self.año= None
        self.color=""

    def acelerar(self):
        return " esta acelerando"

    def __str__(self):
        return(f"La marca del vehiculo es {self.marca}\n"
               f"El modelo del vehiculo es {self.modelo} - {self.año}\n"
               f"El color del auto es {self.color}")

auto = Vehiculo()
auto.marca="Renault"
auto.modelo= "Stepway"
auto.año=2010
auto.color="Azul Grafito"

print(auto)
print(f"La Reni{auto.acelerar()}")
