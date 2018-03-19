
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd

#help(pd.date_range)

pandas_dates = pd.date_range(start='20181201', periods=5)
pandas_datespandas_dates = pd.date_range(start='20181201', end='20181231')
pandas_dates


# In[12]:


pandas_dates = pd.date_range(start='20181201', end='20181231')
pandas_dates


# In[47]:


pd.Series([1,'a', np.nan,True])


# In[55]:


#See How it makes it 0 or 1 in np.ndarray because its supposed to be homogenous
np.array([1, 5.0, 123, False])


# In[56]:


np.array([1, 5.0, 123, 'Hmm', False])

