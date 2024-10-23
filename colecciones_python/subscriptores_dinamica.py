
print(" *** Lista de Suscriptores ***")

#Definimos el ser inicial:
#suscriptores = {} asi se define un diccionario vacio
suscriptores = set() #aca se define un set vacio

numero_suscriptores = int(input('Proporciona el numero de suscriptores iniciales: '))
for _ in range(numero_suscriptores):
    suscriptores.add(input("Ingrese su email -> "))

print(f'Lista de subscriptores Inicial {suscriptores}')

#Verificar si un nuevo suscriptor ya esta en la lista
nuevo_suscriptor = input('Ingrese el nuevo Suscriptor: ')

if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya esta en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado a la lista, {nuevo_suscriptor}')

print(f'La lista de suscriptores es: {suscriptores}')

#eliminar suscriptor
suscriptor_eliminar = input('Proporciona el suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} fue eliminado exitosamente')
print(f'Lista de suscriptores {suscriptores}')

print(f'La cantidad de suscriptores es {len(suscriptores)}')

#Mostrar la lista de suscriptores

print(f'***  Lista de suscriptores  ***')
for suscriptor in suscriptores:
    print(f'* {suscriptor}')
