print('------------comprension Listas------------------')

numeros = range(10 + 1)

pares = [ x for x in numeros if x %2 == 0 ]
print(f'Los numeros pares son: {pares}')
print('------------------------------------------------')

print('')

print('<----- otro ejemplo de comprension por listas ------>')

lista_numeros = [1,2,3,4,5]

potencia = [ x**2 for x in lista_numeros]
print(f'La lista de numeros potenciados por si mismos son: {potencia}')

print("-------Iterar nombres por comprension---------")

nombres =['Jesica','Priscila','Thomas','Damian']

saludo =[f'Hola {nombre}'for nombre in nombres]
print(f'{saludo}')