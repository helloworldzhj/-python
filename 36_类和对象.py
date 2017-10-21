#-*-coding:utf-8-*-

class Turtle:
	clor = 'green'
	weight = 10
	legs = 4
	shell = True
	mouth = '大嘴'
	def climb(self):
		print('我在很努力的往前爬。。。')
	def run(self):
		print('我在很努力的往前跑。。。')
	def bite(self):
		print('咬死你咬死你。。。')
	def eat(self):
		print('有的吃真满足。。。')
	def sleep(self):
		print('困了睡了晚安。。。')
#上面这些就是封装了
tt = Turtle()
# print(tt.legs)
# tt.climb()
# tt.bite()

class MyList(list):
	pass
list2 = MyList()
#这样也就生成了一个这样的列表实例，这个实例继承了list的所应该拥有的所有的东西。
#比如说append(),sort()都可以使用。

#这就是继承了啊
class A:
	def fun(self):
#python的self就相当于c++的this指针。
		print('我是小A。。。')
class B:
	def fun(self):
		print('我是小B。。。')

a = A()
b = B()
a.fun()
b.fun()
#这边的话同样是fun函数，但是输出的结果是不一样的，这就说明这是多态


















