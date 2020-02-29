
class Vector:

    def __init__(self, obj):

        self.items = []
        for item in obj:
            self.items.append(item)

    def __add__(self, other):

        if len(self.items) != len(other.items):

            print("Len ERROR")
            return self

        res = Vector([])
        for i in range(len(self.items)):

            res.items.append(self.items[i] + other.items[i])
        return res

    def __sub__(self, other):

        if len(self.items) != len(other.items):

            print("Len ERROR")
            return self

        res = Vector([])
        for i in range(len(self.items)):

            res.items.append(self.items[i] - other.items[i])
        return res

    def __mul__(self, other):

        if type(other) is Vector:

            if len(self.items) != len(other.items):

                print("Len ERROR")
                return self

            res = Vector([])
            for i in range(len(self.items)):

                res.items.append(self.items[i] * other.items[i])
            return res
        else:

            res = Vector([])
            for i in range(len(self.items)):

                res.items.append(self.items[i] * other)

            return res

    def __eq__(self, other):

        if len(self.items) != len(other.items):
            return False

        for i in range(len(self.items)):
            if self.items[i] != other.items[i]:
                return False
        return True

    def get_len(self):

        sum_of_elements = 0
        for i in range(len(self.items)):
            sum_of_elements += self.items[i]

        return sum_of_elements / len(self.items)

    def __getitem__(self, item):
        return self.items[item]

    def __str__(self):

        s = ""
        for i in self.items:
            s = s + str(i) + " "
        return s


def main():

    a = Vector([1, 2, 3])
    b = Vector([2, 3, 5])

    print("a=", a.items, sep='')
    print("b=", b.items, sep='')

    c = a + b
    print()
    print("a=", a.items, sep='')
    print("b=", b.items, sep='')
    print("c=", c.items, sep='')

    print()
    c *= a
    print("c=", c.items, sep='')

    print()
    c = c * 10
    print("c=", c.items, sep='')

    print("Vector a == Vector b?", a == b)
    print("Vector c == Vector c?", c == c)

    print()
    print("Len of C is", c.get_len())

    print()
    print("C[1]=", c[1], sep='')

    print()
    print("Str C=", str(c))


if __name__ == '__main__':
    main()
