#Dados (-1,3), (0,-7), (4,7), (5,11)
#Estimar el polinomio interpolante

p1 = (-1, 3)
p2 = (0, -7)
p3 = (4, 7)
p4 = (5, 11)
x=0


def fn1(p1, p2, p3, p4):
    A: float = ((p1[0]) * (p1[0] - p3[0]) * (p1[0] - p4[0]))
    B: float = p1[1] / A
    C: float = (p3[0]) * (p4[0])
    D: float = B * C
    return D


print(fn1(p1, p2, p3, p4), 'x3')


def fn2(p1, p2, p3, p4):
    A: float = ((p1[0]) * (p3[0]) * (p4[0]))
    B: float = p2[1] / A
    C: float = (p1[0]) * (p3[0]) * (p4[0])
    D: float = B * C
    return D


print(fn2(p1, p2, p3, p4), 'x2')


def fn3(p1, p2, p3, p4):
    A: float = ((p3[0] - p1[0]) * (p3[0]) * (p3[0] - p4[0]))
    B: float = p3[1] / A
    C: float = (p1[0])  * (p4[0])
    D: float = B * C
    return C


print(fn3(p1, p2, p3, p4), 'x')


def fn4(p1, p2, p3, p4):
    A: float = ((p4[0] - p1[0]) * (p4[0]) * (p4[0] - p3[0]))
    B: float = p4[1] / A
    C: float = (p1[0]) * (p3[0])
    D: float = B * C
    return C


print(fn4(p1, p2, p3, p4))