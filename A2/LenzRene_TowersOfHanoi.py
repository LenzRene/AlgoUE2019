#!usr/bin/env python3

import argparse
from timeit import default_timer as timer

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=int,
                    default='3',
                    help='Insert integer to solve the "Towers of Hanoi"-puzzle. '
                    + 'The integer represents the number of discs to be moved from '
                    + 'peg "A" to peg "C" via peg "B". '
                    + 'Default: %(default)s')

args = parser.parse_args()

movecount = 0

def ToH(n , from_peg="A", to_peg="C", mid_peg="B"): 
    '''
    This function returns the instructions to solve an n-discs
    Towers of Hanoi-puzzle
    '''
    if n == 1: 
        print ("Move disk 1 from peg",from_peg,"to peg",to_peg) 
        return
    global movecount
    movecount += 1
    ToH(n-1, from_peg, mid_peg, to_peg) 
    print ("Move disk",n,"from peg",from_peg,"to peg",to_peg)
    ToH(n-1, mid_peg, to_peg, from_peg)

print(ToH(args.number))
print("Total moves: ", movecount*2+1)