class Person():
    def __init__(self, name):
        self.name = name
        print("Person Initialised")
        
class Employee(Person):
    def __init__(self):
#        Person.__init__(self)
        super().__init__("Hmmm OK")
        print("Employee Initialised")
     
e = Employee()
print("MRO :",e.__class__.mro())

print(Employee.__module__)
print(__file__)

class ModuleError(Exception):
    def __init__(self, msg=None):
#        super(ModuleError, self).__init__(msg)  
        super().__init__(msg) 
    def __str__(self):
        return super().__str__()+"Corey Schafer"

dividend = 6
divisor  = 0
try :
    res = dividend/divisor;
except (ValueError, TypeError, ZeroDivisionError,) as hmm:
    print("I caught a zero divisor"+hmm.__class__.__name__)
    print(hmm.args[0])
    try:
        raise ModuleError
    except (Exception,) as e:
        print("************************")
        print(e)
        print("e.args   : "+e.args.__str__())
        print(e.__class__.__name__)
        print(e.__cause__)
else:
    print("Divison completed sucessful")
finally :
    print("Method Done!")
 
    



