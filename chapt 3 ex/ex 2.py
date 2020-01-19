import numpy as np

# a  
a = np.ones(100) * np.e
print(a)

# b 
b = np.arange(0,361,1)
print(b)

# c
c = np.arange(0,361,1)
c = np.radians(c)
print(c)

check = c - b * np.pi/180
check[np.abs(check) < 1e-15] = 0
print(check)

# d
np.arange(12,17,0.2)

# e
np.arange(12,17.2,0.2)