

def primary_parse():

    f_read = open("numbers.txt", "r")
    now = ""

    f_write = open("temp.txt", "w")
    f_write.close()

    while True:

        f_write = open("temp.txt", "a")

        c = f_read.read(1)
        if not c:
            break

        if c == " " or c == "\n":

            if len(now):
                f_write.write(now + "\n")

            now = ""

        else:
            now = now + c

        f_write.close()


def get_file_len():

    _count = 0

    f_read = open("temp.txt", "r")
    while True:

        c = f_read.read(1)
        if c == "\n":
            _count += 1

        if not c:
            break

    return _count


def skip_line(file_stream):

    while True:

        c = file_stream.read(1)
        if c == '\n':
            return file_stream

        if not c:
            print("READY!")
            exit(0)


def get_number(file_stream):

    now = ""
    while True:

        c = file_stream.read(1)
        if not c:
            print("EOF")
            return None, None, file_stream

        if c == "\n":
            return now, None, file_stream
        elif c == " ":
            return now, 0, file_stream
        else:
            now = now + c


def main():
    primary_parse()

    f1_read = open("temp.txt", "r")
    f2_read = open("temp.txt", "r")

    f1_read = skip_line(f1_read)

    while True:

        a, flag1, f1_read = get_number(f1_read)
        b, flag2, f2_read = get_number(f2_read)

        f_write = open("temp.txt", "a")

        is_begin = True
        while a is not None or b is not None:

            if not is_begin:
                f_write.write(" ")
            is_begin = False

            if a is None:
                f_write.write(b)

                if flag2 is None:
                    b = None
                else:
                    b, flag2, f2_read = get_number(f2_read)

            elif b is None:
                f_write.write(a)

                if flag1 is None:
                    a = None
                else:
                    a, flag1, f1_read = get_number(f1_read)
            else:

                if int(a) < int(b):
                    f_write.write(a)

                    if flag1 is None:
                        a = None
                    else:
                        a, flag1, f1_read = get_number(f1_read)

                else:
                    f_write.write(b)

                    if flag2 is None:
                        b = None
                    else:
                        b, flag2, f2_read = get_number(f2_read)

                # print("a=", a, "flag=", flag1, "b=", b, "flag2=", flag2)

        f_write.write("\n")

        f1_read = skip_line(f1_read)
        # f1_read = skip_line(f1_read)
        # f2_read = skip_line(f2_read)
        f2_read = skip_line(f2_read)

        f_write.close()


if __name__ == "__main__":
    main()
