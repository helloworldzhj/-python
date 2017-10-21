#-*-coding:utf-8-*-

import pickle
import os
os.chdir('C:/Users/Administrator/Desktop')
my_list = [123,3.14,'小甲鱼',['another list']]
pickle_file = open('my_list.pkl','wb')
pickle.dump(my_list,pickle_file)
#把数据像倒到缸里面一样倒进去,并且是以二进制存储的。
# notepad++是以文本的形式读取的，所以是乱码
# 如果用二进制形式打开，就可以看到没内容了
pickle_file.close()

pickle_file = open('my_list.pkl','rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)



























