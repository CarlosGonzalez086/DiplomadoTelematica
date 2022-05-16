#Tarea Tema 4 :Resolver usando uno de los  metodos a elegir y obtener la raiz
#e^(2-x)-7x=0
#Jose Carlos Gonzalez Ramirez

import matplotlib.pyplot as plp
from math import exp

#La funcion original
def fn1(x):
    return exp(2-x) - 7*x

#La funcion derivada
def fn2(x):
    return -exp(2-x) -7

#Primer punto
x0 = 1.5

#Segundo punto
x1 = x0 - (fn1(x0) / fn2(x0))

print('El segundo punto es:', x1)

#Tercer punto
x2 = x1 -(fn1(x1) / fn2(x1))

print('El tercer punto es:', x2)

#Cuarto punto
x3 = x2 - (fn1(x2) / fn2(x2))

print('El cuarto punto es:', x3)
print('El Valor es:', fn1(x3))
print('La Raiz es:', x3)

#Los puntos de la funcion original
x = [-2, -1, 0, 1, 2]
y = [68.59815, 27.085537, 7.38056, -4.281718, -13]

plp.plot(x, y)
plp.show()

#Los puntos de la funcion derivada
y1 = [-61.59815, -27.085537, -14.389056, -9.718282, -8]

plp.plot(x, y1)
plp.show()



