
from task2 import to_json


def test_2_1():

    a = {"a": "b", "c": "d"}

    t1 = to_json(a)
    t2 = '{"a": "b", "c": "d"}'

    assert t1 == t2


def test_2_2():

    a = {"a1": ({"a": ("b1", "b1", "b2"), "c": 228}, {"a1": 322, "c1": "d1"}, "f"), "b1": [1, 2, 1488]}

    t1 = to_json(a)
    t2 = '{"a1": ({"a": ("b1", "b1", "b2"), "c": 228}, {"a1": 322, "c1": "d1"}, "f"), "b1": [1, 2, 1488]}'

    assert t1 == t2



