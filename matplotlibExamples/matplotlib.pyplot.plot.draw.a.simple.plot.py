
# coding: utf-8

# In[3]:


from matplotlib import pyplot as plt
plt.plot([0,1,2,3,4],[0,1,4,9,16])
plt.show()


# In[5]:


import matplotlib.pyplot as plt
plt.xlabel('I am a Xaxis')
plt.ylabel('I am a yaxis')
plt.plot([1,2,3,4,5],[1,2,9,16,20],'c-')
plt.axis([0, 6, 0, 25])
plt.show()


# In[6]:


import numpy as np
help(np.arange)
np.arange(2,10,step=2)
np.arange(2,10)
type(np.arange(0,10,3))


# In[8]:


from matplotlib import pyplot
pyplot.plot([0,1,2,3,4],[0,1,8,27,64],'b-')
pyplot.axis([0,10,0,100])
pyplot.show()import numpy
print(numpy.ndarray.__doc__)
help(numpy.ndarray)


# In[9]:


import numpy
print(numpy.ndarray.__doc__)
help(numpy.ndarray)

