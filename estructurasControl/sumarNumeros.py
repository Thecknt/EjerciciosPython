#Crea un programa que calcule la suma de todos los números impares entre 1 y 100.

numeros = []

for i in range(1,101):
    numeros.append(i)

print(numeros)

suma = 0
for numero in numeros:
    if numero % 2 == 0:
        suma += numero

print(f'La suma total de los numeros es: {suma}')
