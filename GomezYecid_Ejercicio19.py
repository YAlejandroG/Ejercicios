#!/usr/bin/env python
# coding: utf-8

# In[175]:


import numpy as np
import matplotlib.pylab as plt

def fourier(signal):
    N = len(signal)
    Fo = []
    for n in range(N):
        fo = np.complex(0,0)
        for k in range(N):
            exp = np.complex(0,2*np.pi*n*k/N)
            fo += signal[k]*np.exp(-exp)
        fo = np.sqrt(fo.imag**2+fo.real**2)/N
        if fo<0.3:
            fo = 0
        Fo.append(fo)
    return np.array(Fo)

def plotfourier(t,signal,Fo,num,title):
    plt.figure(figsize=(15,5))
    plt.subplot(1,2,2)
    for i in range(len(t)):
        y = np.linspace(0,Fo[i])
        x = np.ones(len(y))*t[i]
        plt.plot(x,y,c='b')
    plt.scatter(t,Fo,c='k',s=20)
    plt.title('Transformada discreta de Fourier')
    plt.subplot(1,2,1)
    plt.plot(t,signal,c='b')
    plt.scatter(t,signal,c='k',s=20)
    plt.title(title)
    plt.savefig(str(num)+'.png')


# In[176]:


def f1(t,w):
    y = 3*np.cos(w*t)+2*np.cos(3*w*t)+np.cos(5*w*t)
    return y

def f2(t,w):
    y = np.sin(w*t)+2*np.sin(3*w*t)+3*np.sin(5*w*t)
    return y

def f3(t,w):
    y = 5*np.sin(w*t)+2*np.cos(3*w*t)+np.sin(5*w*t)
    return y

def f4(t,w):
    y = 5+10*np.sin(w*(t+2))
    return y

def f5(t,w):
    y = 10*np.sin(w*(t+2))
    return y

def f6(t,w):
    y = 5+10*np.sin(w*(t))
    return y

def f7(t,w):
    y = 10*np.sin(w*(t))
    return y

def f8(t,w):
    y = np.sin(w*t)+np.sin(4*w*t)
    return y


# In[178]:


T = 2*np.pi
w = 2*np.pi/T
N = 50
t = np.linspace(0,T,N)
F = [f1,f2,f3,f4,f5,f6,f7,f8]
title = ['y = 3cos(wt)+2cos(3wt)+cos(5wt)','y = sin(wt)+2sin(3wt)+3sin(5wt)','y = 5sin(wt)+2cos(3wt)+np.sin(5wt)',
         'y = 5+10sin(t+2)','y = 10sin(t+2)','y = 5+10sin(t)','y = 10sin(t)','y = sin($\pi$t/2)+np.sin(2$\pi$t)']
for i in range(8):
    signal = F[i](t,w)
    fo = fourier(signal)
    plotfourier(t,signal,fo,i+1,title[i])


# In[ ]:




