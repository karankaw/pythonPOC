'''
This python file tells us how to work with
positional arguments - optional/default arguments
arbitary arguments
keyword arguments

how to handle named argument (applicable while calling method only )

This Has 2 Modes
Calling a Method
and
Defining a Method

Some Caveats apply while defining while some rules have to be respected while calling some
'''

def func(p1, p2, op1='op1', op2="op2", *args, **kwargs):
    print('positional args')
    print(p1)
    print(p2)
    print(op1)
    print(op2)
    
    print('*args')
    print(args)
    for arg in args:
        print(arg)
    
    print('**kwargs')
    print(kwargs)
    for arg in kwargs:
        print(arg)
        

# ------------------------------------------------------
# dictionary = {'key1': 'val1', 'key2': 'val2'}
# keyword arg has no such Expression in keyName

# Order of method definition should be 
# positional_args, *args, **kwargs
# *args are tuple
# **kwargs are dict
    
# Only Positional arguments can have default values making them as optional

# While Calling method
# positional arguments cannot follow keyword arguments
    
# Named Arguments , While calling a method
# func(p2='p2',p1='p1') 

# func(1, 2, 3)
# func(1, 2, op2='OverideDefaultOp2')
    
# Complicated Usages
# func(1,2,3,4,  5,6,   key1='val1', key2='val2') #Valid
# 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    