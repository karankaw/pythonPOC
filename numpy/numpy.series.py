
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

#help(pd.date_range)

pandas_dates = pd.date_range(start='20181201', periods=5)
pandas_datespandas_dates = pd.date_range(start='20181201', end='20181231')
pandas_dates


# In[ ]:


pandas_dates = pd.date_range(start='20181201', end='20181231')
pandas_dates


# In[ ]:


pd.Series([1,'a', np.nan,True])


# In[ ]:


#See How it makes it 0 or 1 in np.ndarray because its supposed to be homogenous
np.array([1, 5.0, 123, False])# It becomes float here


# In[ ]:


np.array([1, 5.0, 123, 'Hmm', False])

