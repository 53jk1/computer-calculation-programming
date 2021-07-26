import numpy as np
from fractions import Fraction
L = np.array([[1,0,0], [Fraction(1/2), 1, 0],[Fraction(1/2), Fraction(1/2), 1]])
U = np.array([[2, -1, -1], [1, Fraction(3/2), Fraction(-1/2)], [2,1,Fraction(1/3)]])
A = np.dot(L, U)
b = np.array([1, -1, 2])
print("A = ")
print(A)
Ahelper = np.array([[1.1,-1.2,-1.3],[1.4,1.5,-1.6],[0.7,0.8,1.9]])
print("Arrangement")
print(np.linalg.inv(Ahelper).dot(b))