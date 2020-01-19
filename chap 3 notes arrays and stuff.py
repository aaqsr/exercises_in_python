a = ["hello",3,"wee",2.95,3+4j,6,"ok",13]
b = ["0:first", "1:second", "2:third", "3:fourth", "4:fifth", "5:sixth"]
c = list(range(0,10))
c
print(a[0])
#lists are indexed starting from 0, so this will print "hello"
print(b[-1])
print(a[-2])
#lists can also be accessed the other wway around via negative numbers, so -1 is the last element and -2 is the second last element

a[1] = a[1] + 3
#elements of lists can be used as variables in calcs, so this will add 3 to the second element of a and override it with that value

print(a + a)
#adding lists does not add their members, it just appends the elements of the second list to the first one

b[2:5]
#will select from the third element to the 5th element 

b[3:]
#will select all of the elements from the 4th one till the end

b[:3]
#will select from the first to the third element

b[:]
#will select all

b[1:-1]
#will select from the second to the second last element and is equivalent to:
b[1:5]

b[0::2]
#will select every second element

b[1::2]
#will select every second element from the second element
range(10) # range(0, 10) function returns an iterable sequence from 0 to 9
# only information stored in the range function is the current value of the sequence, the ending value, and the increment. By contrast, a list stores all the numbers in the list
# they useful with for loops 
list(range(10)) # converts range to a list and makes list of 10 integers from 0 to 9
list(range(3, 10)) # makes a list of integers from 3 to 9
list(range(0, 10, 2)) # makes a list of 10 # integers from 0 to 9 with an increment of 2
list(range(5,6,-1)) # not possible, makes an empty list
list(range(5,0,-1))

d = (0, 1, 2, 4, 5)
#this is tuple, it is like list but it does not support reassignment of variables

d[3]
#selects the 4th element of the tuple 

#d[3] = 3
#gives an error because tuples do not support item assignment

e = [[1,2], [3,4], [5,6]]
#we can also make lists of lists : multidimensional lists
e[2][1]

#not all members of list have to be the same variable type
f = [1, "hello", list(range(0,2)), (2, 4), [1,3]]
f[2]
f[-1][1]
#yeah we can do this with tuples too whatever you get it

#f[-2][1] = 2
#note how this returns an error cause elements in tuples cant be reassigned
f[-2] = (3,5)
#this works because technically the tuple is an element of the list so the entire element can be reassigned

g = (1, 2 , [3, 4])
g[1]
#g[1] = 5 returns error
#g[-1] = [5 , 6] returns error because tuples arent editable
g[-1][1] = 5 
#works because lists are editable

#arrays

#ndarray from numpy is like a list but unlike list all elements must be the same variable type
import numpy as np

np.array(a) #converts list to array but this wont execute because a contains a mix of variables 
h = np.array([1, 4.0, -2, 7])
h # all elements in h are stored as a float because the one 4.0 forces the other ints to become floats 

# np.linspace(start, stop, N) creates array of N (default 50) evenly spaced points from start to end
i = np.linspace(1, 5, 5)
i

# np.logspace(start, stop, N) does the same thing but is on a log scale. Start and stop are powers on 10
jj = np.logspace(0, 2, 5)
jj

# np.arange(start, stop, step) just makes a sequence in an array

k = np.arange(0, 10, 1)
k

# np.zeros(n) makes an array of n elements, all of which are 0
# np.ones (n) makes an array of n elements, all of which are 1

# a maths operator on an array applies to all elements of the entire array 

l = np.array([1, 2, 3, 4, 5])
l + 2
l/2
l**2

# this allows us to do functions easily nice
domain = np.arange(-2, 2, 0.5)
image = domain**2
image

np.exp(domain) # exp(n) is e^n

np.arange(-3.14, 3.14, 0.1)
np.cos(np.arange(-3.14, 3.14, 0.1))

x = np.linspace(-np.pi, np.pi, 21)
y = np.cos(x)
y

2*np.array([1,2,3,4,[1,1]]) + np.array([1,2,3,4,[1,1]])
[1,1] + [1,1]
2*[1,1]
2*np.array([1,1]) 
2**np.array([2,2])


y = np.array([0., 1.3, 5. , 10.9, 18.9, 28.7, 40.])
t = np.array([0., 0.49, 1. , 1.5 , 2.08, 2.55, 3.2])

#using splicing we can do all sorts of calcs that spit out arrays using arrays
v = (y[1:] - y[:-1])/(t[1:] - t[:-1])
v
#like forexample the means of all of the intervals of the array 
avg_t = (t[1:]+t[:-1])/2 
avg_t
#this is so fucking cool

# we can also select only the members of an array that satisfy a certain condition like pick elements greater than 10
v = np.array([ 2.65306122,  7.25490196, 11.8, 13.79310345, 20.85106383, 17.38461538])
v[v > 10]

#again, very fucking cool

#via this we can for example change all the elements that meet certain conditions
v[v > 10] = 0
v

#we can also mix the variables 
# such as selecting from one array and selecting the conidition from the other
w = 1.0/np.arange(0.2, 3, 0.2)
w[w > 1] = 1
w
w[w == 1]

x = np.linspace(0, 10, w.size)
x
x[w == 1] # will select the elements of x that are at the same position as elements from w that satisfy the condition
# only works if the number of elements are same
x[w == 1] = 0
x

# imp
y = np.sin(np.linspace(0, 4 * np.pi, 9))
y
y[np.abs(y) < 1.e-15] = 0
y
#makes them very very small numbers just 0


                    ######## MultiDim arrays

np.array([[1,0],[0,1]])
np.eye(2)
np.array([[1,0,0],[0,1]])
np.array([[1,0,0],[0,1,0],[0,0,1]])
np.eye(3)

#you can also make em like this 
np.ones((3,4), dtype=float)

# you can also make an identity matrix of 2d of N x N 
np.eye(3)

# we can turn 1dim arrays into multidim arrays using np.reshape
np.arange(0,6)
r = np.reshape(np.arange(0,6), (3,2))
r
# how to access them:
r[1][0]

# multi dim arrays the same way as 1 dim arrays, on an element by element basis
np.ones((2,3))
np.ones((2,3))*2
(np.ones((2,3))*2)**3

np.array([[1],[2]])
np.eye(2) * np.array([[1],[2]]) # is not equal to the math equivalent
np.eye(2) * np.array([[1,2]])   # works unlike maths
np.eye(2) * np.array([1,2])     # also works
np.eye(2) * np.array([1,2,3])   # does not work

# so the first element of the array gets multiplied by the first row of the multidim array
# the rows add seperately into each other?
# doesnt really make sense but ok


np.eye(2) + np.array([[1],[2]]) # is not equal to the math equivalent
np.eye(2) + np.array([[1,2]])   # works unlike maths
np.eye(2) + np.array([1,2])     # also works
np.eye(2) + np.array([1,2,3])   # does not work

# if same shape, then they multiply each element with its counterpart
np.array([[1,2],[3,4]]) * np.array([[5,6],[7,8]])
# not the same as matrix multiplication as defined in linear algebra

# matrix multiplication is done with NumPy’s dot function
np.dot(np.eye(2), np.array([[1],[2]]))
# is equal to the maths equivalent

# drawbacks:::

#elements of a NumPy array must all be of the same type

# not part of core python

# Adding additional elements to NumPy array creates a new array and destroys the old one. 
# it can be very inefficient to build up large arrays by appending elements one by one, 
# especially if the array is very large, because you repeatedly create and destroy large arrays. 
# By contrast, elements can be added to a list without creating a whole new list. 
# If you need to build an array element by element, it is usually better to build it as a list, 
# then convert it to an array when the list is complete.

# advantages:::

# support “vectorized” operations like element-by- element addition and multiplication, and other functions

# allow Boolean indexing




# dictionaries 
# this chap is going on for too long man

room = {"E":39, "J":58, "O":74}
#each entry consisting of a key, which in this case is a string, and a value, which in this case is a room number
room["O"]

# dictionaries can be eidited and appended and stuff

record = {}
record["first name"] = "Asad"
record["last name"] = "idiot"  
record["attributes"] = ["islamic", "stubborn", "shayan's bro"]

record["attributes"][1]
record

record.keys()
record.values()

