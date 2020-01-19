import numpy as np

try:
    eq = input("Input quadratic with no spaces with all coefficients including 1 like 1x^2:  0 = "
               ).replace("x^2"," ").replace("x"," ").replace("+", " ").replace("-", " -") 
    # gets user input and removes x^2, x, -, and +
    a, b, c = eq.split() 
    #splits the values into variables
    na, nb, nc = float(a), float(b), float(c)
    #converts them to a float (variable name changed for clarity)
except: 
    #incase of invalid input
    print("invalid input, please input again in the form ax^2+bx+c with no spaces, or type a b c with spaces in between")
    input("Press enter to end")
    exit()

d = nb**2 - 4.*na*nc  

if (d > 0):
    print('Two distinct real roots')
elif (d == 0):
    print("Two equal real roots")
else:
    print("Complex roots")