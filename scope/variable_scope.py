from __future__ import print_function
import tensorflow as tf
tf.set_random_seed(1)	# reproducible


with tf.variable_scope("a_variable_scope") as scope:
	initializer = tf.constant_initializer(value=3)
	var3 = tf.get_variable(name='var3', shape=[1], dtype=tf.float32, initializer=initializer)
	scope.reuse_variables()		# reuse
	var3_reuse = tf.get_variable(name='var3')

	var4 = tf.Variable(name='var4', initial_value=[4], dtype=tf.float32)
	var41 = tf.Variable(name='var4', initial_value=[4.1], dtype=tf.float32)
	

with tf.Session() as sess:
	if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
		init = tf.initialize_all_variables()
	else:
		init = tf.global_variables_initializer()
	sess.run(init)
	print(var3.name)
	print(sess.run(var3))
	print(var3_reuse.name)
	print(sess.run(var3_reuse))

	
	print(var4.name)
	print(sess.run(var4))
	print(var41.name)
	print(sess.run(var41))
	
