import numpy as np

v0 = 10
a = 2.5
z = 4 * (1/3)

v = v0 * (1 - ((z) / (np.sqrt(a**2 + z**2))))
print(v)

z = 8 * (2/3)
v = v0 * (1 - ((z) / (np.sqrt(a**2 + z**2))))
print(v)

z = 13
v = v0 * (1 - ((z) / (np.sqrt(a**2 + z**2))))
print(v)