#!/usr/bin/env python
# coding: utf-8

# In[43]:


#Ejercicio 07 Primera parte
import random

a = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
def intentosPares(l):
    n = []
    m = random.choice(l)
    n.append(m)
    l.remove(m)
    x = 2
    for i in range(11):
        m = random.choice(l)
        for j in n:
            if m == j:
                return x 
        x+=1     
        n.append(m)
        l.remove(m)


# In[13]:


intentos = []
for i in range(10000):
    b = a.copy()
    intentos.append(intentosPares(b))
prom = sum(intentos)/len(intentos)
print ('Se deben sacar ', '%.3f'%prom, ' medias en promedio del cajón para asegurar que se tiene un par del mismo color.')


# In[112]:


#Segunda parte
moneda = ['C', 'S']
probabilidad = 0
for i in range(5000):
    evento = []
    for j in range(100):
        evento.append(random.choice(moneda))
    caras = 0
    for k in evento:
        if k == 'C':
            caras+=1
    if caras == 50:
        probabilidad+=1
probabilidad /=5000
print('La probalidad de que caigan 50 caras y 50 sellos es: ', probabilidad)


# In[140]:


dias = []
for i in range(365):
    dias.append(i+1)
def pCumpleaños(n):
    prob = 0
    for i in range(1000):
        p = []
        prob2 = 0
        for j in range(n):
            p.append(random.choice(dias))
        for j in p:
            p.remove(j)
            for k in p:
                if j==k:
                    prob2+=1
        if prob2>0:
            prob+=1
    prob/=1000
    return prob


# In[141]:


for i in range (20,40):
    p = pCumpleaños(i)
    if p>0.5:
        print ('El mínimo número de personas necesario para que la probabilidad de que dos o más personas tengan el mismo día de cumpleaños supere 0.5 es:', i)
        break


# In[145]:


for i in range (40,50):
    p = pCumpleaños(i)
    if p>0.9:
        print ('El mínimo número de personas necesario para que la probabilidad de que dos o más personas tengan el mismo día de cumpleaños supere 0.9 es:', i)
        break


# In[ ]:




