import numpy as np
L = np.array([[1,0,0],[1,1,0],[1,1.6,1]])
U = np.array([[1,2,3],[1,2,3],[1,2,3]])
A = np.dot(L, U)

print("A = ")
print(A)
print("|A| = ")
print(np.linalg.det(A))