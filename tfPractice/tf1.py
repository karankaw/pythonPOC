import tensorflow as tf

tensor1 = tf.constant([1,2,3,4,5,6], shape=[2,3], dtype=tf.int32)

with tf.Session() as session:
    op = session.run(tensor1)
    print(op)
    print(tensor1)
    print("type of evaluation of tensor",type(op))
    print("type of tensor",type(tensor1)) #
    print(isinstance(tensor1, tf.Tensor))
    print(tf.Tensor)