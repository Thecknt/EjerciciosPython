#Escribe un programa que determine si un número ingresado por el usuario es par o impar.

numero = int(input('Ingrese un numero '))

if numero % 2 == 0:
    print(f'El numero {numero} es Par')
else:
    print(f'El numero {numero} es impar')