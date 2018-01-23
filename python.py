# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 16:49:31 2017

@author: 10640691
"""




print(__name__)
print(__file__)
print("-----------------------------------------------------")



import tensorflow as tf
import numpy as np
import nltk as toolkit
import sklearn as scikitlearn

print(tf.__version__)

print("A word","followed by space")
def a_func():
    """    
    Okay, Help function    
    """
    print('Hola')


list = ['jeff', 'samantha', 'joe', 'shelby']
tuple = ('jeff', 'samantha', 'joe', 'shelby')
print(type(tuple[:]))
print(type(list[:]))
print("Begin")
print(a_func.__doc__)
print("End")



class Abc():
    def __init__(self):
        print("Abc Made")
       
    def __str__(self):
        return "Abc in str"
    
    def __repr__(self):
        return "Abc in repr"
    
abc = Abc()

print(abc)
print(repr(abc))

print(Abc)
print(repr(Abc))
