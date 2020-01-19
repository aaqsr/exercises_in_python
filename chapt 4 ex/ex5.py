import numpy as np

f, a, da = np.loadtxt(
    'chapt 4 ex/ex3data.txt',
     unpack=True, 
     skiprows=3
     ) # to read from file


np.savetxt(
    'ex5data.csv', list(zip(f, a, da)),
    delimiter=',', 
    fmt="%0.16e", 
    comments=''
    ) # to write the file
