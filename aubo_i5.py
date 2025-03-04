import sympy as sp
from sympy.matrices import rot_axis3

#matriz DH
from spatialmath import *
from spatialmath.base import *
#para graficar
import matplotlib.pyplot as plt
import numpy as np
#para usar el DH
import roboticstoolbox as rtb

#toolbox
robot = rtb.DHRobot(
    [
        rtb.RevoluteDH(d=0.0985, a=0, alpha=np.deg2rad(-90), offset=0, qlim=[np.deg2rad(-175), np.deg2rad(175)]),
        rtb.RevoluteDH(d=0.1405, a=0.408, alpha=np.deg2rad(180), offset=np.deg2rad(-90), qlim=[np.deg2rad(-175), np.deg2rad(175)]),
        rtb.RevoluteDH(d=0.1215, a=0.376, alpha=np.deg2rad(-180), offset=0, qlim=[np.deg2rad(-175), np.deg2rad(175)]),
        rtb.RevoluteDH(d=0.1025, a=0, alpha=np.deg2rad(-90), offset=np.deg2rad(-90), qlim=[np.deg2rad(-175), np.deg2rad(175)]),
        rtb.RevoluteDH(d=0.1025, a=0, alpha=np.deg2rad(90), offset=0, qlim=[np.deg2rad(-175), np.deg2rad(175)]),
        rtb.RevoluteDH(d=0.094, a=0, alpha=0, offset=0, qlim=[np.deg2rad(-175), np.deg2rad(175)])
    ],
    name="Aubo i5", base=SE3(0, 0, 0)
)
print(robot)


#para modificar ángulos
joint1= np.deg2rad(0)
joint2= np.deg2rad(0) 
joint3= np.deg2rad(0)
joint4= np.deg2rad(0)
joint5= np.deg2rad(0)
joint6= np.deg2rad(0)


q=np.array([joint1, joint2, joint3, joint4, joint5, joint6])
robot.teach(q)
