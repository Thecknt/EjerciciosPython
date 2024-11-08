'''
 * Crea una función que ordene y retorne una matriz de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 *   o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 *   automáticamente.
'''

lista_numeros = [8,5,4,7,2,9,10,1,3,6]


def ordenar_numeros(numeros, orden):
    if orden.lower() == 'asc':
        lista_Asc = []  # Lista vacía para los números ordenados
        # Repetimos el proceso para cada número en la lista original
        for _ in range(len(numeros)):
            menor = numeros[0]  # Asumimos que el primer número es el menor
            for numero in numeros:  # Comparamos con todos los números
                if numero < menor:  # Si encontramos un número menor
                    menor = numero  # Actualizamos el menor
            lista_Asc.append(menor)  # Agregamos el menor a la lista ordenada
            numeros.remove(menor)  # Lo eliminamos de la lista original
        return lista_Asc  # Devolvemos la lista ordenada

        # Si queremos ordenar en orden descendente
    elif orden.lower() == 'desc':
        lista_desc = []  # Lista vacía para los números ordenados
        # Repetimos el proceso para cada número en la lista original
        for _ in range(len(numeros)):
            mayor = numeros[0]  # Asumimos que el primer número es el mayor
            for numero in numeros:  # Comparamos con todos los números
                if numero > mayor:  # Si encontramos un número mayor
                    mayor = numero  # Actualizamos el mayor
            lista_desc.append(mayor)  # Agregamos el mayor a la lista ordenada
            numeros.remove(mayor)  # Lo eliminamos de la lista original
        return lista_desc  # Devolvemos la lista ordenada

if __name__ == '__main__':
    resultado = ordenar_numeros(lista_numeros,'DESC')
    print(resultado)