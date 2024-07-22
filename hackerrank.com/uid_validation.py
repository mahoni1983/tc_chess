"""
ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:
It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0-9).
It should only contain alphanumeric characters (a-z, A-Z & 0-9).
No character should repeat.
There must be exactly 10 characters in a valid UID.

Input Format
The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.

Output Format
For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input
2
B1CD102354
B1CDEF2354

Sample Output
Invalid
Valid

Explanation
B1CD102354:  is repeating → Invalid
B1CDEF2354: Valid

# Enter your code here. Read input from STDIN. Print output to STDOUT
"""

"""
fileinput will loop through all the lines in the input specified as file names given in command-line arguments, 
or the standard input if no arguments are provided.

Note: line will contain a trailing newline; to remove it use line.rstrip()."""
import fileinput
import re
import sys

lines = ['B1CD102354', 'B1CDEF2354']
results = {}
results_validation = ''
read_from_stdin = True


def is_uid_valid(text):
    # A valid UID must follow the rules below:
    # It must contain at least 2 uppercase English alphabet characters.
    # It must contain at least 3 digits (0-9).
    # It should only contain alphanumeric characters (a-z, A-Z & 0-9).
    # No character should repeat.
    # There must be exactly 10 characters in a valid UID.
    length = len(text)
    upper_case_count = len(re.findall(r'[A-Z]', text))
    digits_count = len(re.findall(r'\d', text))
    only_alpha_numeric = re.match(r'[a-zA-Z0-9]+$', text)
    no_duplicates = only_unique_chars(text)
    if length == 10 and upper_case_count >= 2 and digits_count >= 3 and only_alpha_numeric and no_duplicates:
        return True
    return False


def only_unique_chars(text):
    chars = set()
    for c in text:
        if c in chars:
            return False
        chars.add(c)
    return True


def main():
    global results
    global results_validation
    if read_from_stdin:
        number_of_uid_to_read = None
        uid_entered = 0
        for line in sys.stdin:
            line = line.strip()
            if number_of_uid_to_read is None:
                number_of_uid_to_read = int(line)
                continue
            else:
                results[line] = is_uid_valid(line)
                uid_entered += 1
                if uid_entered == number_of_uid_to_read:
                    break

    else:
        for line in lines:
            results[line] = is_uid_valid(line)

    if not read_from_stdin:
        print(f'results: {results}')
    for result in results.values():
        if results_validation:
            results_validation += '\n'
        results_validation += ('Valid' if result else 'Invalid')
    # print(f'results_validation:\n{results_validation}')

    if read_from_stdin:
        sys.stdout.write(results_validation)


if __name__ == '__main__':
    main()
