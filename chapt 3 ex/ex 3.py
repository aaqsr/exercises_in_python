import numpy as np

g = 9.8

try:
    h = float(input("Initial height... "))
except:
    print("Numbers only pls")
    

y = np.arange(h, 0, -0.5)

t = np.sqrt( (-2*(y - h))/g )
print(t)

list(zip(t, y))[::-1]
# it makes a list of tuples with the t and its corresponding y values
# the [::-1] flips the order for aesthetic reasons