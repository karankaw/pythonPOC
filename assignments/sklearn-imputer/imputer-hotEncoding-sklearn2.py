
# coding: utf-8

# In[1]:


#2nd CSV Example, In this we will use imputer and strategy
from sklearn.preprocessing import Imputer
import pandas as pd
import numpy as np

full_dataset = pd.read_csv('train.csv')
full_dataset

#print(full_dataset.columns)
len(full_dataset.columns)

x_dataset = full_dataset.iloc[ : , 1:26 ]
y_dataset = full_dataset.iloc[ : , 26:27]

column_list = ['MSZoning', 'Street', 'Alley', 'LotShape','LandContour','Utilities','LotConfig',
               'LandSlope','Neighborhood','Condition1',	'Condition2','BldgType','HouseStyle',
               'RoofStyle', 'RoofMatl','Exterior1st','Exterior2nd','MasVnrType']
hot_encoded_x_dataset =  pd.get_dummies(data=x_dataset, columns=column_list)
hot_encoded_x_dataset #All are numbers now


# In[2]:


new_cols = hot_encoded_x_dataset.columns
new_cols


# In[3]:


#imputer = Imputer(missing_values=np.NaN, axis=0, strategy='mean')
imputer = Imputer()
new_x_dataset = imputer.fit_transform(hot_encoded_x_dataset)

type(new_x_dataset)#ndarray
pd.DataFrame(new_x_dataset,columns=new_cols)

