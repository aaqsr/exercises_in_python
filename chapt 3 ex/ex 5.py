import numpy as np

# a
a = np.ones((8,8))
a[1:-1,1:-1] = 0
print(a)

# b 
b = np.ones((8,8))
b[::2,::2] = 0
b[1::2,1::2] = 0
print(b)

#c
c = np.arange(2, 50, 5)
c[c%3 > 0] = c[c%3 > 0] * -1
print(c)

#d
print(a.size)
print(a.shape)
print(a.mean())
print(a.std())

print(b.size)
print(b.shape)
print(b.mean())
print(b.std())

print(c.size)
print(c.shape)
print(c.mean())
print(c.std())