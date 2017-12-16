import tensorflow as tf
import numpy as np

## Save to file
# remember to define the same dtype and shape when restore
W = tf.Variable([[1,2,3],[3,4,5]],dtype=tf.float32,name='weights')
b = tf.Variable([[1,2,3]],dtype=tf.float32,name='biases')

if int((tf.__version__).split('.')[1] < 12 and int(tf.__version__).split('.')[0] < 1):
	init = tf.initialize_all_variables()
else:
	init = tf.global_variables_initializer()

saver = tf.train.Saver()

with tf.Session() as sess:
	sess.run(init)
	save_path = saver.save(sess,"my_net/save_net.ckpt")
	print "Save to path:"  ,save_path


# restore variable
# redefine the same shape and same type for variables
W_out = tf.Variable(np.arange(6).reshape((2, 3)), dtype=tf.float32, name="weights")
b_out = tf.Variable(np.arange(3).reshape((1,3)),dtype = tf.float32,name='biases')

# not need init step
init = tf.global_variables_initializer()

saver = tf.train.Saver()
with tf.Session() as sess:
	sess.run(init)
	saver.restore = (sess,"my_net/save_net.ckpt")
	print "weights:"	,  sess.run(W_out)
	print "biases:"    ,  sess.run(b_out)




