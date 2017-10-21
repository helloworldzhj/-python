#-*-coding:utf-8-*-

'''
while 'C':
	print('我爱鱼')
无数次


i = 10
while i:
	print('我爱鱼')
	i -= 1

cost>10 and cost<50



cost>10 and cost<50

python3中，可以输写多个语句。
python3中，一个语句可以分成多行书写




'''

'''

'''




'''

1.字符串和数据类型可以直接输出
print(1)
print('hello,world.')

2.变量
无论什么类型，数值，布尔，列表，字典。。。都可以直接输出
x = 12
print(x)
s = 'hello'
print(s)
l = [1,2,3,'sda0',"rqwerqw"]
print(l)
t = (1,2,3,'asdf',"uiyruireo")
print(t)
d = {'name':'zhuhajian','a':4564}
print(d)



3.格式化输出类似于c的printf
s = 'hello'
x = len(s)
print("the length of %s is %d" % (s,x))
这个用%xxx来代替数据的就叫格式化输出

看看官方解释：
1.%字符：标记转换说明符的开始
2.转换标志：-表示左对齐；+表示在转换值之前要加上正负号；""(空白字符)表示证书之前保留空格；0表示转换至若位数不够则用0填充
3.最小字段宽度：转换后的字符串至少应该具有制定的宽度。如果是*，则宽度会从值元组中读出。
4.点.后跟精度值：如果转换后的是实数，精度值就表示出现在小数点之后的位数。如果转换后的是字符串，那么给数字就表示最大字段宽度。如果是*，那么精度将从元组中读出
5.字符串格式化转换类型

pi = 3.141592653
print('%10.3f' % pi)
#字段宽10，精度为3
print('pi = %.*f' % (3,pi))
#用*从后面的猿族中读取字段宽度或精度
print('%010.3f' % pi)
#用0填充空白
print('%-10.3f' % pi)
#左对齐
print('%+f' % pi)
#显示正负号


4.如何让print不换行呢？比如下面这个例子，就是每次自动换行的，

for x in range(0,10):
	print(x)

for x in range(0,10):
	print(x,end='')



拼接字符串;



x = 'hello'
y = 'world'
print(x+y)


pow函数：




print(pow(2,3,5))





import random
times =3
secret = random.randint(1,10)
print('----------我是朱华建----------')
guess = 0
print('猜一下我在想什么数字吧。。。',end=" ")
while (guess != secret) and (times>0):
	temp = input()
	guess = int(temp)
	times = times-1
	if guess == secret:
		print("我擦，你是肚子里面的蛔虫吗？")
		print("猜中了也没卵用。。。")
	else:
		if guess>secret:
			print("bigger")
		else:
			print('small')
		if times>0:
			print('再试一次吧',end="")
		else:
			print('机会用光了')
print("机会用完了")



temp = input('请输入一个整数')
num = int(temp)
i = 1
while num:
	print(i)
	i = i + 1
	num = num - 1


temp = input('请输入一个整数：')
num = int(temp)
while num:
	i = num - 1
	while i:
		print(' ',end='')
		i = i - 1
	j = num
	while j:
		print('*',end='')
		j = j - 1
	print()
	num = num - 1

'''



































































































































































