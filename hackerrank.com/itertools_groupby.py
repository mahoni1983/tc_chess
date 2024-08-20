"""https://www.hackerrank.com/challenges/compress-the-string/problem?h_r=internal-search In this task, we would like
for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function,
Check this out . You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace
these consecutive occurrences of the character '' with  in the string. For a better understanding of the problem,
check the explanation. Input Format A single line of input consisting of the string . Output Format A single line of
output consisting of the modified string. Constraints All the characters of  denote integers between  and .

Sample Input
1222311
Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)
Explanation
First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced
by  and so on.
Also, note the single space within each compression and between the compressions.
Enter your code here. Read input from STDIN. Print output to STDOUT
"""
import sys


def get_groups_from_line(line):
    groups = []
    line = [int(el) for el in line]
    cur_el = line[0]
    counter = 1
    for el in line[1:]:
        if el == cur_el:
            counter += 1
        else:
            groups.append((counter, cur_el))
            cur_el = el
            counter = 1
    groups.append((counter, cur_el))
    return groups


def main():
    line = sys.stdin.readline().replace('\n', '')
    groups = get_groups_from_line(line)
    sys.stdout.write(str(groups)[1:-1].replace('), ', ') ' ))


if __name__ == '__main__':
    main()
