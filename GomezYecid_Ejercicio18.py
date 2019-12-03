#!/usr/bin/env python
# coding: utf-8

# In[115]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('USArrests.csv')
Murder = np.array(data['Murder'])
Murder = (Murder-Murder.mean())/Murder.std()
Assault = np.array(data['Assault'])
Assault = (Assault-Assault.mean())/Assault.std()
UrbanPop = np.array(data['UrbanPop'])
UrbanPop = (UrbanPop-UrbanPop.mean())/UrbanPop.std()
Rape = np.array(data['Rape'])
Rape = (Rape-Rape.mean())/Rape.std()
states = np.array(data['Unnamed: 0'])
matriz = np.array([Murder,Assault,UrbanPop,Rape])


# In[116]:


mcov = np.cov(matriz)
val,vect = np.linalg.eig(mcov)
vec1 = vect[:,0]
vec2 = vect[:,1]


# In[117]:


variables= ['Murder', 'Assault', 'UrbanPop', 'Rape']
plt.figure(figsize=(12,11))

for i in range(len(states)):
    statesX = np.dot(vec1,matriz[:,i])
    statesY = np.dot(vec2,matriz[:,i])
    plt.annotate(states[i],(statesX,statesY),fontsize=9,c='green')
    plt.scatter(statesX,statesY,c='white')

for i in range(len(vec1)):
    plt.arrow(0,0,3*vec1[i],3*vec2[i],head_width=0.04,color='orange')
    plt.annotate(variables[i],(3.2*vec1[i],3.2*vec2[i]),fontsize=12,c='orange')

plt.grid()
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.ylim(-3,2.5)
plt.savefig('arrestos.png')


# In[118]:


data2 = pd.read_csv('Cars93.csv')
Model = np.array(data2['Model'])
Horsepower = np.array(data2['Horsepower'])
Horsepower = (Horsepower-Horsepower.mean())/Horsepower.std()
Length = np.array(data2['Length'])
Length = (Length-Length.mean())/Length.std()
Width = np.array(data2['Width'])
Width = (Width-Width.mean())/Width.std()
Fuel = np.array(data2['Fuel.tank.capacity'])
Fuel = (Fuel-Fuel.mean())/Fuel.std()
matriz2 = np.array([Horsepower,Length,Width,Fuel])


# In[119]:


mcov2 = np.cov(matriz2)
val2,vect2 = np.linalg.eig(mcov2)
vec21 = vect2[:,0]
vec22 = vect2[:,1]


# In[120]:


variables2= ['Horsepower', 'Length', 'Width', 'TankCapacity']
plt.figure(figsize=(14,12))

for i in range(len(Model)):
    modelX = np.dot(vec21,matriz2[:,i])
    modelY = np.dot(vec22,matriz2[:,i])
    plt.annotate(Model[i],(modelX,modelY),fontsize=8.5,c='green')
    plt.scatter(modelX,modelY,c='white')

for i in range(len(vec21)):
    plt.arrow(0,0,2.5*vec21[i],2.5*vec22[i],head_width=0.04,color='orange')
    plt.annotate(variables2[i],(3.9*vec21[i],2.8*vec22[i]),fontsize=12,c='orange')

plt.grid()
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.ylim(-2.5,2)
plt.savefig('cars.png')


# In[ ]:




