import numpy as np
try:
    eq = input("Input quadratic with no spaces with all coefficients including 1 like 1x^2:  0 = ").replace("x^2"," ").replace("x"," ").replace("+", " ").replace("-", " -") 
    # gets user input and removes x^2, x, -, and +
    a, b, c = eq.split() 
    #splits the values into variables
    na, nb, nc = float(a), float(b), float(c)
    #converts them to a float (variable name changed for clarity)
    na = na + 0j
    nb = nb + 0j
    nc = nc + 0j
    #converts them to complex so that it can output complex roots
except: 
    #incase of invalid input
    print("invalid input, please input again in the form ax^2+bx+c with no spaces, or type a b c with spaces in between")
    input("Press enter to end")
    exit()

#try: I disabled error check cause it was unnecessary as python just outputs infinity in case of a = 0

x1 = (-nb + np.sqrt(nb**2 - 4*na*nc)/(2*na))  
#equation for x1
x2 = (-nb - np.sqrt(nb**2 - 4*na*nc)/(2*na))  
#equation for x2

#except:
 #   print("calc error (likely divided a = 0)")
  #  exit()

if (x1 == x2):
    print(x1)
else:
    print(x1, x2)    
# not really useful, just tidies up the output