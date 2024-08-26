'''
1. Hacer un programa que nos calcule la hipotenusa de un triángulo rectángulo. Nos
debe preguntar las medidas de los dos catetos y al final indicar el resultado.
hipotenusa=√catetoa2 + catetob2
Se pueden utilizar para prueba como medidas de los catetos los valores 3 y 4, el
valor de la hipotenusa en ese caso es 5.
'''

catetoA = int(input("Ingrese el Cateto A: "))
catetoB = int(input("Ingrese el Cateto B: "))   

while catetoA == 0:
        catetoA = int(input("El Cateto A no puede ser = 0. reintente nuevamente: "))
        hipotenusa = (catetoA**2 + catetoB**2)**0.5
        print("La hipotenusa en base a los catetos obtenidos es: ", hipotenusa)