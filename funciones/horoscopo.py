print('''
Realizar un programa que pida al usuario que ingrese el día y mes de su
cumpleaños (aplique a función de validación de fecha del punto anterior) y el
programa le debe decir a qué signo del zodíaco corresponde.
*Aries: 21 de marzo al 20 de abril
*Tauro: 21 de abril al 20 de mayo
*Géminis: 21 de mayo al 21 de junio
*Leo: 24 de julio al 23 de agosto
*Libra: 24 de septiembre al 22 de octubre
*Sagitario: 23 de noviembre al 21 de diciembre
*Acuario: 21 de enero al 19 de febrero
*Cáncer: 22 de junio al 23 de julio
*Virgo: 24 de agosto al 23 de septiembre
*Escorpio: 23 de octubre al 22 de noviembre
*Capricornio: 22 de diciembre al 20 de enero
*Piscis: 20 de febrero al 20 de marzo
''')
print('*** ------ Horoscopo ------ ***')
dia = int(input('Ingrese el dia de su cumpleaños (1-31)-> '))
mes = int(input('Ingrese el mes de su cumpleaños (1-12)-> '))

def horoscopo(dia,mes):
    if mes == 1 and dia <=20:
        print(f'Tu signo es Capricornio')
    elif mes == 1 and dia >= 21:
        print('hola')

horoscopo = {
'Aries': {
    'inicio':'21-03',
    'fin':'20-04'
    },
'Tauro': {
    'inicio':'21-04',
    'fin':'20-05'
    },
'Géminis':{
    'inicio':'21-05',
    'fin':'21-06'
}
}

for signo in horoscopo:
    print(signo)

