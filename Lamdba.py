answer = lambda x: x**3
print(answer(5))

func = lambda x, y: x + y
print(func(3, 4))

re1 = map((lambda x: x*2), [1, 3, 5, 6])

re2 = map((lambda x, y: x**2+y), [1, 2, 3], [6, 7, 9])

for i in re1:
    print(i)

for i in re2:
    print(i)