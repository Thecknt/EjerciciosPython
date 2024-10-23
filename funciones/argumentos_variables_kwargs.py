#Arg - arguments - tupla
#Kwargs - Keyword arguments (key,value) como un dict

print('*** Argumentos variables ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')

superheroe_superpoderes('Spiderman',
                        'Instinto Aracnido','Telaraña',
                        edad=17, empresa='Marvel')
print('')
superheroe_superpoderes('ironman', 'Armadura','Playboy',edad=45)