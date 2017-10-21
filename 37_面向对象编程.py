'''
class Ball:
	def setName(self,name):
		self.name = name
	def kick(self):
		print('我叫%s，该死的，谁踢我。。。' % self.name)

a = Ball()
a.setName('球A')
b= Ball()
b.setName('球B')
c = Ball()
c.setName('土豆')

a.kick()
b.kick()
c.kick()
'''

#__init__(self)我们称之为构造方法

'''
class Ball:
	def __init__(self,name):
		self.name = name
	def kick(self):
		print('我叫%s，该死的，谁踢我。。。' % self.name)

b = Ball('土豆')
b.kick()
c = Ball()
c.kick()
'''
#这样的话就会出现错误了，因为我们没有给它里面传递参数，这样的话她就会报错，说它需要传递一个参数。

#然后接下来就区分一下
'''
class Person:
	name = '朱华建'

p = Person()
print(p.name)
'''
#那么这儿就涉及到'name mangling'(名字改编，名字重整。)
#在python中定义私有变量就只需要在变量名或者函数名前加上'__'两个下划线，那么这个函数或者变量就变为私有的了。

'''
class Person:
	__name = '朱华建'

p = Person()
print(p.__name)
print(p.name)
'''
#因为他们都找不到了

class Person:
	__name = '朱华建'
	def getName(self):
		return self.__name

p = Person()
#print(p.name)
#print(p.__name)
print(p.getName())
print(p._Person__name)























