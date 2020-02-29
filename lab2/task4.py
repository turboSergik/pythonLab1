
def cached(func):

    cache_map = {}

    def cache(a, b):

        s = str(a) + " " + str(b)
        if cache_map.get(s) is not None:
            # print("From cache ", end='')
            return cache_map[s]

        # print("Calc without cache ", end='')

        temp = func(a, b)
        cache_map[s] = temp
        return temp

    return cache


@cached
def bin_pow(a, b):

    ans = 1

    while b:

        if b % 2 == 1:
            ans *= a

        a *= a
        b //= 2

    return ans


def main():

    print(bin_pow(2, 3))
    print(bin_pow(2, 10))
    print(bin_pow(2, 15))

    print(bin_pow(2, 10))


if __name__ == "__main__":
    main()





