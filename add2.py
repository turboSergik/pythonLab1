
import argparse

parser = argparse.ArgumentParser(description='Lab 1')
parser.add_argument('task_number', type=int, help='Number of task to be performed')
parser.add_argument('input', type=str, help='Name of the input file', default=1488)
parser.add_argument('-n', type=int, default=10, help='Deffault value if N')
args = parser.parse_args()

print("Sys args=", args.task_number, args.input, args.n)
