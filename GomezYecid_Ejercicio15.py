#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import matplotlib.pylab as plt

A = [[4,-2,1],
    [3,6,-4],
    [2,1,8]]

Ainv = np.linalg.inv(A)
print('Matriz invesa de A =',Ainv)
mul = np.matmul(A,Ainv)
mul[mul<1E-10] = 0
print('A*Ainv =',mul)


# In[11]:


b1 = [12,-25,32]
x1 = np.linalg.tensorsolve(A,b1)
b2 = [4,-10,22]
x2 = np.linalg.tensorsolve(A,b2)
b3 = [20,-30,40]
x3 = np.linalg.tensorsolve(A,b3)
print('x1= ',x1,', x2= ',x2,', x3= ',x3)


# In[15]:


alfa = 1
beta = 2
A0 = [[alfa,beta],[-beta,alfa]]
val0, vect0 = np.linalg.eig(A0)
print('alfa= ',alfa,',beta= ',beta)
print('Eigenvalues= ',val0)
print('Eigenvectors: v1 = ',vect0[:,0],' v2 = ',vect0[:,1])


# In[10]:


A1 = [[-2,2,-3],
     [2,1,-6],
     [-1,-2,0]]
val, vect = np.linalg.eig(A1)
print('Eigenvalues= ',val)
print('Eigenvectors: v1 = ',vect[:,0],' v2 = ',vect[:,1],' v3 = ',vect[:,2])


# In[19]:


A2 = np.zeros((100,100))
b0 = np.zeros(100)
for i in range(100):
    for j in range(100):
        A2[i,j] = 1/(i+j+1)
    b0[i] = 1/(i+1)
    
y = np.linalg.tensorsolve(A2,b0)
print('y = ',y)


# In[48]:


def newtonDanimate(x,n=9):
    eps = np.exp(-6)
    d = np.zeros((n,n))
    f = np.zeros(n)
    
    plt.figure()
    L1 = 3
    L2 = 4
    L3 = 4
    xa = x[3]*L1
    ya = x[0]*L1
    xb = xa+L2*x[4]
    yb = ya+L2*x[1]
    xc = xb+L3*x[5]
    yc = yb-L3*x[2]
    mx = 100
    bx = -500
    my = -100
    by = 400    
    xp = [bx,mx*xa+bx,mx*xb+bx,mx*xc+bx]
    yp = [by,my*ya+by,my*yb+by,my*yc+by]
    plt.plot(xp,yp,c='g',label='Inicial')
    plt.legend()
    plt.title('String and masses configuration')
    plt.savefig('newtonNDanimate.png')
    
    


# In[49]:


xf = np.array([0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,1,1])
newtonDanimate(xf)


# In[ ]:




