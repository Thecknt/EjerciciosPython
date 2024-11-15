#Crea una tupla que almacene las coordenadas de tres puntos en un plano. Calcula la distancia entre el primero y el segundo punto.

import math

coordenadas = ((2, 5), (3, 6), (5, 8))
# La fórmula de la distancia euclidiana
# Extraer los puntos
p1 = coordenadas[0]  # Primer punto (2, 5)
p2 = coordenadas[1]  # Segundo punto (3, 6)



# Calcular la distancia usando la fórmula
distancia = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

print(f"La distancia entre {p1} y {p2} es {distancia:.2f}")