# Tarea Derivacion numerica
# Resuelve la siguiente derivada con al menos 3 metodos
# Si f(x) = (sen^3)(2x)/x^4+1 obtener f'(2.45) Respuesta =0.0698503
# Diferencias finitas centradas

from math import sin, exp

print("Diferencias finitas centradas")
def fn(x):
    return (pow(sin(2*x), 3)) / (pow(x, 4) + 1)


x0 = 2.45

h1 = 0.5
r1 = (fn(x0 + h1) - fn(x0 - h1)) / (2 * h1)
print('Resultado 1=', r1)

h2=0.3
r2=(fn(x0+h2)-fn(x0-h2))/(2*h2)
print('Resultado 2=',r2)

h3=0.1
r3=(fn(x0+h3)-fn(x0-h3))/(2*h3)
print('Resultado 3=',r3)

h4=0.00001
r4=(fn(x0+h4)-fn(x0-h4))/(2*h4)
print('Resultado 4=',r4)

h5=0.00000001
r5=(fn(x0+h5)-fn(x0-h5))/(2*h5)
print('Resultado 5=',r5)

print("########################")
print("Diferencias finitas progresivas")

h1=0.5
r1=(fn(x0+h1)-fn(x0))/h1
print('Resultado 1=', r1)

h2=0.3
r2=(fn(x0+h2)-fn(x0))/h2
print('Resultado 2=', r2)

h3=0.1
r3=(fn(x0+h3)-fn(x0))/h3
print('Resultado 3=', r3)

h4=0.00001
r4=(fn(x0+h4)-fn(x0))/h4
print('Resultado 4=', r4)

h5=0.00000001
r5=(fn(x0+h5)-fn(x0))/h5
print('Resultado 5=', r5)

h6=0.0000000001
r6=(fn(x0+h6)-fn(x0))/h6
print('Resultado 6=', r6)

print("#################")
print("Derivada de primer orden")

h1=0.5
r1=(fn(x0+h1/2)-fn(x0-h1/2))/h1
print('Resultado 1=', r1)

h2=0.3
r2=(fn(x0+h2/2)-fn(x0-h2/2))/h2
print('Resultado 2=', r2)

h3=0.001
r3=(fn(x0+h3/2)-fn(x0-h3/2))/h3
print('Resultado 3=', r3)

h4=0.000001
r4=(fn(x0+h4/2)-fn(x0-h4/2))/h4
print('Resultado 4=', r4)

h5=0.000000001
r5=(fn(x0+h5/2)-fn(x0-h5/2))/h5
print('Resultado 5=', r5)



