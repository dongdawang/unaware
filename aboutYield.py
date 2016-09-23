#关于yield的一点重新学习
"""
在学习yield之前先了解python中的迭代器和生成器。两者都是可迭代对象
python的可迭代对象包括：一、集合数据类型，list,tuple,dict,set,str
					  二、generator，包括生成器和带yield的function
"""
#迭代器Iterator和可迭代对象Iterable
#list,tuple,dict,set,str是Iterable，但不是Iterator，原因是Iterator可以无穷，而list等不是无穷的

#可迭代对象都可以使用for循环来遍历
ls = [1,2,3,4,5]
for i in ls:
	print(i)
#判断是否是可迭代对象：Iterable
from collections import Iterable
print(isinstance(ls,Iterable))

#列表生成式
ls1 = list(range(10))
print(ls1)
ls2 = [x for x in range(10)]
print(ls2)
ls2 = [x*x for x in range(10) if x%2==0]
print(ls2)
ls = [x.upper() for x in ['adad','dawda','dwafwa']]
print(ls)

#generator
"""
generator和其他可迭代对象不一样的是，其他可迭代对象一创建，则其中的所有元素都生成并存在内存中，
而generator则根据特定的推导式，调用一次返回一个推导出来的结果。
用处是：
有时候数据很大，而且只需要读取使用一次，这样就可以使用generator，使用的时候在调用。
"""
##生成器：仅仅将列表生成式的中括号[]改成()
#generator可以使用next()函数调用，但是当generator中没有元素了，就会报异常
#所以使用for循环的优点就是不用考虑报异常
ls = (x for x in range(10))
print(ls)
for x in ls:
	print(x,end='--')
print()
#带有yield的函数
def gen(n):
	i = 0
	while i<10:
		yield i
		i += 1
	return 'have no items.'
for i in gen(10):
	print(i,end='--')
print()
"""
yield函数和普通函数不一样的是程序运行到yield时，会中断并返回yield的元素，在运行时是从yield处运行
，也就是说从以前中断的地方继续运行。
"""
#generator版杨辉三角
def tri():
	ls = [1]
	while True:
		yield ls
		ls.append(0)
		ls = [ls[i-1]+ls[i] for i in range(len(ls))]
	return 'stop!'
index = 0
for i in tri():
	print(i)
	index += 1
	if index > 10:
		break


