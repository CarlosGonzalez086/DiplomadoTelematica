#Tarea Graficar los puntos del 0 al 10 con incrementos en 0.10
#Jose Carlos Gonzalez Ramirez

import matplotlib.pyplot as plp
import numpy as np

X = np.arange(0, 10, .10)
Y = X * 3

print("Puntos X:", X)
print("Puntos Y:", Y)

plp.plot(X,Y)
plp.show()

