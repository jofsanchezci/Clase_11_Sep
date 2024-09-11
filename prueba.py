import numpy as np
from math import sin
import time
x=[]
y=[]
c=-6
while c<=6:
	x.append(c)
	c+=0.01

print(x)
print('El tamaño de la lista es: ', len(x))
print('------------------------------')
inicio=time.time()
for i in x:
	y.append(sin(i))
fin=time.time()
tiempo=fin-inicio
print(y)
print('El tiempo de ejecución fue: ',tiempo)