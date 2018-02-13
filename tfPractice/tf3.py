# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:01:18 2018

@author: 10640691
"""
import tensorflow as tf

t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
print(repr(tf.rank(t)))
ip_tensor_no_deviation = tf.random_normal([2,3], mean=10, stddev=0)
ip_tensor_deviation = tf.random_normal([2,3], mean=10, stddev=1)
print(tf.rank(ip_tensor_no_deviation))
print(tf.rank(ip_tensor_deviation))
    

with tf.Session() as session:
    ip_nd = session.run(ip_tensor_no_deviation)
    print(ip_nd)
    mean_calculate_tensor = tf.reduce_mean(ip_nd)
    mean = session.run(mean_calculate_tensor)
    print(mean)  
   
    ip_d = session.run(ip_tensor_deviation)
    print(ip_d)    
    mean_calculate_tensor = tf.reduce_mean(ip_d)
    mean = session.run(mean_calculate_tensor)
    print(mean)
    
    print(repr(tf.rank(t)))
    print(str(session.run(tf.rank(t))))
    