def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

winstons_limit = allowed_dating_age(21)
print("Winston can date girls", winstons_limit, "or older")