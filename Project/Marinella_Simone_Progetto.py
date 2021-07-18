#!/usr/bin/env python
# coding: utf-8

# **GENDER PAY GAP**

# In[36]:


import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import plotly.express as px 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv("Gender_Pay_Gap_Data.csv")
df.head(7)


# In[3]:


df.describe()


# In[4]:


df.shape


# In[5]:


df.rename(columns= {"Dept": "Department"}, inplace=True)
df.rename(columns={"PerfEval":"Performance score"}, inplace=True)
df.rename(columns={"BasePay": "Annual Basic Pay"}, inplace=True)

df


# In[6]:


def display_all(df):
    with pd.option_context("display.max_rows", 1001, "display.max_columns", 1001):
        display(df)


# In[7]:


display_all(df)


# In[8]:


dfr = df.drop(["Seniority", "Bonus", "Performance score", "Age"], axis=1)
dfr


# In[9]:


dfr[dfr.columns[1]]


# In[10]:


colonne = ["JobTitle", "Gender", "Department", "Education"]

for x in colonne: 
    dfr[x] = dfr[x].astype("category")

dfr.info()


# In[11]:


Female = (dfr.Gender == "Female")


# In[12]:


Job_Female = dfr[Female].JobTitle
x = Job_Female.value_counts()
x


# In[13]:


Male = (dfr.Gender == "Male")
Job_Male = dfr[Male].JobTitle
y = Job_Male.value_counts()
y


# In[14]:


dfr.JobTitle.unique()
dfr.JobTitle.value_counts()


# In[15]:


dfr.Education.unique()
dfr.Education.value_counts()


# In[16]:


dfr.groupby(["Gender", "Department", "JobTitle"])["Annual Basic Pay"].value_counts(normalize=True)*100


# In[17]:


Annual_Pay= dfr.sort_values("Annual Basic Pay")
plt.bar("Gender", "Annual Basic Pay", data= Annual_Pay, facecolor= "darkgrey")
plt.xlabel("Gender", size=14)
plt.ylabel("Annual Basic Pay", size=14)
plt.title("Differenza salario annuo tra Male e Female", size= 20);


# In[35]:


plot = px.bar(dfr,x="Department", y="Annual Basic Pay", color="Gender", barmode="group", facet_col="Education", category_orders={"Education":["High School", "College", "Masters", "PhD"]}, labels={"Annual_Pay":"Annual Pay"}, color_discrete_sequence= px.colors.qualitative.Pastel1)

plot.show()


# In[19]:


Ambiti = ["JobTitle", "Performance score", "Education", "Department", "Seniority"]

for i in Ambiti:
    fig= px.histogram(df, x=i, color="Gender", color_discrete_sequence= px.colors.qualitative.Pastel1, barmode="group", title= "Gender gap per {}".format(i))

    fig.show()


# In[20]:


sns.set_palette("pastel")
sns.pairplot(df, plot_kws=dict(marker= "+", linewidth=1), diag_kws=dict());


# In[21]:


#Annual Basic Pay e Bonus, calcolo il Total Pay

df["Total_Pay"]= df["Annual Basic Pay"] + df["Bonus"]
Total_Pay_pivot= df.pivot_table(index= "JobTitle", columns="Gender", values= "Total_Pay").reset_index()
Total_Pay_pivot


# In[22]:


px.bar(df, x="JobTitle", y="Total_Pay", color="Gender", barmode="stack", color_discrete_sequence=px.colors.qualitative.Pastel2)


# In[23]:


Education_pivot= df.pivot_table(index=["Education"], columns="Gender", values="Total_Pay")
Education_pivot


# In[24]:


Seniority_pivot=df.pivot_table(index=["Seniority"], columns="Gender", values="Total_Pay")
Seniority_pivot


# In[25]:


Performance_pivot = df.pivot_table(index= ["Performance score"], columns= "Gender", values= "Total_Pay")
Performance_pivot


# In[26]:


#correlazione 

x = [Performance_pivot.Female]
y = [Seniority_pivot.Female]

x1 = [Performance_pivot.Male]
y1 = [Seniority_pivot.Male]

plt.scatter(x,y, label='Female',color='pink');
plt.scatter(x1,y1,label='Male',color='grey');
plt.xlabel('Performance score');
plt.ylabel('Seniority');
plt.title('SCATTER PLOT');
plt.legend();


# In[27]:


#Seniority 

Seniority_pivot = df.pivot_table(index= "Seniority", columns= "JobTitle", values= "Total_Pay").reset_index()
Seniority_pivot


# In[28]:


plt.figure(figsize=(7,8))

sns.boxplot(data =df, x="Department", y="Total_Pay", hue="Gender", showfliers= False, palette="pastel")

plt.legend(loc="upper right")
plt.show()


# In[29]:


sns.heatmap(Seniority_pivot, linewidths = "2", linecolor="grey", square=False, cmap= "flare");


# In[30]:


#Age

sns.displot(df, x= "Age", hue= "Gender", kind= "kde", fill= True, color= "Pastel");


# In[31]:


df["Age"].describe()


# In[32]:


Gender_Job_Dep_Pay= dfr.groupby(["Department", "JobTitle", "Gender"]).mean()
Gender_Job_Dep_Pay 


# In[33]:


fig = px.treemap(dfr, path=["Department", "JobTitle", "Gender"], values= "Annual Basic Pay", labels= {"Annual Basic Pay" : "Avarage Annual Pay"}, color_discrete_sequence = ["goldenrod"], width=1100, height=600)

fig.show()


# In[34]:


#esporto il dataset df
import os 
os.getcwd()
path_output = 'C:\\Users\\marin\\Downloads'
os.chdir(path_output)
os.getcwd()
lista_files = os.listdir()
lista_files
df.to_excel('output.xlsx')


# In[ ]:




