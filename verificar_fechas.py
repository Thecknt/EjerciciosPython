from datetime import *

print('''
Hacer una función que nos indique con verdadero o  falso si una fecha ingresada en
el formato día, mes, año es válida o inválida. Considerar que será conveniente
hacer una función que verifique si un año es bisiesto, considerando que un año es
bisiesto si es divisible por 4 pero no es divisible por 100, o en el caso que sea
divisible por 400. Desarrollar el código para probarla.
''')

print('Vamos a ingresar su fecha de nacimiento: (dd-MM-yyyy)')
dia = int(input('Ingrese su dia de nacimiento -> '))
mes = int(input('Ingrese su mes de nacimiento, solo numeros del 1 al 12 -> '))
anio = int(input('Ingrese su año de nacimiento solo numeros (YYYY)-> '))

fecha=[]

contador = 0

def validar_fecha(dia,mes,anio):
    global contador
    if 1 <= dia <= 31:
        contador += 1
        fecha.append(dia)
    if 1 <= mes <= 12:
        fecha.append(mes)
        contador+=1
    if 1950 <= anio <= 2025:
        fecha.append(anio)
        contador += 1
    return contador

def es_bisiesto(anio):
    calculo = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
    if calculo:
        print(f'El año {anio} es bisiesto!')
    else:
        print(f'El año {anio} No es biciesto!')


resultado = validar_fecha(dia,mes,anio)

if resultado == 3:
    print(f'La fecha ingresada es correcta!\n {fecha}')
    es_bisiesto(anio)
else:
    print('La fecha ingresada no es correcta!')