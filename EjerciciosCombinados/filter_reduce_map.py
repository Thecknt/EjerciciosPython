from functools import reduce

numeros = [1, 2, 3, 4, 5, 6]

numeros_pares = filter(lambda x: x % 2 == 0, numeros)

print(list(numeros_pares))

numeros_impares = filter(lambda x: x%2 != 0, numeros)

print(f'Los numeros impares son: {list(numeros_impares)}')

multiplicados = map(lambda x: x*3 , numeros)

#Devolver la lista de todos los numeros multiplicados * 3
print(f'Los numeros multiplicados son: {list(multiplicados)}')

#Sumar los numeros entre si y devolver 1 solo resultado
numeros_sumados = reduce(lambda x,y: x+y, numeros)

print(f'El numero final es {numeros_sumados}')

nombres = ["Ana", "Juan", "Cristina", "Pedro", "Luisa", "Carolina"]

#Pasar todas las letras a mayusculas
nombres_a_mayusculas = map(lambda x: x.upper(),nombres)

print(list(nombres_a_mayusculas))

#Filtrar nombres mayores a 5 letras
nombres_mayores_a_5caracteres = filter(lambda x: len(x) > 5, nombres)

print(list(nombres_mayores_a_5caracteres))

#Trabajando con diccionarios y maps

productos = {
    "manzana": 10,
    "pera": 12,
    "plátano": 8,
    "naranja": 15,
    "sandía": 18
}

#Devolver los productos aumentados en un 10%

aumento_10 = map(lambda item: (item[0], item[1] * 1.1), productos.items())

#filtrar productos mayores a 15

productos_filtrados = filter(lambda item: item[1] > 15, aumento_10)

print(dict(aumento_10))
print(dict(productos_filtrados))