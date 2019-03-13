#!/usr/bin/env python

import argparse
from timeit import default_timer as timer

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=int,
                    default='9',
                    help='Insert integer to calculate Fibonacci numbers.'
                    + 'Default: %(default)s')

group = parser.add_mutually_exclusive_group()                    
group.add_argument('-a',  '--all', action='store_true', 
                    help='this creates a CSV-list of the Fibonacci numbers')

args = parser.parse_args()

start = timer()
def recursiveFibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)



result = recursiveFibonacci(args.number)
end = timer()
print(result)
print(end - start)

if args.all:
    numberList = []
    for i in range(1, args.number + 1):
        numberList.append(recursiveFibonacci(i))
    print(numberList)
