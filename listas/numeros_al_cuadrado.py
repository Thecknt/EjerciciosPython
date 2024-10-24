
print('''
 Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
 donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10
 valores de la lista utilizando segmentación de listas.
''')

tope = int(input('Ingrese la cantidad de numeros que se potenciaran al cuadrado -> '))
lista_numeros = []

for numero in range(1,tope + 1):
    resultado = numero**2
    lista_numeros.append(resultado)

largo = len(lista_numeros)
if largo >=10:
    print(f'Imprimiendo la lista de numeros hasta el 10: \n{lista_numeros[:10]}')
else:
    print(lista_numeros)
