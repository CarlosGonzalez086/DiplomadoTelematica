import math
print('Introduce el valor de A:')
a=input()
print('Introduce el valor de B:')
b=input()
print('Introduce el valor de C:')
c=input()

s=((int(a)+int(b)+int(c))*(.5))
print('el semiperimetro es:')
print(str(s))

x=((s)-int(a))*((s)-int(b))*((s)-int(c))
y=(s)*(x)
w=math.sqrt(y)
r=(w)/(s)
print('la circunferencia inscrita en el triangulo es:')
print(str(r)) 
