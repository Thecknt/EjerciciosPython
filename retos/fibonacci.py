print('''
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
''')

lista_fibonacci = []

def fibonacci():
    numero1, numero2 = 0,1 #Con esto inicializo la secuencia

    for _ in range(50):   #Aca genero numeros hasta el 50
        lista_fibonacci.append(numero1)  #El numero actual lo voy agregando a lista
        proximo_valor = numero1 + numero2 #Aca voy sumando los numeros de la secuencia
        numero1 = numero2
        numero2 = proximo_valor #Aca voy actualizando los numeros para el proximo ciclo

    return lista_fibonacci

resultado = fibonacci()

for numero in resultado:
     print(numero, end=', ')