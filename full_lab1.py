import argparse
from task1 import task_1
from task2 import task_2
from task3 import task_3
from task4 import task_4
from add1 import task_5


def main():

    parser = argparse.ArgumentParser(description='Lab 1')
    parser.add_argument('task_number', type=int, help='Number of task to be performed')
    parser.add_argument('file_name', type=str, help='Name of the input file', default=1488)
    parser.add_argument('-n', type=int, default=10, help='Deffault value if N')
    args = parser.parse_args()

    if args.task_number == 1:
        task_1(args.file_name)

    elif args.task_number == 2:
        task_2(args.file_name)
    elif args.task_number == 3:
        task_3(args.file_name)
    elif args.task_number == 4:
        task_4(args.file_name)
    elif args.task_number == 5:
        task_5(args.n)


if __name__ == "__main__":
    main()
