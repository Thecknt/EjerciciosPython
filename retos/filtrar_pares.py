'''
Instrucciones:

Define una función llamada filtrar_pares(lista_numeros).
La función debe recibir una lista de números enteros y devolver una nueva lista que contenga solo los números pares.
Usa un ciclo o una comprensión de listas para realizar el filtrado.
Ejemplo:

python
Copiar código
# Llamada de prueba:
filtrar_pares([1, 2, 3, 4, 5, 6])
# Salida esperada: [2, 4, 6]
'''

lista_numeros = [1, 2, 3, 4, 5, 6]

def filtrar_pares(lista_numeros):
    pares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares


if __name__ == '__main__':
    resultado = filtrar_pares(lista_numeros)
    print(f'El listado de pares es: {resultado}')
