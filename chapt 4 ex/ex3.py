import numpy as np
""" f = [0.75,1.7885,2.8269,3.8654,4.9038,5.9423,6.9808,8.0192,9.0577,10.0962,11.1346,12.1731,13.2115,14.25]
a = [13.52,12.11,14.27,16.6,22.91,35.28,60.99,33.38,17.78,10.99,7.47,6.72,4.4,4.07]
da = [0.32,0.92,0.73,2.06,1.75,0.91,0.99,0.36,2.32,0.21,0.48,0.51,0.58,0.63]
info = 'Date: 2013-09-16\nData taken by Liam and Selena\nfrequency (Hz) amplitude (mm) amp error (mm)'
np.savetxt('ex3data.txt', list(zip(f, a, da)),header=info, fmt="%12.4f", comments='') """ # to generate the text file

f, a, da = np.loadtxt('chapt 4 ex/ex3data.txt', unpack=True, skiprows=3) # to read from it
np.set_printoptions(formatter={'float': lambda x: format(x, '5')})       # to get the proper format
print(f)