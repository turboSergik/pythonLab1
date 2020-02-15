
def task_1(file_name):

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

    for key, value in dictionary.items():
        print("key=", key, " count=", value, sep="")


