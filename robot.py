import roboticstoolbox as rtb
import numpy as np

print(f"versión de RTB: {rtb.__version__}")
print(f"versión de NumPy: {np.__version__}")

robot = rtb.models.DH.Puma560()
q=[0, 0, 0, 0, 0, 0]

robot.plot(q, block=True, backend='pyplot')