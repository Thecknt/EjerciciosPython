'''
2. Hacer un programa que calcule la cantidad de segundos transcurridos desde las 0
horas hasta un momento determinado por el usuario ingresando horas, minutos y
segundos. Validar que la cantidad ingresada de horas, minutos y segundos
represente una hora válida, en caso afirmativo informar el error
'''

print("****************************************************************")
print("*         Bienvenidos a la Calculadora de segundos             *")
print("****************************************************************")

horas = int(input("Ingrese las horas: "))
while horas <0 or horas >23:
    print("El valor de las hs debe estar comprendido entre 0 y 23")
    horas = int(input("Reintente nuevamente: "))

minutos = int(input("Ingrese los minutos: "))
while minutos >59 or minutos <0:
    print("El valor de los seg debe estar comprendido entre 0 y 59")
    minutos = int(input("Reintente nuevamente: "))

segundos = int(input("Ingrese los segundos: "))
while segundos >59 or segundos <0:
    print("El valor de los min debe estar comprendido entre 0 y 59")
    segundos = int(input("Reintente nuevamente: "))


print(f"Vamos a calcular los segundos transcurridos desde las \n {horas}Hs:{minutos}Min:{segundos}Seg.")
SegundosTotales = (horas * 3600) + (minutos * 60) + segundos

print("---------------------------------------------")
print("| Han transcurrido", SegundosTotales,"segundos en total  |")
print("---------------------------------------------")