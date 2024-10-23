print('---------funcion con argumentos variables (*args)----------')

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'\tSuperheroe: {superheroe} - {nombre} - {args}')
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')
#Llamar a la funcion:

superheroe_superpoderes('Spiderman', 'Peter Parker','Instinto aracnido','Telaña')
print('---------------------------------------------------------------------')
superheroe_superpoderes('Iron Man', 'Tony Stark','Super armadura','Misiles','Lazers')