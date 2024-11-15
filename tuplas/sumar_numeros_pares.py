#Escribe un programa que reciba una tupla de números y devuelva una nueva tupla con solo los números mayores a 10.

numeros = ((5,10),(2,8),(4,5))
pares = []

for item in numeros:
    for numero in item:
        if numero % 2 == 0:
            pares.append(numero)

resultado = tuple(pares)
print(resultado)