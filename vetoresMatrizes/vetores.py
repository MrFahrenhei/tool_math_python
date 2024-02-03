import numpy as np
# dados os vetores u=(3, -5, 2) e v=(4,6,3), calcule u.v e uXv
u = np.array([[3,-5,2]])
v=np.array([[4,6,3]])
uv=np.inner(u,v)
uXv=np.cross(u,v)
print(uv)
print(uXv)