import numpy as np


A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

diag = []
for i in range(3):
		diag.append(A[i][i])
np.array(diag)
print(np.resize(diag, (3,1)))

# or we can simply 

diag2 = [A[i][i] for i in range(3)]
print(np.resize(np.array(diag2),(3,1)))
# much smaller

# to get column from A
ColA = [A[i][0] for i in range(3)]
ColA
# or
c1 = [a[1] for a in A]
c1

# conditions too
data = [-5, -3, 1, 7, 4, 23, 27, -9, 11, 41]
[x for x in data if x%3==0]