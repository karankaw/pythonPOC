
# coding: utf-8

# In[ ]:


import sys
paths = sys.path
typeof_paths =type(paths)

print(paths)
print('type of sys.path',typeof_paths)


# In[3]:


import iamanewModule
iamanewModule.function1()
#make a new folder named 'iamanewModule' and place all of logic in __init__.py file 
#whatever is inside __init__.py, it will be imported as such on module import.
#https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3


# In[ ]:


#import os
#cwd = os.getcwd()
#print(cwd)
#sys.path.append(cwd + '/sub_module')
#print(paths)


# In[ ]:


import iamanewModule
iamanewModule.function1()

