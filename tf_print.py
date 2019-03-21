# Adapted from this code: 
# https://gist.github.com/vihari/f9b361058825e16d390f0e443bfdffc7
# https://stackoverflow.com/questions/49012912/error-when-calling-global-variables-initializer-in-tensorflow 
# https://danijar.com/what-is-a-tensorflow-session/
import tensorflow as tf

def tf_print(val):
    init_g = tf.global_variables_initializer()
    init_l = tf.local_variables_initializer()
    with tf.Session() as sess:
        sess.run(init_g)
        sess.run(init_l)
        result = sess.run(val)
        print(result)