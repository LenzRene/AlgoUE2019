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

def fibo_efficient(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

result = fibo_efficient(args.number)
end = timer()
print(result)
print(end - start)

if args.all:
    numberList = []
    for i in range(1, args.number + 1):
        numberList.append(fibo_efficient(i))
    print(numberList)