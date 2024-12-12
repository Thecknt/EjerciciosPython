numeros = []

for i in range(1,100+1):
    numeros.append(i)

print(numeros)

print("------------------------------------")

listaPares = []
for numero in numeros:
    if numero % 2 == 0:
        listaPares.append(numero)

print(listaPares)

print("-----------------------------------")

numeroPrevio = 0
suma = 0
i = 1

while i < 51:
    numeroPrevio = i
    suma += numeroPrevio
    i+=1

print("la suma de los numeros es: ",suma)

print("-----------------------------------")
numero = False

while numero == False:
    numerosCliente = int(input(f"Ingrese los numeros que me desee, para finalizar ingrese un numero negativo: "))
    if numerosCliente < 0:
        numero = True

print("------------------------------------------------")
encontrarNumero= [1,8,5,4,3,7,10]
cont = 0
for numero in encontrarNumero:
    cont +=1
    if numero == 7:
        print("Se encontro el numero 7 en el ciclo: ",cont)
        break

print("---------------------------------------------")

listadoPalabras = ["hola","cariño","todo","bien","cariño"]

print(listadoPalabras[::-1])

nuevoListadoPalabras = set(listadoPalabras)
print(nuevoListadoPalabras)

print("--------------------------------------------")

listadoNumero = [1,8,5,3,9]

nuevoListadoNumeros = []
for numero in listadoNumero:
    cuadrado = numero**2
    nuevoListadoNumeros.append(cuadrado)

print("El nuevo listado es: ",nuevoListadoNumeros)
print("---------------------------------------------")

numeroMasChico = 10000
numeroMasGrande = 1

for numero in listadoNumero:
    if numero > numeroMasGrande:
        numeroMasGrande = numero
    elif numero < numeroMasChico:
        numeroMasChico = numero

print(f"El numero mas chico es {numeroMasChico}")
print(f"El numero mas Grande es {numeroMasGrande}")

print("--------------------------------------")

abecedario = {}