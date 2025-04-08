#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In[2]:


import pandas as pd
import numpy as np


# In[3]:


data = pd.read_excel('customer_data.xlsx')
data.head()


# In[4]:


missing_values = data.isnull().sum()
print("Missing values:")
missing_values


# In[5]:


from sklearn.impute import SimpleImputer


# In[6]:


imputer = SimpleImputer(strategy = 'median')
imputer.fit(data[['Income']])
data[['Income']] = imputer.transform(data[['Income']])


# In[7]:


imputer_2 = SimpleImputer(strategy = 'most_frequent')
imputer_2.fit(data[['City']])
data[['City']] = imputer_2.transform(data[['City']])


# In[8]:


missing_values = data.isnull().sum()
print("Missing values:")
missing_values


# In[9]:


data.dtypes


# In[10]:


unique_values = data['Customer_Lifespan_Months'].unique()
unique_values


# In[11]:


data = data[data['Customer_Lifespan_Months'] != 'XXXX']


# In[12]:


data['Customer_Lifespan_Months'].unique()


# In[13]:


data['Customer_Lifespan_Months'] = data['Customer_Lifespan_Months'].astype(int)


# In[14]:


data['Date_of_Purchase'] = data['Date_of_Purchase'].astype('datetime64')


# In[15]:


data.dtypes


# In[16]:


data.head()


# In[17]:


duplicates = data.duplicated()
data[duplicates]


# In[18]:


data.drop_duplicates(inplace = True)


# In[19]:


duplicates = data.duplicated()
data[duplicates]

