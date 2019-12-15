classmates = {'Tony': ' cool but smells', 'Emma': ' sits behind me', 'Lucy': ' asks too many questions'}
dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

print(classmates)
print(classmates['Emma'])
print(dic)
print(dic['A'])
print(dic.keys())
print(dic.values())
print(dic.items())

for k, v in classmates.items():
    print(k + v)


for a, b in dic.items():
    print(a, b)

# default: dic == dic.keys()
for key in dic:
    print(key)