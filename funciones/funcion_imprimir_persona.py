
def imprimir_persona(nombre, apellido, edad):
    print(f'''Persona:
    nombre: {nombre}
    apellido: {apellido}
    edad: {edad}
''')

persona = ['Cristian','barreto',38]

nombre,apellido,edad = persona

imprimir_persona(nombre,apellido, edad)
if __name__ == '__main__':
    print('-----------Funcion imprimir persona por parametros------------')