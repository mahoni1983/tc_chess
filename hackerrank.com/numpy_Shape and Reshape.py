"""
https://www.hackerrank.com/challenges/np-shape-reshape/problem?h_r=internal-search
Task
You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

Input Format
A single line of input containing 9 space separated integers.
Output Format
Print the 3X3 NumPy array.

Sample Input
1 2 3 4 5 6 7 8 9
Sample Output
[[1 2 3]
 [4 5 6]
 [7 8 9]]

"""

import sys
import numpy as np


def get_next_line_from_input() -> str:
    for line in sys.stdin:
        return line.strip()


def get_elements_from_input():
    line = get_next_line_from_input()
    # line = '1 2 3 4 5 6 7 8 9'

    elements = line.split()
    return list(map(int, elements))


def main():
    elements = get_elements_from_input()
    arr = np.array(elements)
    arr_reshaped = np.reshape(arr, (3, 3))

    sys.stdout.write(str(arr_reshaped))


if __name__ == '__main__':
    main()
