import numpy as np
import matplotlib.pyplot as plt

a = [1, 2, 3, 2, 3, 4, 3, 4, 5]
plt.plot(a)
plt.show()

# used to plot x-y data sets and is written like this
# plot(x, y)
# x,y are which arrays (or lists) must have the same size

# if x array is omitted then it just uses a simple x = [0,1,2...N-1] where N is the number of elements in y

'''Sine wave'''

x = np.linspace(0,4*np.pi, 129)
y = np.sin(x)   
plt.plot(x,y)
plt.show()

'''Test''' 
x = np.linspace(-2*np.pi,2*np.pi, 129)
y = np.sin(x)
plt.plot(x,y,'b-', label='Theory' )

xdata, ydata = np.loadtxt('sin.csv', unpack=True, skiprows=1, delimiter=',') # take input from file
plt.plot(xdata, ydata, 'go', label="Data")  # plots the data from file; the g is for green, o is for circle

plt.axhline(color='gray', zorder=-1)
plt.axvline(color='gray', zorder=-1)
plt.show()  

