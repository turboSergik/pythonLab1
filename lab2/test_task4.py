
import os
# os.chdir("/home/sergey/PycharmProjects/pythonLabs. BSUIR 2020/lab2/")


from task4 import bin_pow


def test_4_1():

    t1 = bin_pow(2, 3)
    t2 = 8

    assert t1 == t2


def test_4_2():
    t1 = bin_pow(2, 10)
    t2 = 1024

    assert t1 == t2

