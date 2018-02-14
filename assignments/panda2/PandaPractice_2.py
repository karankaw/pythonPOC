
# coding: utf-8

# ##### Learn various methods of DataFrame
# ##### Learb iloc[]   loc[]
# ##### read_csv("", header=None)

# In[ ]:


import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib as plt


# In[9]:


random_ndarray = np.random.randn(2,5)
random_ndarray


# In[27]:


dataframe = pd.DataFrame(random_ndarray)
dataframe


# In[30]:


hmm = dataframe.values
hmm
hmm[0:2,1:4]


# In[72]:


dataframe[0:2,1:4]


# In[36]:


type(dataframe.values)


# In[38]:


type(dataframe.iloc[:,:])


# In[76]:


dataframe_named = pd.DataFrame(random_ndarray , index=['cat', 'dog'], columns=['A','B','C','D','E'])
dataframe_named


# In[52]:


diabetes_df = pd.read_csv("pima-indians-diabetes.csv", header=None)
diabetes_df


# In[53]:


type(diabetes_df)


# In[58]:


diabetes_df.head(5)


# In[69]:


diabetes_df.iloc[0:3,1:5]


# In[70]:


diabetes_df[[0]] = diabetes_df[[0]].replace(0, np.NaN)
diabetes_df.head(5)


# In[64]:


listu = np.random.randn(2,5).tolist()
print(listu)


# ** list[[]] does not work **

# In[65]:


listu[[0,1]]


# ** DataFrame[[]] does work **

# In[71]:


diabetes_df[[0,1]]


# In[80]:


diabetes_df[0]


# In[81]:


diabetes_df.columns


# In[85]:


diabetes_df

