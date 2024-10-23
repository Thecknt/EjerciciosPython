print()
print('***     Operaciones en Set     ***')
print('')
conjunto_a = {1,2,3,4}
conjunto_b = {3,4,5,6}

union = conjunto_a | conjunto_b
print(f'La union de los conjuntos es: {union}',end=" ")
print(' ')

interseccion = conjunto_a & conjunto_b
print(f'\nla interseccion entre el conjunto a y b es: {interseccion}',end=" ")
print('')

diferencia = conjunto_a - conjunto_b
print(f'\nLa diferencia entre conjuntos es: {diferencia}',end=" ")