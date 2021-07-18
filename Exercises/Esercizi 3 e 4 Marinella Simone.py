#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Creo una lista di interi 
numbers = [0, 2, 5, 7, 8, 9]


# In[6]:


numbers


# In[7]:


#Calcolo il massimo tra gli elementi
def massimo(numbers):
    max= 0 
    for i in numbers:
        if i > max: 
            max = i 
    print("Il massimo della lista è {}".format(max))

massimo(numbers)


# In[8]:


print(max(numbers))


# In[9]:


#Calcolo il minimo tra gli elementi 
def minimo(numbers):
    min = 0 
    for i in numbers:
        if i < min:
            min = i 
    print("Il minimo della lista è {}".format(min))

minimo(numbers)


# In[145]:


print(min(numbers))


# In[132]:


#Calcolo la somma tra gli elementi della lista

sum(numbers)


# In[11]:


#Calcolo la media tra gli elementi della lista 

def media(numbers):
    media = sum(numbers)/len(numbers)
    print("La media degli elementi della lista è {}".format(media))

media(numbers)


# In[16]:


#Creo una lista vuota
num = []


# In[17]:


#Inserisco nella lista numeri interi a mio piacimento
num.extend([4, 7, 9, 2])


# In[18]:


num.append(5)


# In[19]:


num.insert(0, 250)


# In[20]:


num


# In[21]:


#Rimuovo i numeri pari dalla lista
for i in num: 
    if(i %2==0):
        num.remove(i)


# In[22]:


num


# In[23]:


#Creo una funzione che restituisce true/false se il parametro è un quadrato perfetto

def quadrato_perfetto(num): 
    sum = 0 
    for i in num:
        if (num %i==0):
            sum = sum + i 
    return sum 

if (num == quadrato_perfetto):
    print("True")
else: 
    print("False")


# In[32]:


#Svolgo l'esercizio precedente utilizzando una compressione di liste 

num = [quadrato_perfetto for n in num]

