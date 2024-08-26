'''
4. Realizar un programa que permita el ingreso de un conjunto indeterminado de datos
numéricos (sin incluir el cero) y obtenga: 
• El mayor de los números negativos 
• El menor de los números positivos.
• El promedio de todos los valores ingresados (sin incluir el 0).
'''

exit = True
mensajeSalida = "Gracias por utilizar el sistema de ordenamiento"
cont = 0
while True:
    print("*****************************************************")
    print("*  Bienvenido al sistema de ordenamiento numerico   *")
    print("*****************************************************")
    print("")
    print("Para salir ingrese 0")

    numero1 = int(input("Ingrese el primer numero: "))
    if numero1 == 0:
        print(mensajeSalida)
        exit = False
        break
    numero2 = int(input("Ingrese el segundo numero: "))
    if numero2 == 0:
        print(mensajeSalida)
        exit = False
        break
    numero3 = int(input("Ingrese el tercer y ultimo numero: "))
    if numero3 == 0:
        print(mensajeSalida)
        exit = False
        break
    print("*******************************")
    print("* Los numeros ingresados son: *")
    print(f"*         {numero1}                   *")
    print(f"*         {numero2}                  *")
    print(f"*         {numero3}                  *")
    print("*******************************")
    if numero1 >= numero2 and numero1 >= numero3:
        mayor = numero1
        if numero2 >= numero3:
            medio = numero2
            menor = numero3
            negativo = numero3
        else:
            medio = numero3
            menor = numero2
            negativo = numero2
    elif numero2 >= numero1 and numero2 >= numero3:
        mayor = numero2
        if numero1 >= numero3:
            medio = numero1
            menor = numero3
            negativo = numero3
        else:
            medio = numero3
            menor = numero1
            negativo = numero1
    else:
        mayor = numero3
        if numero1 >= numero2:
            medio = numero1
            menor = numero2
            negativo = numero2
        else:
            medio = numero2
            menor = numero1
            negativo = numero1
    promedio = numero1+numero2+numero3 / 3
    if numero1 <0 and numero2 <0 and numero3 <0:
        print("Todos los numeros son negativos, el mayor numero de los negativos es:",mayor)
    if numero1>0 and numero2>0 and numero3>0:
        print("Todos los numeros son positivos,el menor de los numeros positivos es:",menor)   
    if negativo <0 and menor >0:
        print(f"El numero mayor de los numero negativos es: {negativo}\nEl numero menor de los positivos es: {menor}\n********************************************************")
    if negativo >0 or menor >0:
        print(f"No se ingresaron numeros negativos. \nEl numero menor de los positivos es: {menor}\n********************************************************")
    if mayor > 0 and medio > 0:
        print(f"El numero mayor de los numero negativos es: {negativo}\nEl numero menor de los positivos es: {medio}")
    print("El promedio de los numeros ingresados es: ",promedio,"\n********************************************************")