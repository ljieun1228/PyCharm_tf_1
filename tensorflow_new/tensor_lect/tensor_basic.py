import tensorflow as tf

var = tf.Variable([5.0], dtype=tf.float32)#기본형 float 정수사이 무한한 값 /대문자 : 생성자 var 는 생성자에 의해 만들어진 객체
con = tf.constant([10.0], dtype=tf.float32)#상수
session = tf.Session()#객체
init = tf.global_variables_initializer()#전역적으로 변수들을을초기화

session.run(init)#함수를 파라미터에 (콜백유사) 세션이 돌아갈 때

print(session.run(var*con))
print('>>>>>>>>>>>>>>>>>>')
session.run(var.assign([10.0]))
print(session.run(var))

p1 = tf.placeholder(dtype=tf.float32)
p2 = tf.placeholder(dtype=tf.float32)

t1= p1 * 3
t2= p1 * p2

session = tf.Session()

print(session.run(t1,{p1:[4.0]})) #print(session.run(t1,feed_dict={p1:[4.0]})) feed_dict 생략가능

print(session.run(t2,feed_dict={p1:4.0,p2:[2.0,5.0]})) #p2 행렬연산