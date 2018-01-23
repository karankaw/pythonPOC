# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:02:00 2018

@author: 10640691

tf.Variable
tf.initialize_all_variables
tf.initialize_variables[[]]

tf.get_variable(name, shape, dtype=None, initializer=tf.constant([23,32]))
Behavior depends on whether variable reuse enabled
RNN - Recurrent Neural Network

tf.global_variables_initializer())

tf.get_variable(name, shape, dtype, initializer=tf.constant)

You need to set some variables while declaring

You need to initialize variable, thawing them back to life

You can also use reassign value to variable using tf.assign function reference, new_value
"""

import tensorflow as tf

un_init_variable = tf.Variable(True)

special_variable = tf.get_variable("ma_special_variable16", [2], dtype=tf.float32)
hmm = tf.random_normal([2], dtype = tf.float32, mean=5)
res = special_variable + hmm

variable1 = tf.Variable(123, name="variable1", dtype=tf.float32)
print(variable1.name)
print(type(variable1))
print(isinstance(variable1, tf.Tensor))
variable2 = tf.Variable(1., name="variable2")

cnst = tf.constant(123, dtype=tf.int32, shape=[2*3])
#print(type(cnst))
#print(isinstance(cnst, tf.Tensor))

#result = tf.add(cnst, variable1)
sum_result = tf.add(variable1, variable2)
final_result = tf.assign(variable1, sum_result)#ref, value
#print(type(result))

init = tf.initialize_all_variables()
#init = tf.initialize_variables([variable1])

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    
    a = sess.run(special_variable)
    b = sess.run(hmm)
    print(a)
    print(b)
    print(a + b)
   
    for _ in range(5):
#   sess.run(init)
        output =  sess.run(final_result)
        print(output)
    
    
