numero_mesas = 31

suma = 1+14+3+48+63+29+31+53

suma_cuadrado = 14724 + 6738 + 187 + 11090 + 3638

varianza = suma_cuadrado/numero_mesas-(suma/numero_mesas)**2

print(f'la varianza es: {varianza}')

import numpy as np

data1 = np.array([1,3,14,48,63,29,31,53,7,21,42,30,22,28,73,32,17,37,77,0,10,20,35,60,33,18,3,5,12,3,0])

print(np.var(data1), np.mean(data1))

print((np.sum(data1**2))/len(data1)-(np.sum(data1)/len(data1))**2)


