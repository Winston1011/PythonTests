def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)

    print(first)
    print(avg)
    print(last)

drop_first_last([65, 76, 98, 54, 21])

drop_first_last([31, 53, 54, 56, 76, 83, 34])