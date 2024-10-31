'''
generar un programa que calcule el factorial de un numero
'''

numeroFinal = int(input('Ingrese el numero maximo -> '))


def factorial(numeroFinal):
    resultado = 1
    for i in range(1, numeroFinal + 1): #Le digo que arranque en 1, en vez de cero, hasta el numero que puse + 1 asi lo incluye
        resultado *= i
        print(resultado)
    #return resultado

print(factorial(numeroFinal))