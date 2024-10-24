print('''
Intercalar los elementos de una lista entre los elementos de otra. La intercalación
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3] y
lista2 =[5,9,7], lista1 deberá quedar como [8,5,1,9,3,7].
''')

lista1 = [8, 1, 3]
lista2 =[5,9,7]

for i in range(len(lista2)):
    lista1.insert(i*2+1,lista2[i])
                 #0*2+1 = 1 -> 5
                 #1*2+1 = 3 -> 9
                 #2*2+1 = 5 -> 7
print(lista1)
