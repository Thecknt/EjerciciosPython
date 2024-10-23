
print('***  Playlist de Canciones  ***')
print()
#creo la lista vacia
lista_reproduccion = []

numero_canciones = int(input('¿Cuantas canciones desea agregar? ->'))

#Iteramos cada elemento de la lista para agregar un nuevo elemento
for cancion in range(numero_canciones):
    cancion = input(f'Ingrese la cancion y banda que desea agregar: {cancion+1}-> ')
    lista_reproduccion.append(cancion)

#lista_reproduccion.append('Hotel California - Eagles')
#lista_reproduccion.append('Staying Alive - Bee Gees')
#lista_reproduccion.append('Dream on - Aerosmith')

#Ordenar lista en orden alfabetico
lista_reproduccion.sort()

#Muestro la lista ordenada
print(f'Lista de reproduccion en orden Alfabetico Ascendente '
      f'\n{lista_reproduccion}')
print()
lista_reproduccion.sort(reverse=True)
print(f'Lista de reproduccion en orden Descendente '
      f'\n{lista_reproduccion}')
print()
for cancion in lista_reproduccion:
    print(f'|> {cancion}')