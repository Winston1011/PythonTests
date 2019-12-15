first = ['Winston', 'Tom', 'Taylor']
last = ['DZ', 'Hanks', 'Swift']

ta = [1,2,3]
tb = [9,8,7]

# cluster
zipped = zip(ta,tb)
print(zipped)
# decompose
na, nb = zip(*zipped)
print(na, nb)

names = zip(first, last)

for a, b in names:
    print(a, b)

# nc, nd = zip(*names)
# print(nc, nd)
