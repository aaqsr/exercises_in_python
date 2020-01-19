import numpy as np

a = eval(input("input... ")) # figures out which variable type works and assigns it to a (like int, list, float etc)[not string] 

distance = float(input("Input trip distance (miles): "))
100
time = distance/60
gallons = distance/30
cost = gallons*2.85
# how to format print statements better
print("\nDuration of trip = {0:0.1f} hours".format(time)) 
print("Gasoline used = {0:0.1f} gallons (@ {1:0.0f} mpg)".format(gallons, 30))
print("Cost of gasoline = ${0:0.2f} (@ ${1:0.2f}/gallon)".format(cost, 2.85))
 
# \n is new line, \a is warning sound, \b is backspace?
# the {} tells .format where to put stuff 
# number before : tells which variable in the list in the format function is printed
# number after : is minimum amount of spaces reserved for the number, (0 means only as many as required)
# number after the period specifies the number of digits to the right of the decimal point
# leaving the {} empty, they will autofill with the first then the second then the third etc

# f specifies that a number is to be printed with a fixed number of digits, e would make it sci notation, d for integers, s for strings
# read more of it at http://docs.python.org/library/string.html#formatspec

# we can also just simply 
print('Duration = ' + str(time))
# but this will not round off the output and present it in a nice way

print(2*'J. {0:8.3f} '.format(1.2349))

print('L. {0:12.3e}'.format(10.239)) # 12 spaces, 3 decimals

# Numpy Arrays

a = np.linspace(3, 19, 7)
print(a)

np.set_printoptions(precision=4)
print(a)

# for scientific notation we can use a lambda func to format it
np.set_printoptions(formatter={'float': lambda x: format(x, '5.1e')}) # prints in exp sci notation
print(a)

np.set_printoptions(formatter={'float': lambda x: format(x, '6.3f')}) # prints with 3 decimal places
print(a)

#default output format
np.set_printoptions(precision=8)
print(a)



## file I/O


# python funcs

# internal func for files. w means write. w+ means create the file if it doesnt exist
f = open("guru99.txt","w+")
f.write("So guys \n we did it")
# does not work if the file hasn't been opened and only writes to the file once it has been closed
f.close()

f = open("guru99.txt","a") # the a means it'll append the data
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
f.close()

#to read from a file we do
f=open("guru99.txt", "r") # r means to read
#to check if file is being read, we can use the mode func

if f.mode == 'r':
    contents =f.read()

print(contents)

# 'r'	This is the default mode. It Opens file for reading.
# 'w'	This Mode Opens file for writing.
# If file does not exist, it creates a new file.
# If file exists it truncates the file.
# 'x'	Creates a new file. If file already exists, the operation fails.
# 'a'	Open file in append mode.
# If file does not exist, it creates a new file.
# 't'	This is the default mode. It opens in text mode.
# 'b'	This opens in binary mode.
# '+'	This will open a file for reading and writing (updating)

cont = f.readlines()
print(cont)
print(cont[0] + cont[3])

# NUMPY

np.loadtxt( "fallexampledata.txt", skiprows=5) 
# skips the first few rows and starts reading till the end storing each line in a row of the array

np.loadtxt("fallexampledata.txt", skiprows=5, unpack=True)
# the unpack tag stores each column in a row of the array

dataPt, time, height, error = np.loadtxt( "fallexampledata.txt", skiprows=5 , unpack=True)
# this just cuts up the array into these variables

# loadtxt works ONLY with simple, well formatted files 

np.loadtxt("fallexampledata.txt", skiprows=5, unpack=True, usecols=(0,2))
# only selects columns 0 and 2, skipping 1 and 3

# we can also save .xlsx (excel) files as .csv files using excel and then read them in
np.loadtxt("testdata.csv", skiprows=1, delimiter=',$')

# the delimiter tag makes it so that numpy knows that the columns are separated by what is in the " " and not whitespace

# we can write data to a file via 
# savetxt(filename, array, fmt="%0.18e", delimiter=" ", newline=" \n", header="", footer="", comments="#")

np.savetxt("mydatawritten.txt",list(zip(dataPt, time, height, error)),fmt="%12.1f")
# WARNING THIS OVERWRITES FILES BE CAREFUL

# btw zip combines the four arrays and returns a list of tuples, where the ith tuple contains the ith element from each of the arrays

np.savetxt('mydatawritten.txt', list(zip(dataPt, time, height, error)), header="data time height error",comments="", fmt="%12.1f")
# header puts a bunch of text above the arrays, and the comments tag puts something before any line in the header, 
# default is a #

dataPt, time, height, error = np.loadtxt("fallexampledata.txt", skiprows=5,unpack=True)
info = 'Data for falling mass experiment'
info += '\nDate: 16-Aug-2016'
info += '\nData taken by Lauren and John'
info += '\n\n data point time (sec) height (mm) ' 
info += 'uncertainty (mm)'
np.savetxt('ReadWriteMyDataHeader.txt', list(zip(dataPt, time, height, error)),header=info, fmt="%12.1f")