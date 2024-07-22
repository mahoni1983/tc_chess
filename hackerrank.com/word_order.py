"""
https://www.hackerrank.com/challenges/word-order/problem
You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should
 correspond with the input order of appearance of the word. See the sample input/output for clarification.
Note: Each input line ends with a "\n" character.

Constraints:
The sum of the lengths of all the words do not exceed
All the words are composed of lowercase English letters only.

Input Format
The first line contains the integer, n.
The next n lines each contain a word.

Output Format
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
"""

import sys
from collections import Counter


def get_next_line_from_input() -> str:
    for line in sys.stdin:
        return line.strip()


def read_number_of_words():
    line = get_next_line_from_input()
    return int(line)


def read_words(number_of_words: int):
    words = []
    for _ in range(number_of_words):
        line = get_next_line_from_input()
        words.append(line)
    return words


def main():
    number_of_words = read_number_of_words()
    words = read_words(number_of_words)
    words_counter = Counter(words)
    # words_distinct_string = ' '.join(words_counter.keys())
    # sys.stdout.write(words_distinct_string + '\n')
    sys.stdout.write(str(len(words_counter)) + '\n')
    sys.stdout.write(' '.join(list(map(str, words_counter.values()))))


if __name__ == '__main__':
    main()
