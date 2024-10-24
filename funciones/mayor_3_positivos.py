
print('''
-------------------Ejercicio 1 Funciones-------------------------
Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver None
en caso de no haber ninguno. Desarrollar también un programa de prueba para
ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un
mensaje informativo si éste no existe
''')

numeros = []

def mayor_numero(numero1,numero2,numero3):
    if numero1 == numero2 == numero3:
        print(f'Entre los numeros ingresados no hay un numero mayor estricto:\n{numero1} - {numero2} - {numero3}')
        return None
    elif numero1 > numero2 and numero2 > numero3:
        numeroMayor = numero1
        numeroIntermedio = numero2
        numeroMenor = numero3
        numeros.append(numeroMayor)
        numeros.append(numeroIntermedio)
        numeros.append(numeroMenor)
    else:
        if numero2 > numero1 and numero1 > numero3:
            numeroMenor = numero3
            numeroMayor = numero2
            numeroIntermedio = numero1
            numeros.append(numeroMayor)
            numeros.append(numeroIntermedio)
            numeros.append(numeroMenor)
        else:
            if numero3 > numero2 and numero2 > numero1:
                numeroMayor = numero3
                numeroIntermedio = numero2
                numeroMenor = numero1
                numeros.append(numeroMayor)
                numeros.append(numeroIntermedio)
                numeros.append(numeroMenor)
    return print(f'El numero mayor es: {numeroMayor}\n'
                 f'El numero intermedio es {numeroIntermedio}\n'
                 f'y por ultimo el numero menor es {numeroMenor}')

numero1 = int(input(f'Ingrese el numero 1 ->'))
numero2 = int(input(f'Ingrese el numero 2 ->'))
numero3 = int(input(f'Ingrese el numero 3 ->'))

mayor_numero(numero1,numero2,numero3)