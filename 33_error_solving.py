#-*-coding:utf-8-*-

'''
file_name = input("请输入你想要打开的文件的名字：")
f = open(file_name)
print('文件的内容是：')
for each_line in f:
	print(each_line)
'''

try:
	f = open('我为什么是一个文件.txt')
	print(f.read())
	f.close()
#except OSError as reason:
#	print('打开出错啦。。。\n错误的原因是：'+str(reason))
except:
	print('chucuola')
