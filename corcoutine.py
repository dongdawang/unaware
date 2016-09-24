"""
生产者，消费者模型
"""
#生产者
def cou():
	r = '1'
	print('我被调用了！')
	while True:
		n = yield r
		if not n:
			return
		print('我消费了{0}'.format(n))
	return 'ok'
#消费者
def prod(c):
	m = c.send(None)
	print(m)
	n = 0
	while n<5:
		n += 1
		print('开始生产{0}'.format(n))
		m = c.send(n)
		print('消费了，返回了')
	c.close()

# c = cou()
# prod(c)

#asyncio
import asyncio

async def hello():
	print('hello world!')
	r = await asyncio.sleep(1)
	print('hello again!')

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()




