print('***    manejo de sets o conjuntos   ***')
print()
#Crear un conjunto:

mi_set = {1,2,3,4,5,4}
print(f'Mi_set {mi_set}')
print()
#Agregar elemento al Set
mi_set.add(6)
mi_set.add(7)

print(f'Mi set modificado: {mi_set}')
print()
# Agregar un elemento duplicado, cuando lo hago lo ignora
mi_set.add(3)
print(f'Mi set modificado: {mi_set}')
print()
# Eliminar un elemento del conjunto:
mi_set.remove(1)

print(f'Mi set luego de eliminar el 1: {mi_set}')
print()
print("Iterando el set o conjunto: ")
for numero in mi_set:
    print(f'{numero}',end=' - ')
print()
# Comprobar si existe un elemento en el conjunto

print(f'\nExiste el 4 en mi set? {4 in mi_set}')

print()
print(f'El largo del set es: {len(mi_set)}')