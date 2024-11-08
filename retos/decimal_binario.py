'''
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
'''

numero = int(input('Ingrese un numero-> '))
binario= []

def decimal_binario(numero):
    if numero == 0:
        return
    else:
        temp = numero % 2
        decimal_binario(numero // 2)
        binario.append(temp)

if __name__ == '__main__':
    decimal_binario(numero)
    print(f'El numero binario es: {binario}')
    for numero in binario: print(numero,end=' ')