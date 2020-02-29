import pprint as pp


def list_to_json(obj, type_of_obj):
    
    if type_of_obj is tuple:
        res = "("
    else:
        res = "["

    flag = False
    for item in obj:

        if flag is True:
            res = res + ', '
        flag = True

        if type(item) is str:

            res = f'{res}"{item}"'
        elif type(item) is int:

            res = f'{res}{item}'
        elif type(item) is list:

            res = res + " " + list_to_json(item)
        elif type(item) is dict:

            res = res + to_json(item)
        else:

            print("WRONG OBJ!")
            exit(0)

    if type_of_obj is tuple:
        res = res + ")"
    else:
        res = res + "]"

    return res


def to_json(obj):
    res = "{"

    flag = False
    for item in obj.items():

        if flag is True:
            res = res + ', '
        flag = True

        res = f'{res}"{item[0]}":'
        temp = item[1]

        if type(temp) is list or type(temp) is tuple:

            res = res + " " + list_to_json(temp, type(temp))
        elif type(temp) is str:

            res = f'{res} "{temp}"'
        elif type(temp) is int:

            res = f'{res} {temp}'
        elif type(temp) is dict:

            res = res + " " + to_json(temp)
        else:

            print("WRONG OBJ!")
            exit(0)

    return res + "}"


def main():
    a = {"a1": ({"a": ("b1", "b1", "b2"), "c": 228}, {"a1": 322, "c1": "d1"}, "f"), "b1": [1, 2, 1488]}
    b = to_json(a)

    print("b =", b)
    print("type=", type(b), sep="")


if __name__ == "__main__":
    main()

"""
{
"a1" : {"a":"b"}, 
"b1" : [1, 2, 3]
}

"""
