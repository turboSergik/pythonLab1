

def get_fib(n):

    if n <= 0:
        raise ValueError("Invalid argument")

    if n == 1:
        return 1

    a = [1, 1]
    while len(a) < n:
        a.append(a[-1] + a[-2])

    return a


def task_5(n):
    print(get_fib(n))
