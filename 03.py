import numpy as np
L = np.array([[4.1,4.1,4.1],[4.1,4.1,4.9],[4.1,1.6,4.1]])
U = np.array([[4.1,4.1,4.1],[4.1,4.1,4.1],[4.1,4.1,4.1]])
A = np.dot(L, U)

print("A = ")
print(A)
print("|A| = ")
print(np.linalg.det(A))