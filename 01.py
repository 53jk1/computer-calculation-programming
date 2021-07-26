import numpy as np
x = np.array([1,3,4,3,2])
y = np.array([1,1,2,5,4])

def Area(x, y):
    return 0.5*np.abs(np.dot(x, np.roll(y,1))-np.dot(y,np.roll(x,1)))

print(Area(x, y))
