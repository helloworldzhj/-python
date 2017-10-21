#-*-coding:utf-8-*-

'''
for i in range(0,10,2):
	print('我爱你')


for i in 5:
	print('我爱你')
	#这样的话会报错的

break会跳出当前循环,continue就是程序继续运行下去

列表可变

range(10)-----0.1.2.3.4.5.6.7.8.9

while True:
    while True:
        break
        print(1)
    print(2)
    break
print(3)
#打印2和3

while True:循环体
同样用于游戏实现，因为只要游戏运行着，就需要是可接受用户输入，因此可以永远为真确保游戏在线。操作系统也是同样的道理，时刻待命，操作系统永远为真的这个循环叫做消息循环。另外很多通讯服务器的客户都拿服务器系统也是通过这样的原理来工作的。







'''
'''

count = 3
init_pw = '123456'

while count:
	my_pw = input('请输入你的密码：')
	if my_pw == init_pw:
		print('密码正确，欢迎光临')
		break
	elif '*' in my_pw:
		print('密码中不能含有‘*’号，请重新输入，您还有',count,'次机会。',end = ' ')
		continue
	else:
		print('密码输入有误！您还有',count-1,'次机会！',end=' ')
	count -= 1
'''
'''`

count = 3
password = 'FishC.com'

while count:
    passwd = input('请输入密码：')
    if passwd == password:
        print('密码正确，进入程序......')
        break
    elif '*' in passwd:
        print('密码中不能含有"*"号！您还有', count, '次机会！', end=' ')
        continue
    else:
        print('密码输入错误！您还有', count-1, '次机会！', end=' ')
    count -= 1

'''

'''

for i in range(100,1000):
	a = str(i)
	if i == int(a[0])**3+int(a[1])**3+int(a[2])**3:
		print(i)



for i in range(100, 1000):
	sum = 0
	temp = i
	while temp:
		sum = sum + (temp%10) ** 3
		temp //= 10         # 注意这里要使用地板除哦~
	if sum == i:
		print(i)
'''

'''
for i in range(4):
	for j in range(4):
		for k in range(7):
			if i+j+k==8:
				print(i,j,k)
'''

print('red\tyellow\tgreen')
for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                # 注意，下边不是字符串拼接，因此不用“+”哦~
                print(red, '\t', yellow, '\t', green)
































































































































































