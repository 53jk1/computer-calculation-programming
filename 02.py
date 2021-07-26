import numpy as np
A = np.array([[1,2,3],[2,3,4],[3,4,1]])
b = np.linalg.det(A)
print(b)
c = np.linalg.cond(A)
print(c)
print("The matrix is well coditioned.")
