'''
Ejercicio 2: Contar Elementos en una Lista
Objetivo: Dada una lista de elementos, cuenta cuántas veces aparece cada elemento en la lista.

Instrucciones:

Crea una función llamada contar_elementos(lista).
La función debe recibir una lista y devolver un diccionario donde las claves sean los elementos de la lista y los valores sean las veces que aparece cada elemento.
Usa un ciclo para realizar el conteo.
Ejemplo:
python
Copiar código
# Llamada de prueba:
contar_elementos(["manzana", "naranja", "manzana", "pera", "naranja", "manzana"])
# Salida esperada: {"manzana": 3, "naranja": 2, "pera": 1}
'''

elementos = ["manzana", "naranja", "manzana", "pera", "naranja", "manzana"]

def contar_elementos(lista):
    listado_nuevo = {}  # Diccionario para almacenar los conteos
    for elemento in lista:
        if elemento in listado_nuevo:
            listado_nuevo[elemento] += 1  # Incrementa el conteo si ya existe
        else:
            listado_nuevo[elemento] = 1  # Inicializa el conteo si no existe
    return listado_nuevo

print(contar_elementos(elementos))
if __name__ == ' __main__':
    print(f'{contar_elementos(elementos)}')