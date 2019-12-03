#!/usr/bin/env python
# coding: utf-8

# In[78]:


#Ejercicio 09 Primera parte
import numpy as np
import matplotlib.pyplot as plt
import decimal

def biasedCoin(c,s):
    x = np.linspace(0,1,500)
    y = x**c*(1-x)**s
    return x, y


# In[106]:


CyS = [[1,0],[4,6],[35,65],[320,680]]
plt.figure(figsize = (10,3))

for i in CyS:
    x, y = biasedCoin(i[0],i[1])
    f = plt.subplot(2, 2, CyS.index(i)+1)
    plt.plot(x, y, c='g', label='H= '+str(i[0])+', C= '+str(i[1]))
    plt.title('prob(H|{data},I)')
    plt.legend()
    f.axes.get_yaxis().set_visible(False)
plt.subplots_adjust(top=1.5, bottom=0.08, hspace=0.35)
plt.savefig('biasedCoin.png')


# In[119]:


def lighthouse(xk):
    beta = 3
    alfa = np.linspace(-6,6,500)
    y = np.ones(500)
    for i in xk:
        y *= beta/(np.pi*(beta**2+(i-alfa)**2))
    y /= 12
    return alfa, y


# In[120]:


X = [-5.2, -3.1, -2.8, -3.5]
xk = []
l = ''
plt.figure(figsize = (10,3))

for j in X:
    xk.append(j)
    l += str(j)+', '
    xk = np.asarray(xk)
    x, y = lighthouse(xk)
    f = plt.subplot(2, 2, X.index(j)+1)
    plt.plot(x, y, c='g', label='xk = '+l)
    plt.axvline(xk.mean(), color='k', linestyle='dashed', linewidth=1)
    plt.title('prob(alfa|xk)')
    plt.legend()
    f.axes.get_yaxis().set_visible(False)
    xk = list(xk)
plt.subplots_adjust(top=1.5, bottom=0.08, hspace=0.35)
plt.savefig('lightHouse.png')


# In[132]:


def desintegracion(xi):
    Q = np.linspace(0.1,1,500)
    y = np.ones(500)
    for i in xi:
        y *= np.exp(-Q*i)/Q
    return Q, y


# In[134]:


Xi = [0.5, 1.0, 0.8, 0.9]
xi = []
l1 = ''
plt.figure(figsize = (10,3))

for k in Xi:
    xi.append(k)
    l1 += str(k)+', '
    xi = np.asarray(xi)
    x, y = desintegracion(xi)
    f = plt.subplot(2, 2, Xi.index(k)+1)
    plt.plot(x, y, c='g', label='xi = '+l1)
    plt.title('prob(Q|xi)')
    plt.legend()
    f.axes.get_yaxis().set_visible(False)
    xi = list(xi)
plt.subplots_adjust(top=1.5, bottom=0.08, hspace=0.35)
plt.savefig('desintegracion.png')


# In[ ]:




