import simpy as sp
from simpy.matrices import rot_axis3
#para poder graficar
import matplotlib.pyplot as plt
import numpy as np
#para generar la matriz dh
from spatialmath import *
from spatialmath.base import *

#definir los símbolos
theta, d, a, alpha= sp.symbols('theta, d, a, alpha')

#matriz RzTzTxRx
TDH= trotz(theta) @ transl(0, 0, d) @ transl(a, 0, 0) @ trotx(alpha)
sp.pprint(TDH)
print(type(TDH))

#declarandola explicitamente
T= sp.Matrix([[sp.cos(theta), -sp.sin(theta)*sp.cos(alpha), sp.sin(theta)*sp.sin(alpha), a*sp.cos(theta)],
                [sp.sin(theta), sp.cos(theta)*sp.cos(alpha), -sp.cos(theta)*sp.sin(alpha), a*sp.sin(theta)],
                [0, sp.sin(alpha), sp.cos(alpha), d],
                [0, 0, 0, 1]])

sp.pprint(T)
print(type(T))
