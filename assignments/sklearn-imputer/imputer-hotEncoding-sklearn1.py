
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

full_dataset = pd.read_csv('train_u6lujuX_CVtuZ9i.csv')
full_dataset


# In[9]:


X_dataset = full_dataset.iloc[ :,1:12]
X_dataset


# In[4]:


print(full_dataset.columns)
len(full_dataset.columns)


# In[10]:


Y_dataset = full_dataset.iloc[:, 12:13]
Y_dataset


# In[11]:


X_dataset.head(20)


# In[ ]:


X_dataset =  X_dataset.replace(0,np.NaN)
X_dataset.head(5)
X_dataset =  X_dataset.replace('0',np.NaN)
X_dataset.head(5)


# In[ ]:


X_dataset['Dependents']
X_dataset['CoapplicantIncome']
X_dataset['Credit_History']


# In[ ]:


X_dataset.mean()


# In[12]:


X_dataset['ApplicantIncome'].mean()


# In[13]:


print(X_dataset['ApplicantIncome'].head(20))


# In[14]:


X_dataset['ApplicantIncome'].fillna(X_dataset['ApplicantIncome'].mean() ,inplace=True)
print(X_dataset['ApplicantIncome'].head(20))


# In[16]:


X_dataset['CoapplicantIncome'].fillna(X_dataset['CoapplicantIncome'].mean() ,inplace=True)
X_dataset['LoanAmount'].fillna(X_dataset['LoanAmount'].mean() ,inplace=True)
X_dataset['Loan_Amount_Term'].fillna(X_dataset['Loan_Amount_Term'].mean() ,inplace=True)
X_dataset['Credit_History'].fillna(X_dataset['Credit_History'].mean() ,inplace=True)


# In[17]:


X_dataset.head(20)


# In[18]:


cols_to_hotEncode = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']
X_dataset_with_dummies = pd.get_dummies(X_dataset, cols_to_hotEncode)
X_dataset_with_dummies.head(20)


# In[66]:


Y_dataset.head(20)


# In[67]:


transformed_Y_dataset = pd.get_dummies(data=Y_dataset, columns=['Loan_Status'])


# In[68]:


transformed_Y_dataset

