#!/usr/bin/env python
# coding: utf-8

# In[146]:


#Ejercicio 10 Primera parte
import numpy as np
from scipy.special import factorial
import matplotlib.pylab as plt

def backGroundB(xk, Nk, w):
    prob = np.ones((100,100))
    A = np.linspace(0,100,100)
    B = np.linspace(0,100,100)
    A,B = np.meshgrid(A,B)
    
    x = []
    for j in range(len(xk)):
        for k in range(Nk[j]):
            x.append(xk[j])
    plt.figure(figsize = (12,4))
    plt.subplot(121)
    plt.hist(x, bins=len(xk))
    plt.ylabel('Number of counts N')
    plt.xlabel('Measurement variable x')
    
    for i in range(len(xk)):
        Dk = (A*np.exp(-1*(xk[i]**2)/(2*w**2))+B)
        prob *= (Nk[i]*np.log(Dk)-Dk)
    
    plt.subplot(122)
    plt.contour(A,B,prob)
    plt.ylabel('Background B')
    plt.xlabel('Amplitude A')
    plt.savefig('Background.png')


# In[147]:


xk = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
Nk = [60, 70, 70, 80, 90, 110, 90, 80, 60, 55, 60]
backGroundB(xk,Nk,5)


# In[162]:


def lighthouse(x):
    beta = 3
    alfa = np.linspace(-7,7,100)
    n = []
    for i in range(len(x)):
        for j in alfa:
            prob = beta/(np.pi*(beta**2+(x[i]-j)**2)*14)
            for k in range(int(prob*10000/(i+1))):
                n.append(j)
    
    return n


# In[163]:


X = [-5.2, -3.1, -2.8, -3.5]
xk = []
l = ''
plt.figure(figsize = (10,3))

for j in X:
    xk.append(j)
    l += str(j)+', '
    xk = np.asarray(xk)
    n = lighthouse(xk)
    plt.subplot(2, 2, X.index(j)+1)
    plt.hist(n, bins=25, label='xk = '+l)
    plt.title('prob(alfa|xk)')
    plt.legend()
    xk = list(xk)
plt.subplots_adjust(top=1.5, bottom=0.08, hspace=0.35)
plt.savefig('lightHouse.png')


# In[161]:


n = lighthouse(X)
print(len(n))


# In[ ]:




