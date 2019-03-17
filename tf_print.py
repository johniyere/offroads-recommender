import tensorflow as tf

def tf_print(val):
    init_g = tf.global_variables_initializer()
    init_l = tf.local_variables_initializer()
    with tf.Session() as sess:
        sess.run(init_g)
        sess.run(init_l)
        result = sess.run(val)
        print(result)