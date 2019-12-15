
# add numbers as u wish
def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(3)
add_numbers(1, 2424)
add_numbers(5, 5342, 451)
add_numbers(5, 2, 41, 23, 242141)