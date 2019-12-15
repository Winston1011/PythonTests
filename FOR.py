foods = ['bacon', 'tuna', 'ham', 'sausages', 'beef']
a = '1'
if a is '1':
    for i in foods[:2]:
        print(i)
        print(len(i))
else:
    for i in foods[:-2]:
        print(i)
        print(len(i))