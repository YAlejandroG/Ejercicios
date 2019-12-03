#!/usr/bin/env python
# coding: utf-8

# In[1]:


def randomGeneration(a, c, m, r):
    randomSequence = [r]
    for i in range(m-1):
        r1 = (a*r+c)%m
        r = r1
        randomSequence.append(r)
    return randomSequence
r = randomGeneration(57, 1, 256, 10)
t = len(r)
print (r)
print ('El periodo de la secuencia generada es: ', t)


# In[49]:


import matplotlib.pylab as plt
x = []
y = []
for i in range(len(r)):
    if i%2==0:
        x.append(r[i])
    else:
        y.append(r[i])
plt.subplot(221)
plt.scatter(x, y, c='g', s=20, marker="x")
plt.title("Correlation random numbers")

n = []
for i in range(len(r)):
    n.append(i)
plt.subplot(222)
plt.plot(n, r, c='g', linewidth=0.9)
plt.xlabel("Sequence number")
plt.ylabel("Random number")

import numpy as np
r1 = []
for i in range(256):
    r1.append(np.random.random())
    
x1 = []
y1 = []
for i in range(len(r1)):
    if i%2==0:
        x1.append(r1[i])
    else:
        y1.append(r1[i])
plt.subplot(223)
plt.scatter(x1, y1, c='g', s=20, marker="x")
plt.title("Correlation random numbers 2")

n1 = []
for i in range(len(r1)):
    n1.append(i)
plt.subplot(224)
plt.plot(n1, r1, c='g', linewidth=0.9)
plt.xlabel("Sequence number")
plt.ylabel("Random number")

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5, wspace=0.5)
plt.savefig("random.png")


# In[54]:


r2 = randomGeneration(9999, 11, 112232, 10)
x2 = []
y2 = []
for i in range(len(r2)):
    if i%2==0:
        x2.append(r2[i])
    else:
        y2.append(r2[i])
plt.subplot(211)
plt.scatter(x2, y2, c='g', s=5, marker="x")
plt.title("Correlation random numbers 3")

n2 = []
for i in range(len(r2)):
    n2.append(i)
plt.subplot(212)
plt.plot(n1, r1, c='g', linewidth=0.7)
plt.xlabel("Sequence number")
plt.ylabel("Random number")

plt.subplots_adjust(top=1.5, bottom=0.08, hspace=0.25)
plt.savefig("random2.png")


# In[42]:


import math
def testUniformity(k, N, r):
    r1=[]
    for j in r:
        n = j**k-1/(k+1)
        r1.append(n)
    c = math.sqrt(N)*abs(sum(r1)/N)
    return c


# In[43]:


k=[1, 3, 7]
N=[100, 10000, 100000]
r3=np.random.random(1000)
for i in k:
    for j in N:
        a = testUniformity(i, j, r3)
        print ("Para k=", i, " y N=", j, ": ", a)
print("Por lo cual el metodo random.random() genera una distribución uniforme")


# In[44]:


r = randomGeneration(57, 1, 256, 10)
for i in k:
    for j in N:
        a = testUniformity(i, j, r)
        print ("Para k=", i, " y N=", j, ": ", a)
print("Por lo cual el metodo linear congruente no genera una distribución uniforme")


# In[ ]:




