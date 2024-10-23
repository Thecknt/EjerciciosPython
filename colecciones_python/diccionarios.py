print('***    Diccionarios   ***')

#Creamos un diccionario de persona con clave:valor
print('')
persona = {
    'nombre' : 'Cristian',
    'edad' : 40,
    'Ciudad' : 'Buenos Aires'
}

print(persona)

#Acceder los datos de persona:
print('')
print(f'Nombre: {persona['nombre']}\n'
      f'Edad: {persona.get('edad')}\n'
      f'Ciudad: {persona.get('Ciudad')}')

#Modificar un valor de la clave:

persona['edad'] = 39
print(f'Diccionario de persona: {persona}')
print('')
#Agregar una nueva clave:valor

persona['profesion'] = 'Developer'
print(f'{persona}')
print('')
#Eliminar un elemento del diccionario
del persona['Ciudad']
print(f'{persona}')
print('')
persona.pop('profesion')
print(f'{persona}')

#iterar sobre el diccionario:
print('')
for llave, valor in persona.items():
    print(f'{llave} : {valor}')

print('')
#Obtener solo los valores del diccionario:
for valor in persona.values():
    print(f'{valor}')

print('')
#Obtener solo las llaves del diccionario:
for llave in persona.keys():
    print(f'{llave}')