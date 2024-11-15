'''
Dada una lista de nombres de películas, crea una nueva lista por comprensión que contenga
solo los nombres de películas que contengan el caracter "e" y no finalicen con "s".
peliculas = ["Inception", "Matrix", "Amelie", "E.T.", "Avengers"]
Resultado esperado: ['Inception', 'Amelie', 'E.T.']
'''

peliculas = ["Inception", "Matrix", "Amelie", "E.T.", "Avengers"]
resultado = [pelicula for pelicula in peliculas if 'e' in pelicula and not pelicula.endswith('s') ]

resultado2 = [pelicula for pelicula in peliculas if 'e' in pelicula.lower() and pelicula[len(pelicula) - 1] != 's']

if __name__ == '__main__':
    print(resultado)
    print('------------------------')
    print(resultado2)
