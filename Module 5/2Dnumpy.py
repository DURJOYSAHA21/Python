import numpy as np

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A=np.array(a)
print(A.ndim)
print(A.shape)
print(A.size) #total ele
print(A[1,2])
print(A[0,0:2])

X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 1], [1, 2]])

z=X+Y
print(z)

z_scaler=2*Y
print(z_scaler)

z_elementmulti=X*Y
print(z_elementmulti)

z_dotormatrix=np.dot(X,Y) # A@B
print(z_dotormatrix)

x=np.array([[[1,2],[3,4]]])
print(np.sum(x))
print(np.sum(x,axis=0))# col wise sum 
print(np.sum(x,axis=1))#rowise sum

a_transpose=A.T
print(a_transpose)

row=np.array([1,2,3])
result=a+row
print(result)

ar=np.array([1,2,3,4,5,6])
new_matrix=ar.reshape(2,3)
print(new_matrix)

