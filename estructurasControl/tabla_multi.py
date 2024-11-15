#Escribe un programa que genere la tabla de multiplicar de un número ingresado por el usuario.

multiplicador = int(input('Ingrese un numero, para determinar la tabla: '))
print(f'La tabla sera del numero... {multiplicador}')
tabla = []
resultado = 0
for i in range(1,11):
    resultado = i*multiplicador
    tabla.append(resultado)
contador =1
for numero in tabla:
    print(f'{contador}x{multiplicador}={numero}\n')
    contador += 1

