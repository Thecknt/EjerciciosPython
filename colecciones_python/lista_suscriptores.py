
print("")
print('***    Lista de suscriptores    ***')

lista_suscriptores = []

respuesta = input('Desea agregar un suscriptor al boletin informativo? -> ')
if respuesta.lower() == "si":
    cantidad = int(input('¿Cuantos agregara? -> '))

while respuesta.lower() == "si":
    for item in range(cantidad):
        print(f'Suscriptor: {item + 1}')
        suscriptor = ((input('Ingrese su nombre: ->'), input('Ingrese su email: ->')))
        if suscriptor in lista_suscriptores:
            print('El suscriptor ya se encuentra agregado al boletin!')
            suscriptor = ((input(f'Ingrese su nombre: ->'), input(f'Ingrese su email: ->')))
        else:
            print('---------------------------------')
        lista_suscriptores.append(suscriptor)
    respuesta = input('Desea agregar un suscriptor al boletin informativo? -> ')

#print(f'La lista de suscriptores es: {lista_suscriptores}',end=" ")

#Aca por cada uno de los tuplas voy iterando y desempaquetando
    for suscriptor in lista_suscriptores:
        nombre, email = suscriptor
        print(f'* Nombre suscriptor:{nombre} - email: {email}')

print('\nSaliendo de la lista de suscriptores, gracias por utilizar el servicio!')