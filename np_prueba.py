import numpy as np
import time
x=np.arange(-6,6,0.01)
print(x)
print('Tamaño de la lista: ',len(x))
print('------------------------------')
inicio=time.time()
y=np.sin(x)
fin=time.time()
print(y)
tiempo=fin-inicio
print('Tiempo de ejecución',tiempo )


