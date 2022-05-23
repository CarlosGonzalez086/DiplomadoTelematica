##La distriubcion de gaus o normal
#Ejemplo si se rellenar una jarra de agua que contiene 1 litro y a otras se les da mas o menos de la cantidad cuales
#el promedio o la media de todas que se sirve
import random
import matplotlib.pyplot as plt

r = random.gauss(990, 73.10)
print('La distribucion de Gaus:', r)
plt.figure(figsize=(9, 6))
plt.hist([random.gauss(990, 73.10) for i in range(998)], bins = 1100)
plt.show()