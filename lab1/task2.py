
def task_2(file_name):

    with open(file_name) as my_file:
        s = my_file.read()

    s = s.replace("\n", " ")
    s = s.replace(".", "")
    s = s.replace(",", "")

    words = s.split(" ")
    dictionary = {}

    for word in words:

        if len(word) == 0:
            continue

        if dictionary.get(word) is None:
            dictionary[word] = 0

        dictionary[word] += 1

    sorted_dict = {k: v for k, v in sorted(dictionary.items(), key=lambda item: -item[1])}

    _count = 0
    for word in sorted_dict.keys():
        print(word, end=" ")

        _count += 1
        if _count == 10:
            break

    print()