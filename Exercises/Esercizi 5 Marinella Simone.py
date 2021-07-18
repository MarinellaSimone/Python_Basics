#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Homework2


# In[9]:


#Creo una matrice 3x3 con valori compresti tra 0 e 8 

import numpy as np 

np.arange(9).reshape(3, 3)


# In[21]:


#Creo un vettore random con 30 elementi e trovo il valore medio 

a = np.random.rand(30)


# In[22]:


a


# In[24]:


np.mean(a) 
print(f"Il valore medio tra gli elementi dell'array è {np.mean(a)}")


# In[53]:


#Altro modo per creare un vettore random con 30 elementi e trovare il valore medio 

import numpy.random as rdm 

a = rdm.random(30)
a
b = a.mean()
print("Il valore medio tra gli elementi è: {}".format(b))


# In[3]:


#Trovo gli indici degli elementi diversi da zero dal seguente array

Array = [3, 5, 0, 4, 0, 8, 0]
Array 


# In[4]:


import numpy as np 
a = np.array(Array)
a


# In[5]:


np.where(a!=0)


# In[6]:


#Scrivo un programma per ottenere gli indici degli elementi ordinati di un dato array 

Array = [1023, 5202, 6230, 1671, 1682, 5241, 4532]

a = np.array(Array)
a.argsort()


# In[77]:


#Scrivo un programma che calcola la media attraverso la dimensione in un array 2D 

a = [[10, 30], [20, 60]]
np.array(a)


# In[89]:


#media delle colonne

Columns = np.array(a).mean(axis = 0)
Columns


# In[87]:


#media delle righe 

Rows = np.array(a).mean(axis = 1)
Rows

