import numpy as np

# resolva o sistema:
# (2+j)a+(5-j)b=3+8j
# (5-j)a+(7+4j)b=2+5j
A = np.array([
    [complex(2, 1), complex(5, -1)],
    [complex(5, -1), complex(7, 4)],
])
b = np.array([
    [complex(3, 8)],
    [complex(2, 5)],
])
print(np.linalg.solve(A, b))

# resolva o sistema:
# (3+2j)a+(-2-6j)b=70 < 0º
# (-2-6j)a+(10+j)b=110 < 30º
C = np.array([
    [complex(3,2),complex(-2,-6)],
    [complex(-2,-6), complex(10, 1)]
])
x1=np.cos(np.deg2rad(0))
y1=np.sin(np.deg2rad(0))
x2=np.cos(np.deg2rad(30))
y2=np.sin(np.deg2rad(30))
d = np.array([
    [70*complex(x1,y1)],
    [110*complex(x2, y2)]
])
print(np.linalg.solve(C, d))