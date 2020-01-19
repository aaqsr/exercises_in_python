import numpy as np 

f, a, da = np.loadtxt(
    'chapt 4 ex/ex3data.txt',
     unpack=True, 
     skiprows=3
     ) # to read from file


info = 'Date: 2013-09-16\nData taken by Liam and Selena\nfrequency (Hz) amplitude (mm) amp error (mm)'
np.savetxt('ex4data.txt', 
            list(zip(f, a, da)),
            header=info,
            fmt="%12.4f",
            comments=''
            ) # to write the file