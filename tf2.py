# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:01:11 2018

@author: 10640691
"""

import tensorflow as tf

tensor1 = tf.constant([1,2,3,4,5,6], shape=[2,3], dtype=tf.int32)
tensor2 = tf.constant([1,2,3,4,5,6], shape=[3,2], dtype=tf.int32)


result = tf.matmul(tensor1, tensor2)

with tf.Session() as session:
	o_p = session.run(result)
	print(type(o_p))
