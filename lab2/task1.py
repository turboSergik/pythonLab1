

fWrite = open("1.txt", "a")
fRead = open("1.txt", "r")

for i in range(4):
    fWrite.write("Hello world!\n")

    a = fRead.readline()
    print(a, end='')

