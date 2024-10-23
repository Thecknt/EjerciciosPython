print("---------Regresar tupla de valores------------")

def regresar_varios_valores(nombre,apellido,edad):
    return nombre.upper(),apellido.upper(),edad

nombre = 'Juan'
apellido = 'Fernandez'
edad = 30

print(regresar_varios_valores(nombre, apellido, edad))