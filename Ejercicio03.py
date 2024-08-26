'''
Realizar un programa que encuentre las raíces del polinomio de segundo grado ax 2
+ bx + c = 0, utilizando la fórmula resolvente. Se requiere que si la raíz es única, se
indique y se muestre un solo valor. En el caso que las raíces sean imaginarias la
expresión de ambos valores complejos en la forma valor real + valor imaginario,
por ejemplo: 3.21 + -1.8i
Tu programa además deberá contemplar cualquier situación excepcional
evitando los cuelgues por razones detectables: divisiones por 0, raíces de
números negativos, etc. 
resolvente:  −b ± √b2−4*ac
                 2*a
En el caso de raíces complejas: −b ± √−(b2−4*ac)i
                                2*a     2*a
'''
print("")
print("******************************************************************")
print("* Programa para resolver ecuaciones cuadráticas de segundo grado *")
print("******************************************************************")
print("")

coefA = float(input("Ingrese el coeficiente a: "))
if coefA !=0:
    coefB = float(input("Ahora ingrese el coeficiente b: "))
    coefC = float(input("Y por ultimo ingrese el coeficiente c: "))
    determinante = coefB**2 - 4*coefA * coefC
    if determinante > 0:
        raiz1 = (- coefB - determinante ** 0.5) / (2*coefA)
        raiz2 = (- coefB + determinante ** 0.5) / (2*coefA)
        print(f"Las raices de la ecuacion son:\n*Raiz 1= {raiz1} \n*Raiz 2: {raiz2}")
    elif determinante == 0:
        raizUnica = -coefB / (2*coefA)
        print(f"La raiz Unica de la ecuacion es: {raizUnica}")
    else:
        raizR = -coefB / (2*coefA)
        raizI = (-determinante ** 0.5) / (2*coefA)
        print(f"La raiz Real es:\n*Raiz real:{raizR} \n*Raiz I:{raizI}")
print("******************************************************************")        