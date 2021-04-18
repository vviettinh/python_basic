import numpy as np 
m = int(input())
n = int(input())
np.random.seed(0)
matrix = np.random.randint(0,10,size =(m,n))
print(matrix)
tatol = np.sum(np.diag(matrix,k=0))
print("tổng đường trụ chéo chính: "+ str( tatol) )
matrix=np.sort(matrix,axis=1).T
print("giá trị lớn nhất mỗi hàng: \n",matrix[-1].reshape(m,1))
print("giá trị nhỏ nhất mỗi hàng: \n",matrix[0].reshape(m,1))

