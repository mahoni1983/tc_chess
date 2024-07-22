"""
https://www.hackerrank.com/challenges/piling-up/problem
There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes.
The next cube put on top of the pile must have side less or equal the length of the previous cube.
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is
possible to stack the cubes. Otherwise, print No.
Input Format

The first line contains a single integer , the number of test cases.
For each test case, there are  lines.
The first line of each test case contains , the number of cubes.
The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

Output Format
For each test case, output a single line containing either Yes or No.

Sample Input
STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]

Sample Output
Yes
No
"""

import sys


def get_next_line_from_input() -> str:
    for line in sys.stdin:
        return line.strip()


def read_number_of_tests():
    line = get_next_line_from_input()
    return int(line)


def get_cubes_number_and_cubes_list_from_input():
    number_of_cubes = int(get_next_line_from_input())
    cubes_line = get_next_line_from_input()
    cubes = list(map(int, cubes_line.split()))
    return number_of_cubes, cubes


def get_tests_list_from_input(number_of_tests: int) -> list:
    tests = []
    for i in range(number_of_tests):
        number_of_cubes, cubes = get_cubes_number_and_cubes_list_from_input()
        tests.append({'test number': i+1, 'number of cubes': number_of_cubes, 'cubes': cubes})
    return tests


def possible_to_pile_up_cubes(test) -> bool:
    number_of_cubes = test['number of cubes']
    cubes = test['cubes']
    cubes_pile = []
    cube_on_pile_top = None
    for i in range(number_of_cubes - 1):
        left_cube = cubes[0]
        right_cube = cubes[number_of_cubes - 1 - i]
        cur_greater_cube, position = (left_cube, 0) if left_cube >= right_cube else (right_cube, number_of_cubes - 1 - i)
        if cube_on_pile_top is None:
            cube_on_pile_top = cur_greater_cube
        else:
            if cur_greater_cube > cube_on_pile_top:
                return False
        cubes_pile.append(cur_greater_cube)
        cubes.pop(position)
    cubes_pile.append(cubes[0])
    return True


def main():
    number_of_tests = read_number_of_tests()
    tests = get_tests_list_from_input(number_of_tests)
    results_list = []
    for test in tests:
        test['can be piled'] = possible_to_pile_up_cubes(test)
        test['result'] = 'Yes' if test['can be piled'] else 'No'
        results_list.append(test['result'])
    sys.stdout.write('\n'.join(results_list))


if __name__ == '__main__':
    main()
