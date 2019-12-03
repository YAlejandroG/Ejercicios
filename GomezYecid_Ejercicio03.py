#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Ejercicio1
#1.1
import random
promedioLanzamientos = 0
for i in range(1000):
    puntaje = 0
    lanzamientos = 0
    while puntaje<100:
        puntaje += int(5*random.random()+1)
        lanzamientos += 1
    promedioLanzamientos += lanzamientos
print("En promedio se debe lanzar el dado ", promedioLanzamientos//1000, " veces para obtener minimo 100 puntos")


# In[7]:


#Ejercicio2
#2.1
import math
def distancia(l1, l2):
    distancia = 0
    for i in range (len(l1)):
        distancia += (l1[i]-l2[i])**2
    return math.sqrt(distancia)
distancia([0,1,2], [2,3,4])


# In[8]:


#Ejercicio3
#3.1
class Circle:
    def __init__(self, radius):
        self.radius = radius 
    def perimeter(self):
        return 2*math.pi*self.radius
c1 = Circle(1.0)
print (c1.radius)
print (c1.perimeter())
#3.2
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def dot(self, vector2):
        dotProduct = self.x*vector2.x + self.y*vector2.y + self.z*vector2.z
        return dotProduct
    #SegundaParte
    #Clases
    def cross(self, vector2):
        crossProduct = []
        crossProduct.append(self.y*vector2.z-self.z*vector2.y)
        crossProduct.append(-(self.z*vector2.x-self.x*vector2.z))
        crossProduct.append(self.x*vector2.y-self.y*vector2.x)
        self.x = crossProduct[0]
        self.y = crossProduct[1]
        self.z = crossProduct[2]
v = Vector3D(2, 0, 1)
w = Vector3D(1, -1, 3)
dot = v.dot(w)
print (dot)
v.cross(w)
print (v.x, v.y, v.z)


# In[9]:


#Ejercicio4
#4.1
import random
l3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print (l3)
random.shuffle(l3)
print (l3)


# In[6]:


#SegundaParte
#Funciones
def cuenta_palabra(archivo, n_letras=4):
    archivo2 = open(archivo, "r")
    lineas = archivo2.readlines()
    palabras = []
    for i in lineas:
        palabras += i.split()
    palabrasRepetidas = {}
    for j in palabras:
        if len(j)>=n_letras:
            for k in palabras:
                if k == j and k in palabrasRepetidas.keys():
                    palabrasRepetidas[k] = palabrasRepetidas[k]+1
                else:
                    palabrasRepetidas[k] = 1
    print (palabrasRepetidas)
cuenta_palabra('hamlet.txt', 7)


# In[ ]:




