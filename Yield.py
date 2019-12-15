def gen2():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000

def gen1():
    for i in range(4):
        yield i

for x in gen1():
    print(x)

for y in gen2():
    print(y)


G = (_ for _ in range(4))
for i in G:
    print(i)

