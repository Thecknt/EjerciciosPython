print('''
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 que
no sean múltiplos de 5. A y B se ingresan desde el teclado.
''')

listaA = []
listaB = []
opcion = ''

while opcion.lower() !='no':
    numeroA = int(input('Ingrese un numero para la lista A-> '))
    listaA.append(numeroA)
    numeroB = int(input('Ingrese un numero para la lista B-> '))
    listaB.append(numeroB)
    print(listaA)
    print(listaB)
    opcion = input('Desea agregar mas numeros? (si/no)')

resultado = [numero for numero in listaA and listaB if numero % 7 == 0 and numero % 5 !=0]
print('Recuerde que si el numero es multiplo de 5 y 7 no se imprimira por pantalla')
print(f'El resultado de los multiplos de 7 es: {resultado}')