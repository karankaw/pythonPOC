# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:01:11 2018

@author: 10640691
"""



import tensorflow as tf
tf1Constant = tf.constant(dtype=tf.int32, value=123)

print(tf1Constant)

def openfunc(name=None, pos_default=None):
    print(pos_default, name)
    
    
def func(name, burra, pos):
    print(pos, name)
    print(burra)
    
