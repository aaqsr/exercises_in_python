# the code they gave:

n = int(input("Input an integer > 1: ")) 

i=2
while (n % i) != 0:
    i += 1

print("The smallest factor of {0:d} is {1:d}".format(n, i))

'''
    How it works
Computer asks for user input of a number above 1 and stores it in n
i is set to 2
Then a while loop runs that executes whilst n is not fully divisible by i (ie. it leaves remainder so its modulus is not 0)
The loop adds 1 to i, iterating until i divides n with no remainder left 
This will be the smallest factor of n as it fully divides n and also is the first pos integer to do so 
Loop will then terminate and output i
This will always happen as, by the Fundamental Theorem of Arithmetic, there must be some integer that fully divides n
'''

# modification to make it detect primes

print("Is it prime?: {}".format(i==n))

# program already prints out smallest prime factor 
