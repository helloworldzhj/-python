#-*-coding:utf-8-*-


'''
class Parent:
	def hello(self):
		print('正在调用父类hello方法。。。')

class Child(Parent):
	pass

p = Parent()
p.hello()

c = Child()
c.hello()

class Child(Parent):
	def hello(self):
		print('正在调用子类的方法。。。')

c = Child()
c.hello()
'''

import random as r

class Fish:
	def __init__(self):
		self.x= r.randint(0,10)
		self.y= r.randint(0,10)
	def move(self):
		self.x -= 1
		print('my position is' ,self.x,self.y)

class Goldenfish(Fish):
	pass

class Crap(Fish):
	pass

class Salmon(Fish):
	pass

class Shark(Fish):
	def __init__(self):
#		Fish.__init__(self)#方法1
		super().__init__()#第二种方法
		self.hungry = True
	def eat(self):
		if self.hungry:
			print('吃货就想着吃')
			self.hungry = False
		else:
			print('这下子不饿了。。。')
'''
fish = Fish()
fish.move()
fish.move()
fish.move()
fish.move()

goldfish = Goldenfish()
goldfish.move()
goldfish.move()
goldfish.move()
goldfish.move()
'''

#shark = Shark()
'''
shark.eat()
shark.eat()
'''
#shark.move()#这里是会报错的，因为在shark里面又重写了init属性，父类的方法就被覆盖了。


#那接下来就会考虑如何多重继承，就是前面先定义两个类，a和b
#然后我就定义一个类c它继承a和b的里面的方法

class Base1:
	def fool1(self):
		print('我是1')

class Base2:
	def fool2(self):
		print('我是2')

class C(Base1,Base2):
	pass

c = C()
c.fool1()
c.fool2()


















