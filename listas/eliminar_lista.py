print('''
Eliminar de una lista de palabras las palabras que se encuentren en una segunda
lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.
''')

lista1 = ['Hola','soy','de','la','lista1','python']
lista2= ['pertenezco','a','la','lista2','python']
lista_unificada = []

print(f'La primer lista contiene: {lista1}\n'
      f'La segunda lista contiene: {lista2}')
for palabra in lista1:
    if palabra in lista2:
        print(f'Las palabra repetida es: {palabra}')
        lista1.remove(palabra)
        lista2.remove(palabra)

lista_unificada.append(lista1)
lista_unificada.append(lista2)
print(f'Nueva lista: {lista_unificada}')