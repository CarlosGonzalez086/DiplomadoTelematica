#la estatura promedio de los hombres en mexico es 170cm
import numpy as np

import matplotlib.pyplot as plt

MeanValor = 170
ModeValor = np.sqrt(2/np.pi) * MeanValor
Solucion = np.random.rayleigh(ModeValor,1000000)
Resultado = 100.*sum(Solucion > 180)/1000000.
print('El porcentaje que supera la estatura media es: ', Resultado)
plt.figure(figsize=(9, 6))
plt.hist([np.random.rayleigh(180, 1000000)], bins=200, density=True)
plt.show()






