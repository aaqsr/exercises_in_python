import numpy as np

a = (2 + np.e**2.8) / (np.sqrt(13) - 2)

b = ( 1 - ( 1 + np.log(2) )**-3.5 ) / ( 1 + np.sqrt(5) )

c = np.sin( (2 - np.sqrt(2) ) / (2 + np.sqrt(2) ))

while True:
    i = input("which one? (anything other than a,b,c to break)")
    if (i == "a"):
        print(a)
    elif (i == "b"):
        print(b)
    elif (i == "c"):
        print(c)
    else:
        exit()