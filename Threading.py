import threading

class WinstonMessager(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = WinstonMessager(name='Send out messages')
y = WinstonMessager(name='Receive messages')
x.start()
y.start()