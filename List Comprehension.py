L1 = []
for x in range(10):
    L1.append(x*3)

# List Comprehension
L2 = [x**2 for x in range(10)]

print(L1)
print(L2)

xl = [1, 3, 5]
yl = [9, 12, 13]
L3 = [a for (a, b) in zip(xl, yl) if b > 10]
print(L3)