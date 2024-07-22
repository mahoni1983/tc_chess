"""
https://www.hackerrank.com/challenges/no-idea/problem
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers.
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0.
For each i integer in the array, if i in A, you add 1 to your happiness. If i in B, you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints



Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1

# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
import sys


def get_next_line_from_input() -> str:
    for line in sys.stdin:
        return line.strip()


def read_n_and_m_numbers():
    line = get_next_line_from_input()
    return tuple(map(int, line.split()))


def read_array():
    line = get_next_line_from_input()
    return list(map(int, line.split()))


def main():
    n, m = read_n_and_m_numbers()
    array = read_array()
    set_like = set(read_array())
    set_dislike = set(read_array())

    happy_score = 0
    for el in array:
        if el in set_like:
            happy_score += 1
        if el in set_dislike:
            happy_score += -1
    sys.stdout.write(str(happy_score))


if __name__ == '__main__':
    main()

