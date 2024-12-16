class persona:
    def __init__(self):
        self.nombre = ""
        self.apellido=""
        self.email = ""
        self.edad = 0

    def __str__(self):
        return(f'El nombre de la persona es: {self.nombre} \n'
        f'El apellido es: {self.apellido} \n'
        f'Su email es: {self.email} \n'
        f'Su edad es: {self.edad}')

    def es_mayor(self):
        if self.edad >= 18:
            return True
        else:
            return False

if __name__ == "__main__":
    persona1 = persona()

    persona1.nombre = 'Carlos'
    persona1.apellido = 'Perez'
    persona1.edad=22
    persona1.email= 'CarlosPerez@email.com'
    esMayor=persona1.es_mayor()
    print(f'{persona1}\n{persona1.nombre} es mayor? {esMayor}')