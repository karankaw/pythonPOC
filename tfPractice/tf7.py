'''

'''

import tensorflow as tf
import numpy as np
import os

var = tf.Variable([1,2,3])
scalar  = 100
const = tf.constant(50)
#placebo = tf.placeholder(tf.int32,shape=[3])    #Works
#placebo = tf.placeholder(tf.int32,shape=None)   #Works
#placebo = tf.placeholder(tf.int32,shape=[None]) #Works
placebo = tf.placeholder(tf.int32,shape=[])      #ain't work with non-scalar
add = placebo + var

#tf.convert_to_tensor
listu = [0, 7, 4]
nparr = np.array(listu)
print(type(listu))
print(type((tf.convert_to_tensor(listu))))
print(type(nparr))

#add_layer
def add_layer(input, inp_size, op_size, activation_func):
    pass

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    param = sess.run(tf.random_uniform([3], dtype=tf.int32, maxval=5))
    print(param)
    #result  = sess.run(add, feed_dict={placebo: param})
    #result  = sess.run(add, feed_dict={placebo: scalar}) # Works with PH-shape[]
    #result  = sess.run(add, feed_dict={placebo: const})  # aint work tf.Tensor and PH-shape []
    result  = sess.run(add, feed_dict={placebo: sess.run(const)}) # sess.run() Works!! with PH-shape []
    print(result)
    
print(os.path.dirname(os.path.realpath(__file__)))
    