#Dados: (-2, 4),(-1, -2), (3, 5) y (4.3, 11) estimar el valor de y cuando x = 7.7 Larange

p1 = (-2, 4)
p2 = (-1, -2)
p3 = (3, 5)
p4 = (4.3, 11)
x = 7.7


def fn(x, p1, p2, p3, p4):
    a = ((x - p2[0]) / (p1[0] - p2[0]))
    b = ((x - p3[0]) / (p1[0] - p3[0]))
    c = ((x - p4[0]) / (p1[0] - p4[0]))
    d = a * b * c * p1[1]
    return d


print("Valor de FN1:", fn(x, p1, p2, p3, p4))

def fn1(x, p1, p2, p3, p4):
    a = ((x - p1[0]) / (p2[0] - p1[0]))
    b = ((x - p3[0]) / (p2[0] - p3[0]))
    c = ((x - p4[0]) / (p2[0] - p4[0]))
    d = a * b * c * p2[1]
    return d


print("Valor de FN1:", fn1(x, p1, p2, p3, p4))


def fn2(x, p1, p2, p3, p4):
    a = ((x - p1[0]) / (p3[0] - p1[0]))
    b = ((x - p2[0]) / (p3[0] - p2[0]))
    c = ((x - p4[0]) / (p3[0] - p4[0]))
    d = a * b * c * p3[1]
    return d


print("Valor de FN2:", fn2(x, p1, p2, p3, p4))


def fn3(x, p1, p2, p3, p4):
    a = ((x - p1[0]) / (p4[0] - p1[0]))
    b = ((x - p2[0]) / (p4[0] - p2[0]))
    c = ((x - p3[0]) / (p4[0] - p3[0]))
    d = a * b * c * p4[1]
    return d


print("Valor de FN3:", fn1(x, p1, p2, p3, p4))


def fn4(x, p1, p2, p3, p4):
    return fn(x, p1, p2, p3, p4) + fn1(x, p1, p2, p3, p4) + fn2(x, p1, p2, p3, p4) + fn3(x, p1, p2, p3, p4)


print("El valor de Y= ", fn4(x, p1, p2, p3, p4))
