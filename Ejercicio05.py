'''
5. Realizar un programa que ingrese un día y un mes e indique a que estación del año
pertenece esa fecha (otoño, invierno, primavera o verano)
'''

print("********************************************")
print("*        Estaciones del año                *")
print("********************************************")

print("")
dia = 1
mes = 1
while dia > 0 and dia < 32 or mes > 0 and mes < 13:
    print("Para salir ingrese en el DIA 0")
    dia = int(input("Ingrese el dia del mes: "))
    if dia == 0:
        print("Gracias por utilizar la App")
        break
    mes = int(input("Ingrese el mes del año: "))
    if dia > 19 and mes == 3 or mes == 4 or mes == 5:
        print("La fecha pertenece a la estación de Otoño")
        print("********************************************")
    if dia > 20 and mes == 6 or mes == 7 or mes == 8:
        print("La fecha pertenece a la estación de Invierno")
        print("********************************************")
    if dia > 22 and mes == 9 or mes == 10 or mes == 11:
        print("La fecha pertenece a la estación de Primavera")
        print("********************************************")
    if dia > 20 and mes == 12 or mes == 1 or mes == 2:
        print("La fecha pertenece a la estación de Verano")
        print("********************************************")