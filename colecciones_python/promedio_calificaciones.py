print()
print("***     Bienvenido al Sistema de Calificaciones    ***")
calificaciones = []
suma = 0
cantidad_calificaciones = int(input("Indique la cantidad de calificaciones que ingresara para obtener el promedio -> "))

for i in range(cantidad_calificaciones):
    nota = int(input(f'Ingrese la calificacion {i + 1} -> '))
    calificaciones.append(nota)
    print(nota)

for nota in calificaciones:
    suma = suma + nota

promedio = suma / cantidad_calificaciones
print(f'El promedio de calificaciones es: {promedio}')