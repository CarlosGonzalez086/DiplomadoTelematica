from statistics import mean, median, median_high, median_low, mode, variance
def Edades():
    Edades = [9,6,7,8,6,8,6,8,9,10,8,7,8,9,6,8,8,8,12,14,15,21,8,13,17,17,18,19]
    return Edades

def Mediana():
    Mediana = median(Edades())
    return Mediana
def avg():
    Promedio = mean(Edades())
    return Promedio

def min():
    MediaBaja = median_low(Edades())
    return MediaBaja

def max():
    MediaAlta = median_high(Edades())
    return MediaAlta

def Variance():
    Varianza = variance(Edades())
    return Varianza

def Moda():
    Moda = mode(Edades())
    return Moda

print('Mediana: ', Mediana())
print('Promedio: ', avg())
print('Media Baja: ', min())
print('Media Alta: ', max())
print('Varianza: ', Variance())
print('Moda: ', Moda())


