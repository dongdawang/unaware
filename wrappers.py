def makebody(fn):
	def wrapper():
		return '<b>'+fn()+'</b>'
	return wrapper

@makebody
def hello():
	return 'hello'

print(hello())

#将参数传给装饰器
#这样需要在函数运行的过程中动态生成装饰器
def deco_maker(temp1,temp2):
	print('------------------'+temp1+'--'+temp2+'---------------')
	def deco(fn):
		print('fn已经传入')
		def wrapper():
			print('before fn.'+' '+temp1+' '+temp2)
			fn()
			print('after fn.'+' '+temp1+' '+temp2)
		return wrapper
	print('------------------'+temp1+'--'+temp2+'---------------')
	return deco

@deco_maker('ok','sola')
def hello():
	print('i am wrappered by deco function')

hello()
"""
产生的动作是：
hello = deco_maker('ok','sola')(hello)  hello()
"""