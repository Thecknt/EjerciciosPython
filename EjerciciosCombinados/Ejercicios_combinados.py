colores = ('azul','rojo','amarillo')
listaColores = []

for color in colores:
    listaColores.append(color)

print(listaColores)

numeros = [1,2,3,4,5]
numeros.append(6)
print(f'Los nuevos numeros son: {numeros}')
numeros.pop(0)

print(numeros)

frutas = ["manzana", "plátano", "cereza", "naranja"]
frutas.insert(3,"pera")
print(frutas)

for fruta in frutas:
    if "plátano" in frutas:
        print("Existe platano en frutas")
        break

estudiantes = {
    "ana":85,
    "juan":90,
    "Luis":78
}

estudiantes.update({"Sofia":92})
print(estudiantes)

estudiantes["juan"]=95

print(estudiantes)

del estudiantes["Luis"]

print(estudiantes)

#Contador de palabras

palabras = ["manzana", "pera", "manzana", "plátano", "pera", "manzana"]
contadorPalabras = {}
for palabra in palabras:
    if palabra in contadorPalabras:
        contadorPalabras[palabra] += 1
    else:
        contadorPalabras[palabra] = 1

print(contadorPalabras)

#promedio


notas = [8, 5, 3, 2, 10]

promedio = 0


def promedios(notas):
    suma = 0
    cant_notas = len(notas)
    for nota in notas:
        suma += nota

    promedio = suma / cant_notas
    return promedio


respuesta = promedios(notas)

print(f"El promedio es {respuesta}")

oracion = input("Ingrese una palabra para generarla al reves -> ")

def alreves(oracion):
    nueva_oracion = oracion[::-1]
    return nueva_oracion

palabra_alreves = alreves(oracion)

print(palabra_alreves)