import random
from random import choice

Raton = random.choice(['Norte', 'Noroeste', 'Noreste', 'Sur', 'Suroeste', 'Sureste', 'Oeste', 'Este'])
print(Raton)

Direccion = random.choice(['Norte','Noroeste', 'Noreste', 'Sur', 'Suroeste', 'Sureste', 'Oeste', 'Este'])
print(Direccion)


if Raton == Direccion:
    X = Direccion
    print('EL raton esta en:', X)
else:
    print('El raton esta en otra direccion:', Raton)


