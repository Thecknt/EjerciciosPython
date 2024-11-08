from random import randint

print('''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
''')

palabra1 = 'Amor'
palabra2 = 'roMa'

largo = len(palabra1)

def anagrama(palabra1, palabra2):
    if palabra1.lower() == palabra2.lower():
        return False
    else:
        print(palabra1.lower(), palabra2.lower())
        return sorted(palabra1.lower()) == sorted(palabra2.lower())

if __name__ == '__main__':
    resultado = anagrama(palabra1,palabra2)
    print(f'{resultado}')