class Persona:
    def __init__(self):
        self.DNI= None
        self.nombre= ""
        self.apellido=""
        self.nacimiento = []

    def __str__(self):
        return (f"Persona: {self.nombre} {self.apellido}\n"
                f"DNI: {self.DNI}\n"
                f"Nacimiento: {self.nacimiento[0]}-{self.nacimiento[1]}-{self.nacimiento[2]}\n")

persona1 = Persona()
persona1.DNI=546467
persona1.nombre="Carlos"
persona1.apellido="Fernandez"
persona1.nacimiento=(2000,1,1)

print(persona1)