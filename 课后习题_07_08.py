#-*-coding:utf-8-*-

'''
if money>=100:

assert这个关键字称为断言，当这个关键字后面的条件为假的时候，程序自动崩溃并且抛出assertionerror的异常
当我们测试程序的时候就很好用，因为与其让错误的条件导致程序今后莫名其妙地崩溃，不如在错误条件出现的那一瞬间就自爆。
一般来说我们可以用Ta再程序中置入检查点，当需要确保程序中的某个条件一定为真才能让程序正常工作的话，assert关键字就非常有用了。

在python中

x=1
y=2
z=3
x,y,z=z,x,y
print(x,y,z)


for i in range(10):
	print(i)

score = int(input('请输入一个分数：'))
if 80 > score >= 60:
    print('C')
elif 90 > score >= 80:
    print('B')
elif 60 > score >= 0:
    print('D')
elif 100 >= score >= 90:
    print('A')
else:
    print('输入错误！')


small = x if (x < y and x < z) else (y if y < z else z)
small = x if (x < y and x < z) else (y if y < z else z)





'''

























