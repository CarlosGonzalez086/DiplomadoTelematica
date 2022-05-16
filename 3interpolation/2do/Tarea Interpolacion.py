#Tarea 1 dados (-4,-2) y (1,5) estimar el valor para x cuando y = 3.7
p1 = (-4, -2)
p2 = (1, 5)


def fn(p1, p2):
    a = (3.7-p1[1]) * (p2[0]-p1[0])
    return a
print(fn(p1, p2))

def fn2(p1, p2):
    b = ((p2[1])-(p1[1]))
    return b
print(fn2(p1,p2))

def fn3(p1):
    c = p1[0] + (fn(p1,p2)/fn2(p1,p2))
    return c
print(fn3(p1))

