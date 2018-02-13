# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:01:36 2018

@author: 10640691

placeholder

"""

import tensorflow as tf

x = tf.placeholder(tf.int32, shape = [2,3])
y = tf.placeholder(tf.int32, shape = [3,2])

x1 = tf.random_uniform([2,3], dtype=tf.int32, maxval=10)
y1 = tf.random_uniform([3,2], dtype=tf.int32, maxval = 100)

op = tf.matmul(x,y)

with tf.Session() as sess:
    
    xip = sess.run(x1)
    yip = sess.run(y1)
    print(xip)
    print(yip,"\n-----------------------------")
    print(sess.run(tf.matmul(xip,yip)),"\n-----------------------------")
    print(sess.run(op,feed_dict={x:xip, y:yip}))
    
    