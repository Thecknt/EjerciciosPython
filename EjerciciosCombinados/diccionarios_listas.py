persona = {
    "nombre": "Juan",
    "edad": 25,
    "email": "juan@example.com"
}

nombre = persona["nombre"]
print(nombre)

for dato in persona:
    if "telefono" in persona:
        print(f'El telefono es {persona["telefono"]}')
print("No existe el telefono para la persona")

telefono = persona.get("telefono")
if telefono == None:
    print('No Disponible')

calificaciones = {
    "Ana": 85,
    "Luis": 78,
    "Sofía": 92
}

# Mostrar clave

for nombre in calificaciones.keys():
    print(nombre)

# Mostrar valor
for nota in calificaciones.values():
    print(nota)

for nombre, nota in calificaciones.items():
    print(f'Nombre: {nombre}, Calificacion: {nota}')

inventario = {
    "manzanas": 10,
    "naranjas": 15,
    "bananas": 5
}

print(inventario)

inventario["manzanas"] = 15

print(inventario)

inventario.update({"peras": 20})

print(inventario)

del inventario["bananas"]

print(inventario)

precios = {
    "manzana": 1.5,
    "pera": 2.0,
    "banana": 1.2
}


def retornoPreciosTotales():
    precioTotal = 0
    for fruta in precios.values():
        if fruta == 1.5:
            precioTotal += 1.5 * 3
        elif fruta == 2.0:
            precioTotal += 2.0 * 2
        elif fruta == 1.2:
            precioTotal += 5 * 1.2
    return precioTotal


resultado = retornoPreciosTotales()
print(f'El precio total es de ${resultado}')

# Aumento del 10%
for value in precios:
    precios[value] *= 1.1

print(precios)

biblioteca = {
    "Ficción": [],
    "Ciencia": [],
    "Historia": []
}
print(biblioteca)
biblioteca["Ficción"].append("volver al futuro")
biblioteca["Ficción"].append("La Mazacre de Chainsaw")
biblioteca["Ficción"].append("Deux Ex Machine")
biblioteca["Ciencia"].append("Pinguins Life's")
biblioteca["Ciencia"].append("The Patagonian")
biblioteca["Historia"].append("World War")
biblioteca["Historia"].append("the Pianist")

print(biblioteca["Ciencia"])

for genero, books in biblioteca.items():
    print(f'Los libros correspondientes al genero {genero} son: ')
    for book in books:
        print(f'* {book}')