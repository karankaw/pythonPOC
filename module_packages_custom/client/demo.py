
# coding: utf-8
# Packages and Modules
# Its possible to have empty __init__.py
# In[3]:

#this submodsubmodule is inside current directory
#Works just like that , import name
import insideFile
insideFile.function1()



# In[ ]:
#2nd option - Append Path of dir to sys.path (Not recommended for prod)
import sys
import os

cwd = os.getcwd()
print(cwd)

paths = sys.path
typeof_paths = type(paths)
print('type of sys.path',typeof_paths)

sys.path.append(cwd + '/../outside_sub_module')
print("===============================================\n",paths)


#this submodsubmodule is inside current directory
#The path of this module is appended to sys.path
from sysPathEnabledPython import functionAbc
print('===============================================')
functionAbc()


# In[ ]:
# Recommended for Production
#3rd option is to place the .py file in Lib/site-packages folder


# In[]
#have a folder and __init__.py inside that is called a package
#You can place this package one level inside current working directory
# or You can tells its path via sys.path
# or you can add package to site-packages

# __all__ is just a convenience to handle
# from module import * 
# only modules i.e  .py files mentioned 
# in __all__ will be given to import *
# but if you know its name of module you can use it anyway

#import mycustompackage.dependency1
#mycustompackage.dependency1.function1()

from mycustompackage import *
dependency1.function1()
#dependency2.function2() # gave error 

from mycustompackage import dependency2
dependency2.function2() # Worked
