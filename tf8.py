# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:06:16 2018

Multiple eval inside 

@author: 10640691
"""

import tensorflow as tf
import numpy as np

var1 = tf.Variable(initial_value=tf.random_uniform([3], dtype=tf.int32, maxval=5))
var2 = tf.constant(123, dtype=tf.int32, shape=[1])
var3 = np.array(np.random.rand(2,3))

var4 = tf.convert_to_tensor(var3) #numpy_arr converted to tensor
var5 = tf.convert_to_tensor(0)    #scalar converted to Tensor
var6 = tf.convert_to_tensor(var2)

print(var3)
print(var4)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    #Multiple Variables fetched and run together, they return numpy 
    print(type(sess.run(var2)))
    print(sess.run([var1, var2]))
    print(var5)
    print(var6)


print(var2.eval(session=tf.Session()))

listu = [[1,2,3]] # 2 Dimensional - 2 Square Brackets
# can be handled by listu[0][2]