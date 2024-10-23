print('***    Combinacion de Listas y Tuplas    ***')

# Definir una lista que almacena tuplas de productos

productos = [
    ('P001','Camiseta', 20.00),
    ('P002','Jeans', 30.00),
    ('P003','Sudadera', 40.00)
]

# Imprimir la informacion de cada producto
# y ademas calculamos el precio total

precio_total = 0
print()
print('Informacion de los productos')
for producto in productos:
    id, descripcion, precio = producto   #hago un unpacking de la tupla
    precio_total += precio # sino tambien  precio_total+=producto[2]
    print(producto)

print(f'El total de los productos es: u$s{precio_total}')