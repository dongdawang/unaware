"""
    异步扫描
"""
import socket
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector = DefaultSelector()


class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)

    def __iter__(self):
        yield self
        return self.result


def connect(sock, address):
    f = Future()
    sock.setblocking(False)
    try:
        sock.connect(address)
    except BlockingIOError:
        pass

    def on_connected():
        print(">> {}连接成功".format(address[0]))
        f.set_result(None)

    selector.register(sock.fileno(), EVENT_WRITE, on_connected)
    yield from f
    selector.unregister(sock.fileno())


class Crawler:
    def __init__(self, ip):
        self.ip = ip
        self.response = b''

    def fetch(self):
        sock = socket.socket()
        yield from connect(sock, (ip, 21))


class Task:
    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            next_future = self.coro.send(future.result)
        except StopIteration:
            return
        next_future.add_done_callback(self.step)

ips = ["192.168.145."+str(i) for i in range(0, 120)]

def loop():
    # for ip in ips:
    events = selector.select(timeout=2)
    for event_key, event_mask in events:
        callback = event_key.data
        callback()


if __name__ == '__main__':
    import time
    start = time.time()

    for ip in ips:
        crawler = Crawler(ip)
        Task(crawler.fetch())
    loop()
    print(time.time() - start)
