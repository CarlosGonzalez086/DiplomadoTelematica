#Dados: (-2, 4),(-1, -2), (3, 5) y (4.3, 11) estimar el valor de y cuando x = 7.7

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
    a1 = ((x - p1[0]) / (p2[0] - p1[0]))
    b1 = ((x - p3[0]) / (p2[0] - p3[0]))
    c1 = ((x - p4[0]) / (p2[0] - p4[0]))
    d1 = a1 * b1 * c1 * p2[1]
    return d1


print("Valor de FN1:", fn1(x, p1, p2, p3, p4))


def fn2(x, p1, p2, p3, p4):
    a2 = ((x - p1[0]) / (p3[0] - p1[0]))
    b2 = ((x - p2[0]) / (p3[0] - p2[0]))
    c2 = ((x - p4[0]) / (p3[0] - p4[0]))
    d2 = a2 * b2 * c2 * p3[1]
    return d2


print("Valor de FN2:", fn2(x, p1, p2, p3, p4))


def fn3(x, p1, p2, p3, p4):
    a3 = ((x - p1[0]) / (p4[0] - p1[0]))
    b3 = ((x - p2[0]) / (p4[0] - p2[0]))
    c3 = ((x - p3[0]) / (p4[0] - p3[0]))
    d3 = a3 * b3 * c3 * p4[1]
    return d3


print("Valor de FN3:", fn1(x, p1, p2, p3, p4))


def fn4(x, p1, p2, p3, p4):
    return fn(x, p1, p2, p3, p4) + fn1(x, p1, p2, p3, p4) + fn2(x, p1, p2, p3, p4) + fn3(x, p1, p2, p3, p4)


print("El valor de Y= ", fn4(x, p1, p2, p3, p4))
