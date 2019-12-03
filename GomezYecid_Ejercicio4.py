#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Ejercicio1
#1.1
import numpy as np
n1 = np.random.rand(4, 8)
print (n1)
n1[:,-1] = -1
print (n1)
n1[1,:] = 2
print (n1)
#1.2
n2 = np.random.normal(size=1000)
a = len(n2[n2>2.0])
print (a)
print ('El 95,44 de la distribución normal se encuentra entre dos desviaciones estandar alrededor del centro, por lo cual la cantidad de numeros mayores a 2, es decir fuera de este intervalo corresponde a al 2,29 de la distribucion, es decir, cerca de 22 números, lo cual corresponde a lo obtenido en el ejercicio. (', a,')')
positivos = np.greater(n2,0)
negativos = np.less(n2,0)
n2[positivos] = 1
n2[negativos] = -1
print (n2)


# In[21]:


#Ejercicio4
#4.1
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.figure()
t = np.linspace(0,10,1000)
x = 10*np.sin(5*t)
y = 10*np.sin(4*t)
plt.plot (x, y) 
plt.title("Lissajous curve") 
#4.2
def circulo(N):
    plt.figure()
    x = np.random.uniform(-1,1,N)
    y = np.random.uniform(-1,1,N)
    circulo = (x**2+y**2)<=1
    plt.scatter(x[circulo],y[circulo],s=4)
    plt.axis("equal")
    plt.title("Circulo")
    return x, y
x1, y1 = circulo(1000)
def esfera(N):
    theta=np.random.uniform(0, 2*np.pi,N)
    phi=np.random.uniform(0, np.pi,N)
    fig = plt.figure()
    ax = Axes3D(fig)
    x = np.cos(theta)*np.sin(phi)
    y = np.sin(theta)*np.sin(phi)
    z = np.cos(phi)
    ax.scatter(x, y, z, c='g', s=4)
    ax.set_xlim3d(-1.4,1.4)
    ax.set_ylim3d(-1.2,1.2)
    ax.set_zlim3d(-0.8,0.8)
    plt.show()
    return x, y, z
x2, y2, z2 = esfera(1000)


# In[20]:


#Parte2
import math
plt.figure()
for i in range(10):
    vx = (i+1)*2-1
    vy = math.sqrt(400-vx**2)
    a = -10
    tv = abs(2*vy/a)
    t = np.linspace(0, tv, 100)
    x = t*vx
    y = t*vy + 0.5*a*t*t
    x1 = vx*tv/2
    y1 = vy*tv/2 + 0.5*a*(tv/2)**2
    plt.scatter(x1, y1, c="black", s=40)
    plt.plot (x, y, c="g") 
    vx = -((i+1)*2-1)
    x = t*vx
    x1 = vx*tv/2
    plt.scatter(x1, y1, c="black", s=40)
    plt.plot (x, y, c="g") 
    plt.title("N=20, -19<=Vox<=19, |v|=20, a=-10")


# In[ ]:




