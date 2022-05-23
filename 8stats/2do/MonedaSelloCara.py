import operator
import random
def resultado():
    return (random.choice([1, 2])) % 2

cara = 0
sello = 0
moneda = input('Cuantos lanzamientos quieres: ')
for i in range(0, int(moneda)):
    if resultado() == 0:
        cara = operator.add(cara, 1)

    else:
        sello = operator.add(sello, 1)

print('La veces de cara fueron: ', cara)
print('Las veces de sello fueron', sello)







