import numpy as np
a = np.array([1, 3, 5, 7]); b = np.array([8, 7, 5, 4]); c = np.array([0, 9,-6,-8])

d = list(zip(a,b,c)); print(d) 
# d's elements are tuples
e = np.array(d); print(e) 
print(e[3,2]) # to get the value of -8
print(d[3][2]) # to get value of -8
# e[1] is a numpy array