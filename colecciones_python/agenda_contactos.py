print('---------------------------------- Agenda de contactos ------------------------------------')

agenda = {
    'Carlos':{
        'telefono':'455646',
        'email':'carlos@gmail.com',
        'direccion':'Calle Falsa 123'
    },
    'Maria':{
        'telefono':'546413',
        'email':'Maria@gmail.com',
        'direccion':'Calle Falsa 321'
    },
    'Pedro':{
        'telefono': '844611',
        'email': 'Pedro@gmail.com',
        'direccion': 'Calle Falsa 456'
    }
}
print('')
for llave, valor in agenda.items():
    print(f'{llave} : {valor}')
print('')

#Acceder a la informacion de un contacto en especifico:
print(f''' Informacion del contacto de Maria:
Telefono: {agenda['Maria']['telefono']}
Email: {agenda['Maria']['email']}
Direccion: {agenda.get('Maria').get('direccion')}
''')
print('')

#Agregar un nuevo contacto:
agenda['Ana'] = {
        'telefono':'6854236',
        'email':'Ana@gmail.com',
        'direccion':'Calle Falsa 789'
}
print(f''' Informacion de contacto de Ana ->
Telefono: {agenda['Ana']['telefono']}
Email: {agenda['Ana']['email']}
Direccion: {agenda.get('Ana').get('direccion')}
''')
print('')

#Eliminar un elemento de agenda:
agenda.pop('Pedro')
# del agenda['Pedro']
print('''Listado de contactos: 
----------------------------------------------
''')
for nombre, valor in agenda.items():
    print(f'''Nombre: {nombre}: 
Telefono: {valor.get('telefono')}
Email: {valor.get('email')}
Direccion: {valor.get('direccion')}
''')
print('')
print('')