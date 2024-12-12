#Dada una tupla con los nombres de los meses del año, solicita al usuario un número entre 1 y 12 e imprime el mes correspondiente.

meses = ('Enero',1),('Febrero',2),('Marzo',3),('Abril',4),('Mayo',5),('Junio',6),('Julio',7),('Agosto',8),('Septiembre',9),('Octubre',10),('Noviembre',11),('Diciembre',12)

mes = int(input('Ingrese un numero equivalente a un mes del año, para pasarlo a cadena '))

if mes >0 and mes <13:
    for item in meses:
        meses.app
        if item[1] == mes:
            print(f'El Mes ingresado es {item[0]}')
else:
    print('El mes es inexistente')

