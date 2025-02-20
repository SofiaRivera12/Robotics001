import numpy as np
import matplotlib.pyplot as plt
from spatialmath import *
from spatialmath.base import *
from math import pi

#Referencia T0
T0= rotz(0, unit='deg')
trplot(T0, dims=[-1, 1, -1, 1, -1, 1], color='k') #dibujar

#sistema de coordenadas rotado (TA)
TA= rotz(90, unit='deg')
trplot(TA, dims=[-1, 1, -1, 1, -1, 1], color='g') #dibujar

#definir el punto p con respecto a T0
p= np.array([1, 1, 0])
ax=plt.gca()
ax.scatter(p[0], p[1], p[2], color='r', label='p')

#configurar plot
plt.gca().view_init(elev=25, azim=44) #perspectiva

#mostrar la trama
plt.show()
