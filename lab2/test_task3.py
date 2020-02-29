
from task3 import Vector


def test_3_1():

    a = Vector([1, 2, 3])
    b = Vector([2, 3, 5])

    c = a + b

    assert c.items == [3, 5, 8]


def test_3_2():

    a = Vector([1, 2, 3])
    c = a * 10

    assert c.items == [10, 20, 30]



