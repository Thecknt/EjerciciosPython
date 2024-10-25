#print('''
 #Almacenar una lista con 12 elementos que contengan listas con signo del zodiaco, mes y día desde y mes y día hasta.
 #Ingresar por teclado un día y un mes, indicar a qué sigo del zodiaco corresponde.
 #* Aries: 21 de marzo al 20 de abril
 #* Géminis: 21 de mayo al 21 de junio
 #* Leo: 24 de julio al 23 de agosto
 #* Libra: 24 de septiembre al 22 de octubre
 #* Sagitario: 23 de noviembre al 21 de diciembre
 #* Acuario: 21 de enero al 19 de febrero
 #* Tauro: 21 de abril al 20 de mayo
 #* Cáncer: 22 de junio al 23 de julio
 #* Virgo: 24 de agosto al 23 de septiembre
 #* Escorpio: 23 de octubre al 22 de noviembre
 #* Capricornio: 22 de diciembre al 20 de enero
 #* Piscis: 20 de febrero al 20 de marzo
#''')

print('*** ---------¿Cual es tu Signo del Zodiaco?--------- ***')
print('')
zodiaco = [
#   nombre    tupla1    tupla2
    ['Aries', (21, 3), (20, 4)],
    ['Tauro', (21, 4), (20, 5)],
    ['Géminis', (21, 5), (21, 6)],
    ['Cáncer', (22, 6), (23, 7)],
#   nombre   tupla1    tupla2
    ['Leo', (24, 7), (23, 8)],
    ['Virgo', (24, 8), (23, 9)],
    ['Libra', (24, 9), (22, 10)],
    ['Escorpio', (23, 10), (22, 11)],
    ['Sagitario', (23, 11), (21, 12)],
#   nombre            tupla1  tupla2
    ['Capricornio', (22, 12), (20, 1)],
    ['Acuario', (21, 1), (19, 2)],
    ['Piscis', (20, 2), (20, 3)],
]

dia = int(input('Ingrese el dia de su cumpleaños-> '))
mes = int(input('Ingrese el mes de su cumpleaños-> '))

def obtener_signo(dia, mes):
  for signo in zodiaco:
    nombre_signo = signo[0]
    tupla1 = signo[1]
    tupla2 = signo[2]

    primera_condicion = (mes == tupla1[1] and dia >= tupla1[0])  # primero chequeo que el mes de la tupla 1 sea igual al mes y que el día sea mayor o igual que al de tupla 1
    segunda_condicion = (mes == tupla2[1] and dia <= tupla2[0])  # Luego chequeo en la tupla 2 si Mes es igual a el mes de la tupla 2 y si el día es menor o igual al de tupla 2
    tercera_condicion = (mes > tupla1[1] and mes < tupla2[1])  # y por ultimo el Mes que está entre el mes de tupla 1 y el mes de tupla 2
    #cualquiera de estas condiciones me devuelve False, solo la que cumple devuelve True

    if primera_condicion or segunda_condicion or tercera_condicion:
        print('---------------------------------')
        print(f"Tu signo zodiacal es {nombre_signo}")
        print('---------------------------------')
        break

print('')
signo = obtener_signo(dia, mes)
print('')

opcion = input('¿Desea chequear otra fecha? (si/no)-> ')

while opcion.lower() != 'no':
    dia = int(input('Ingrese el dia de su cumpleaños-> '))
    mes = int(input('Ingrese el mes de su cumpleaños-> '))
    signo = obtener_signo(dia, mes)
    opcion = input('¿Desea chequear otra fecha? (si/no)-> ')

print('Gracias por utilizar nuestra app!')