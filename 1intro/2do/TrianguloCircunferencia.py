import math
a = int(input('Introduce el valor de A:'))
b = int(input('Introduce el valor de B:'))
c = int(input('Introduce el valor de C:'))

s = ((int(a)+int(b)+int(c))*(.5))
print('el semiperimetro es:', s)

x = ((s)-int(a))*((s)-int(b))*((s)-int(c))
print(x)
y = s*x
print(y)
w = math.sqrt(y)
print(w)
r = w/s
print('la circunferencia inscrita en el triangulo es:', r)
