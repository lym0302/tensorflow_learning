from __future__ import print_function
import tensorflow as tf
tf.set_random_seed(1)	# reproducible


with tf.name_scope("a_name_scope"):
	initializer = tf.constant_initializer(value=1)
	var1 = tf.get_variable(name='var1', shape=[1], dtype=tf.float32, initializer=initializer)
	var2 = tf.Variable(name='var2', initial_value=[2], dtype=tf.float32)
	var12 = tf.get_variable(name='var2', shape=[1], dtype=tf.float32, initializer=initializer)
	var21 = tf.Variable(name='var2', initial_value=[2.1], dtype=tf.float32)


with tf.Session() as sess:
	if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
		init = tf.initialize_all_variables()
	else:
		init = tf.global_variables_initializer()
	sess.run(init)
	print(var1.name)
	print(sess.run(var1))
	print(var2.name)
	print(sess.run(var2))
	print(var12.name)
	print(sess.run(var12))
	print(var21.name)
	print(sess.run(var21))
