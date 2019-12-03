#!/usr/bin/env python
# coding: utf-8

# In[70]:


#Ejercicio 08 Primera parte
#1.1
import random

def directPi(N):
    n=0
    for i in range(N):
        x = 2*(random.random()-0.5)
        y = 2*(random.random()-0.5)
        if(x**2+y**2<1):
            n+=1
    return n
pi0=[]
for i in range(100):
    pi0.append(directPi(4000))
pi=sum(pi0)/100
pif=pi/1000
print('Direct Pi 100 repeticiones, N=4000: ', '%.3f'%pi, '->', '%.3f'%pif)


# In[71]:


#1.2
def markovPi(N,d):
    n=0
    x,y=1,1
    for i in range(N):
        dx = 2*d*(random.random()-0.5)
        dy = 2*d*(random.random()-0.5)
        if(abs(x+dx)<1 and abs(y+dy)<1):
            x+=dx
            y+=dy
        if(x**2+y**2<1):
            n+=1
    return n
pi0=[]
for i in range(100):
    pi0.append(markovPi(4000,0.3))
pi=sum(pi0)/100
pif=pi/1000
print('Markov Pi 100 repeticiones, N=4000 y delta=0,3: ', '%.3f'%pi, '->', '%.3f'%pif)


# In[72]:


#1.8
def markovTwoSite(k):
    if(k==0): 
        l=1
    if(k==1): 
        l=0
    def probabilidad(n):
        if n==0:
            return 0.4
        else:
            return 0.6
    gamma = probabilidad(l)/probabilidad(k)
    if random.random()<gamma:
        k = l
    return k
k = 0
print('Mark two site p(0)=0.4, p(1)=0.6')
for i in range(20):
    k = markovTwoSite(k)
    print(markovTwoSite(k))


# In[91]:


#1.18
import numpy as np
import matplotlib.pyplot as plt

def gauss(sigma):
    phi = random.random()*2*math.pi
    gamma = -math.log(random.random())
    r = sigma*math.sqrt(2*gamma)
    x = r*math.cos(phi)
    y = r*math.sin(phi)
    return x, y
y1=[]
for i in range(10000):
    x0,y0=gauss(1.0)
    y1.append(x0)
    y1.append(y0)
x = np.linspace(-3, 3, 100)
y = 3750/(2*np.pi)*np.exp(-0.5*((x)**2))

plt.figure()
plt.plot(x, y)
plt.hist(y1, 100)
plt.title('Gaussiana')
plt.savefig('Gausiana.png')


# In[ ]:




