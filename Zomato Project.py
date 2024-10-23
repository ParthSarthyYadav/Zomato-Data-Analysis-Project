#!/usr/bin/env python
# coding: utf-8

# # Zomato Data Analysis Project

# Step 1: Importing libraries

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Step 2: Creating dataframe

# In[4]:


dataframe = pd.read_csv("Zomato data .csv")


# In[5]:


print(dataframe)


# In[6]:


dataframe


# Step 3: Converting data type of 'rate' column

# In[7]:


def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate)


# In[8]:


print(dataframe.head())


# In[9]:


dataframe.info()


# ## Type of restraunt

# In[10]:


dataframe.head()


# In[13]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel('Type of restraunt')


# ### Conclusion 1: Majority of the restraunt fall in 'Dining' category

# In[14]:


dataframe.head()


# In[16]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes':grouped_data})
plt.plot(result, c='green',marker='o')
plt.xlabel("Type of restraunt", c='red', size = 20)
plt.ylabel("Votes", c='red', size = 20)


# ### Conclusion 2: Dining restraunts have maximum number of votes

# In[17]:


plt.hist(dataframe['rate'], bins=5)
plt.title('Ratings Distribution')
plt.show()


# ### Conclusion 3: Majority restraunts have ratings between 3.5 to 4

# In[18]:


dataframe.head()


# In[19]:


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# ### Conclusion 4: Majority couples prefer restraunts with an approx cost of 300 Rs

# In[20]:


dataframe.head()


# In[22]:


plt.figure(figsize = (6,6))
sns.boxplot(x= 'online_order', y= 'rate', data = dataframe)


# ### Conclusion 5: Offline order recieved lower ratings comapred to online order

# In[23]:


dataframe.head()


# In[24]:


pivot_table = dataframe.pivot_table(index = 'listed_in(type)', columns = 'online_order', aggfunc = 'size', fill_value = 0)
sns.heatmap(pivot_table, annot= True, cmap= 'YlGnBu', fmt = 'd')
plt.title("Heatmap")
plt.xlabel("online_order")
plt.ylabel("listed_in(type)")
plt.show()


# ### Conclusion 6: Dining restraunts primarily accept offline orders, whereas cafes primarily recieve online orders.This suggests that clients preferorders in person at restraunts, but prefer online ordersa at cafes.
