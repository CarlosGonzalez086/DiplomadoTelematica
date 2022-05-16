p1 = (2, 1.43)
p3 = (3.2, 2.79)
p2 = (4, 3.56)

def fn(p1, p3):
    a = (p3[1] - p1[1]) / (p3[0] - p1[0])
    return a
print(fn(p1, p3))

def fn1(p2, p3):
    b = (p2[1] - p3[1]) / (p2[0] - p3[0])
    c = b - fn(p1, p3)
    d = c / (p2[0] - p1[0])
    return d
print(fn1(p2, p3))

def fn2(p1, p2):
    y = (p1[1] + fn(p1, p3) * (3.6 - p1[0]))
    x = (fn1(p2, p3)*((3.6 - p1[0])*(3.6 - p2[0])))
    w = y + x
    return w
print(fn2(p1, p2))
