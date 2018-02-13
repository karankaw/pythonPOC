# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:01:29 2018

@author: 10640691
"""



import tensorflow as tf

t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
ip_tensor_no_deviation = tf.random_normal([2,3], mean=10, stddev=0)
ip_tensor_deviation = tf.random_normal([2,3], mean=10, stddev=1)

with tf.Session() as session:
    pass