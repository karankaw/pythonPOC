import tensorflow as tf

def add_layer(input_, num_ip, num_op, activation_func):
#    weights is num_ip*num_op tensor ??? not numpy array ??
#    if tensor, then Variable or constant, Variable because it needs to be changed
#    What to initialize, Random of Tf, tf.random_normal() - float wala
    weights = tf.Variable(tf.random_normal([num_ip,num_op]))
    
   
#    Multiply Input and weights, Input is 1-D and weights is 2-D
#    It has to be 2 D like or 1 D [1, 3] or just [3]
    
    matmul = tf.matmul(input_, weights)
    
    return matmul
    

input_data = tf.placeholder(tf.float32,shape=[1,3],name='input') 
#input_data = tf.placeholder(tf.float32,shape=[3],name='input')   
op = add_layer(input_data,3,5,None)

with tf.Session() as session:
#    input_list = [1., 2., 3.]
    input_list = [[1., 2., 3.]]
    
#    session.run(tf.initialize_all_variables())   
    session.run(tf.global_variables_initializer())
#    matmul_result = session.run(add_layer(input_data,3,5,None),feed_dict={input_data: input_list})
    matmul_result = session.run(op,feed_dict={input_data: input_list})
    print(matmul_result)
    
    
    


'''
tf.initialize_all_variables
tf.global_variables_initializer

WARNING:initialize_all_variables is deprecated and will be removed after 2017-03-02.
Use `tf.global_variables_initializer` instead.


tf.local_variables_initializer()
'''