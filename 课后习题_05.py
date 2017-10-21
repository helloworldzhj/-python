#-*-coding:utf-8-*-

'''

bool
int向下取整
round对数字四舍五入
ceil向上取整
分别取整和取小数部分 modf()返回一个元组

1.type可以只接收一个参数，打印其未知的所属的类型；而isinstance只能判断是否属于某个已知类型
2.isinstance可以判断子类对象是否继承自父类；而type不可以
总结来说type主要用于获取未知变量的类型
isinstance主要用于判断a类是否继承于b类

python3源码文件默认使用utf-8编码，也就支持中文了，这就使得以下代码是合法的
小甲鱼 = '我爱你'
print（小甲鱼）
我爱你



temp = int(input('请输入一个整数：'))
if temp % 4 == 0 and temp % 100 != 0:
	print('这是闰年')
else:
	print('这不是闰年')



if temp/400 == int(temp/400)


'''













































