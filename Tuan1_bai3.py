import numpy as np
def Xmatrix():
    if n==x:
        return matA.dot(matB)
    return None
m = int(input())
n = int(input())
x = int(input())
y = int(input())
np.random.seed(0)
matA = np.random.randint(0,20,size =(m,n))
print(matA)
matB = np.random.randint(0,20,size =(x,y))
print(matB)
print(Xmatrix())