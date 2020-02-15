import random


def quick_sort(a):

    arr_size = len(a)
    if arr_size <= 1:
        return a

    low = []
    equal = []
    highs = []

    mid = random.randint(0, arr_size - 1)

    for i in a:
        if i < a[mid]:
            low.append(i)
        elif i == a[mid]:
            equal.append(i)
        else:
            highs.append(i)

    return quick_sort(low) + equal + quick_sort(highs)


def task_3(file_name):

    with open(file_name) as my_file:

        a = my_file.readline().replace('\n', '').split(" ")

    print("Before:             ", a)
    print("After:              ", quick_sort(a))

    a.sort()
    print("Sorted with python: ", a)

