#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dichiaro due variabili numeriche 
x1 = 4
y1 = 6 


# In[2]:


x1


# In[3]:


y1


# In[9]:


#Eseguo un'operazione qualsiasi che le coinvolga
x1 + y1


# In[10]:


#Eseguo un'operazione qualsiasi che le coinvolga 
x1/y1


# In[11]:


#Eseguo un'operazione qualsiasi che le coinvolga
x1**y1


# In[12]:


#Salvo il risultato in una terza variabile 
x2 = x1 + y1


# In[13]:


x2


# In[21]:


#Stampo il risultato nella forma "Il risultato dell'operazione ...tra...e ...è ...""
print('Il risultato della somma tra {} e {} è {}'.format(x1, y1, x2))


# In[22]:


#Commento le righe del codice con il significato delle azioni corrispondenti
print('x1 vale 4')
print('y1 vale 6')
print('la somma tra',x1,y1,'vale', x2) 


# In[23]:


#Utilizzo il comando %whos per vedere tutti i valori delle variabili create

get_ipython().run_line_magic('whos', '')


# In[24]:


#Stampo la riga "Ho creato il mio primo programma"

a = 'Ho creato il mio primo programma' 
print(a)


# In[25]:


a = "programma"
print('Ho creato il mio primo {}'.format(a)) 

