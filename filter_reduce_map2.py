from functools import reduce

inventario = {
    "manzana": 10,
    "pera": 5,
    "pan": 8,
    "leche": 12,
    "queso": 3
}

mas5Unidades = filter(lambda item: item[1] > 5, inventario.items())

print(f"Los productos con mas de 5 Unidades son: {dict(mas5Unidades)}")

descuento10 = map(lambda item: (item[0], item[1] * 0.9), inventario.items())

print(f'Descuento del 10 % aplicado a todos los productos \n{dict(descuento10)}')

productos_dia1 = {"manzana", "pera", "pan", "leche", "queso"}
productos_dia2 = {"pera", "leche", "banana", "queso", "tomate"}

ambos_dias = productos_dia1.intersection(productos_dia2)
ambos_dias2 = productos_dia1 - productos_dia2
ambos_dias3 = productos_dia1 ^ productos_dia2

print(f'productos vendidos en ambos días {ambos_dias}')
print(f'productos vendidos solo el día 1 {ambos_dias2}')
print(f'(diferencia simetrica) productos vendidos en uno u otro día, pero no en ambos{ambos_dias3}')

calificaciones = [85, 90, 78, 92, 88, 76, 95, 89]

mayoresA90 = filter(lambda x: x > 90, calificaciones)
largo = len(calificaciones)
suma = None
promedio = reduce(lambda suma, x: suma + x, calificaciones)
print(f'Las calificaciones mayores a 90 son {list(mayoresA90)}')
print(f'El promedio de las notas es {promedio / largo}')


class producto:
    def __init__(self):
        self.nombre: ""
        self.precio: None
        self.categoria: ""

    def nuevoProducto(self, nombre, precio, categoria):
        self.nombre: nombre
        self.precio: precio
        self.categoria: categoria

    def __str__(self):
        return (f'Producto: {self.nombre} - Precio: ${self.precio} - categoria: {self.categoria}')


productoNuevo = producto()

productoNuevo.nombre = "Televisor"
productoNuevo.precio = 150000.0
productoNuevo.categoria = "Electrodomesticos"
print(productoNuevo)

nuevosProductos = []
nuevosProductos.append(productoNuevo)

productoNuevo1 = producto()
# productoNuevo1.nombre = input("Ingrese un producto para la categoria 'Frutas' -> ")
# productoNuevo1.precio = float(input("Ingrese el precio $ -> "))
productoNuevo1.nombre = "bananas"
productoNuevo1.precio = 2500
productoNuevo1.categoria = "Frutas"
print(f'Nuevo producto -> {productoNuevo1}')
nuevosProductos.append(productoNuevo1)

for producto in nuevosProductos:
    print(f'* {producto}')

nombre = "Milanesas"
precio = 25000
categoria = "Carniceria"
productoNuevo1.nuevoProducto(nombre, precio, categoria)

for producto in nuevosProductos:
    print(f'* {producto}')

productos = [
    {"nombre": "manzana", "precio": 1.5, "categoria": "Fruta"},
    {"nombre": "pera", "precio": 2.0, "categoria": "Fruta"},
    {"nombre": "pan", "precio": 1.0, "categoria": "Panadería"},
    {"nombre": "leche", "precio": 1.8, "categoria": "Lácteos"},
    {"nombre": "queso", "precio": 3.5, "categoria": "Lácteos"}
]

#Tengo que pasar a listas estos iterados para que no se pierda el valor con los for de abajo,sino no puedo realizar las operaciones restantes
frutas = list(filter(lambda x: x["categoria"] == "Fruta", productos))
for fruta in frutas:
    print(f"* Producto: {fruta}")

descuento15 = list(map(lambda x: {"nombre": x["nombre"], "precio": x["precio"] * 0.85}, frutas))

for desc in descuento15:
    print(f" * Producto: {desc}")

totalProductdesc = reduce(lambda x, y: x + y["precio"], descuento15, 0)

print(f'Total de los productos con el descuento aplicado $ {totalProductdesc:.2F}')