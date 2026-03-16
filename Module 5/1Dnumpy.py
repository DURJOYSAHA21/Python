import numpy as np
import matplotlib.pyplot as plt
 
a =np.array([1,2,3,4,5])
print(a)
print(type(a))
print(a.dtype)
print(a.size)
print("Dimension:",a.ndim)
print("Size of array in each dimension:",a.shape)
a[1]=100
print(a)
b=a[0:3]
print(b)

a[2:4]=[200,300]
print(a)

u=np.array([1,0])
v=np.array([0,1])
z=u+v
print(z)
z=u-v
print(z)
y=np.array([2,4])
z=2*y
print(z)
c=np.array([2,4])
d=np.array([4,8])
z=c*d
print(z)
z=np.dot(c,d)#dot product
print(z)
z= d+5
print(z)
e=np.array([2,4,5])
print(e.mean())
print(e.max())

x= np.array([0,np.pi/2,np.pi])
y=np.sin(x)
print(y)
y=np.cos(x)
print(y)

x=np.linspace(-2,2,6) #start end how many num
print(x)
x=np.linspace(1,10,20)
print(x)

x=np.linspace(0,2*np.pi,200)
y=np.sin(x)
plt.plot(x,y)
plt.show()