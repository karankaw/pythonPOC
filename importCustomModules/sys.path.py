
# coding: utf-8

# In[3]:


import sys
paths = sys.path
typeof_paths =type(paths)

print(paths)
print('type of sys.path',typeof_paths)


# In[4]:


import iamanewModule
iamanewModule.function1()


# In[5]:


import os
cwd = os.getcwd()
print(cwd)
sys.path.append(cwd + '\\sub_module')
print(paths)


# In[7]:


import iamanewModule
iamanewModule.function1()

