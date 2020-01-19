import numpy as np

# uses a bit from ex 3
h0 = 10
g = 9.8
y = np.arange(h0, 0, -0.5)
t = np.sqrt( (2*(h0 - y))/g )

# y[1:20] # the elements of y from the second one to the last
# y[0:19] # the elements of y from the first one to second last
# y[1:20]-y[0:19] # this represents the values of Δy 

# the more elegant way to do this is to do this
# y[1:]  # the elements of y from the second one          
# y[:-1] # the elements of y till second last

d_y = y[1:] - y[:-1] 
d_t = t[1:] - t[:-1]

v = d_y / d_t
print(v)

# bonus:
d_v = v[1:] - v[:-1]
d2_t = (d_t[1:] + d_t[:-1])/2

a = d_v/d2_t
print(a)
# justified as since the ball is falling the only acceleration on it is the constant
# downward decceleration of the gravitational field strength we set at 9.8m/s/s 