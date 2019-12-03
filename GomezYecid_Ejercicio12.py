#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np

def F(x):
    y = np.cos(x)*np.exp(-(x**2)-x)
    return y

def gauss(f, N):
    integral = 0
    x0, w0 = np.polynomial.legendre.leggauss(N+1)
    x = x0/(1-x0**2)
    w = w0*(1+x0**2)/(1-x0**2)**2
    integral = sum(f(x)*w)
    return integral

print('Método cuadratura Gaussiana, I=',gauss(F,20))


# In[19]:


def f(x):
    y = np.cos(x)
    return y

def g(x):
    y = np.exp(-(x**2)-x)
    return y

def metropolisHastings(f,N):
    x0 = np.random.random()
    x = [x0]
    delta = 1
    for i in range(N):
        xn = x0+delta
        if (f(x0)<f(xn)):
            x0 = xn
            x.append(xn)
        else:
            c = f(xn)/f(x0)
        p = np.random.rand(0,1)
        if (c>p):
            x0 = xn
            x.append(xn)
        else:
            x.append(x0)
    return x

def monteCarlo(f,g,a,b,N):
    x = metropolisHastings(g,N)
    integral = (b-a)*np.sum(f(x))/N
    return integral

I = monteCarlo(f,g,np.pi/2,np.pi,100000)
print('Método Monte Carlo, I=',I)


# In[ ]:


def f1(x):
    y = np.cos((np.sum(x**2))**0.5)
    return y

def g1(x):
    y = np.exp(-(np.sum(x**2))
    return y

