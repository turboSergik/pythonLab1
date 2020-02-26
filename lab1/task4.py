
def merge_sort(a):

    arr_size = len(a)
    if arr_size <= 1:
        return a

    left = merge_sort(a[:arr_size // 2])
    right = merge_sort(a[arr_size // 2:])

    point_left = 0
    point_right = 0
    result = []

    while point_left < len(left) or point_right < len(right):

        if point_left == len(left):
            result.append(right[point_right])
            point_right += 1

        elif point_right == len(right):
            result.append(left[point_left])
            point_left += 1

        else:

            if left[point_left] < right[point_right]:
                result.append(left[point_left])
                point_left += 1
            else:
                result.append(right[point_right])
                point_right += 1

    return result


def task_4(file_name):

    with open(file_name) as my_file:
        a = my_file.readline().replace('\n', '').split(" ")

    print("Before:             ", a)
    print("After:              ", merge_sort(a))

    a.sort()
    print("Sorted with python: ", a)


