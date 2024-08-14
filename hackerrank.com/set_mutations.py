"""
https://www.hackerrank.com/challenges/py-set-mutations/problem?h_r=internal-search
We have seen the applications of union, intersection, difference and symmetric difference operations, but these operations do not make any changes or mutations to the set.

We can use the following operations to create mutations to a set:

.update() or |=
Update the set by adding elements from an iterable/another set.

H = set("Hacker")
R = set("Rank")
H.update(R)
print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

H = set("Hacker")
R = set("Rank")
H.intersection_update(R)
print H
set(['a', 'k'])
.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

H = set("Hacker")
R = set("Rank")
H.difference_update(R)
print H
set(['c', 'e', 'H', 'r'])
.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.

H = set("Hacker")
R = set("Rank")
H.symmetric_difference_update(R)
print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
TASK
You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation operations on set .

Your task is to execute those operations and print the sum of elements from set .

Input Format

The first line contains the number of elements in set .
The second line contains the space separated list of elements in set .
The third line contains integer , the number of other sets.
The next  lines are divided into  parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

 len(set(A))
 len(otherSets)

Output Format

Output the sum of elements in set .

Sample Input

 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
Sample Output

38
Explanation

After the first operation, (intersection_update operation), we get:
set

After the second operation, (update operation), we get:
set

After the third operation, (symmetric_difference_update operation), we get:
set

After the fourth operation, ( difference_update operation), we get:
set

The sum of elements in set  after these operations is .

Enter your code here. Read input from STDIN. Print output to STDOUT
"""
import sys


def get_next_line_from_input():
    for line in sys.stdin:
        return line.strip()


def get_size():
    line = get_next_line_from_input()
    # return tuple(map(int, line.strip().split()))
    return int(line.strip())


def get_operation_and_size():
    line = get_next_line_from_input().strip()
    operation, size = line.split()
    size = int(size)
    # return tuple(map(int, line.strip().split()))
    return operation, size


def get_set_of_given_size():
    myset = set()
    line = get_next_line_from_input()
    myset.update(list(map(int, line.strip().split())))
    return myset


def get_sum_of_set_elements(set1):
    set_copy = set1.copy()
    sum1 = 0
    while set_copy:
        sum1 += set_copy.pop()
    return sum1


def main():
    m = get_size()
    set1 = get_set_of_given_size()
    n = get_size()
    for _ in range(n):
        operation, size = get_operation_and_size()
        set_new = get_set_of_given_size()
        command = f'set1.{operation}(set_new)'
        exec(command)
        # sys.stdout.write('updated set: '+str(set1) + '\n')
    sys.stdout.write(str(get_sum_of_set_elements(set1)) + '\n')
    # sys.stdout.write('updated set: ' + str(set1) + '\n')


if __name__ == '__main__':
    main()
