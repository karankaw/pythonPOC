from module2 import callMe2
print('Current name : {file_name}'.format(file_name=__name__))
callMe2()

#from submodule import *
from submodule import module1
module1.callMe1()

from submodule.module1 import  callMe11
callMe11()