import numpy as np

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([x[i][2] for i in range(3)])

print(
    2 * (
        np.array( [x[i][1] for i in range(3)]
                 )**2)
    )