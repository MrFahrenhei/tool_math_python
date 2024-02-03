import numpy as np

# resolva o sistema linear 4x+2y-z=7, 3x+3y+2z=20, 5y+2z=-1
A = np.array([[4, 2, -1], [3, 3, 2], [0, 5, 2]])
b = np.array([[7], [20], [-1]])
x = np.linalg.solve(A, b)
print(x)
# resolva o sistema linear: x+3y+4z=18, 2x-y+z=10, -4y+2y-2z=-7
C = np.array([[1, 3, 4], [2, -1, 1], [-4, 2, -2]])
d = np.array([[18], [10], [-7]])
x = np.linalg.solve(C, d)
print(x)
