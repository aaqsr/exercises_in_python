import numpy as np

# Python reaches an elif or else statement only if all the preceding if and elif statements are False
# once Python finds a true condition, it skips all subsequent elif and else statements in a given if, elif, and else block, irrespective of their truth values
'''
Operator    Function
<           less than
<=          less than or equal to
>           greater than
>=          greater than or equal to
==          equal
!=          not equal 
and         both must be true
or          either must be true
not         reverses the truth value
'''

a = 1
a2 = 7
not a > 2 and a2 < 10

# for <itervar> in <sequence>: 
#   <body>

for n in ['n', 'yayaya', 'm', 'adwadw'] :
    print(n)


# Python program to illustrate 
# enumerate function in loops 
l1 = ["eat","sleep","repeat"] 

# printing the tuples in object directly 
for ele in enumerate(l1): 
	print(ele)
print
# changing index and printing separately 
for count,ele in enumerate(l1,100): 
	print(count,ele)
 
# for i, letter in enumerate(variable):
# "for i-th element(which we will assign to variable "letter") in variable(like list or string)"

# for loops are slow


A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

diag = []
for i in range(0,3):
		diag.append(A[i][i])
np.array(diag)
np.resize(diag, (3,1))
print(diag)

