# -*- coding: utf-8 -*-
"""Tensorflow example ,Constant_PlaceHolder_Variable

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PrgqhBrpzB1UbyOQazPP0G2YGfzkWDgX
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 1.x
 import tensorflow as tf

#CONSTANT

 c1 = tf.constant(10)
c2 = tf.constant(3.14)
c3 = tf.constant("sahuji")
c4 = tf.constant(False)
#print([c1,c2,c3,c4])
sess = tf.Session()
##sess = tf.compat.v1.Session
#print(tf.version)
#print(sess.run([c1,c2,c3,c4]))
add= tf.constant([1,2,3,4,5,6])+tf.constant([6,5,4,3,2,1])
m = tf.constant([1,2,3,4,5,6])*tf.constant([6,5,4,3,2,1])
#sess =tf.Session()
sess.run([add,m])

#PLACEHOLDER
a = tf.placeholder(tf.int32)
b = a*2
sess.run(b,feed_dict={a:[1,2,3,4,5]})
sn = tf.placeholder(tf.string)
snm = "i am sahu"+ sn
sess.run(snm,feed_dict={sn:["sahu","rahul","master"]})

#VARIBLE

var1 = tf.Variable([20],tf.int32)
init = tf.global_variables_initializer()
sess.run(init)
sess.run(var1)
updated_var1 =tf.assign(var1,[25])
sess.run(updated_var1)

#LINEAR_MODEL

p = tf.Variable([10],tf.int32)
q = tf.Variable([20],tf.int32)
r = tf.placeholder(tf.int32)
init =tf.global_variables_initializer()
linear_model = p*r+q 
sess.run(init)
sess.run(linear_model,feed_dict={r:[1,2,3,4,5]})