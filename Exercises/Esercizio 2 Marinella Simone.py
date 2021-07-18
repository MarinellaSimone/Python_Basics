#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Creo una funzione che esegue l'addizione tra due numeri interi che gli vengono passati come parametri e che ha come valore di ritorno la somma dei due numeri 

def addizione(a, b):
    print("Eseguo e restituisco la somma tra {} e {}.".format(a, b))
    c = a + b 
    return c


# In[5]:


#Invoco la funzione creata con valori a mio piacimento

addizione(10, 4)


# In[4]:


#Assegno il valore restituito ad una terza variabile 

risultato = addizione(10, 4)

risultato


# In[25]:


#Creo una funzione che concateni due stringe passate come parametro e che stampi la stringa finale in caratteri maiuscoli

def concatenazione(a, b): 
    print("Eseguo la concatenazione tra {} e {}.".format(a, b))
    completo = a + b 
    completo = completo.upper()
    return completo
    print("completo.upper()")


# In[26]:


#Invoco la funzione creata con stringhe a mio piacimento 

concatenazione("Marinella", "Simone")


# In[34]:


#Creo una funzione che raddoppia il primo parametro e che triplica il secondo e che stampi i due valori di ritorno nel formato "il doppio di è..., mentre il triplo di... è" 

def operazioni(a, b):
    c = a*2
    d = b*3
    print("il doppio di {} è {}, mentre il triplo di {} è {}.".format(a, c, b, d))


# In[35]:


#Invoco la funzione creata con valori a mio piacimento

operazioni(10,4)

