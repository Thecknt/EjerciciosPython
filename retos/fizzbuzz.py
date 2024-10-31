print('''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
''')

numeros = []
for numero in range(1,100+1):
    numeros.append(numero)

contador = 0
for numero in numeros:

    if numero % 3 == 0 and numero %5 == 0:
        numeros.remove(numero)
        numeros.insert(contador,'fizzbuz')
    else:
        if numero % 3 == 0:
            numeros.remove(numero)
            numeros.insert(contador,'fizz')
        elif numero % 5 == 0:
            numeros.remove(numero)
            numeros.insert(contador,'buzz')
    contador += 1
    print(numero,end='\n')

print(f'La lista de numeros es: {numeros}')