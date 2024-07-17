"""In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats
below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be
capitalized (with no periods therein) and that there will be a space before each. Assume that these times are
representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically. 9:00 AM to 5:00 PM 9 AM to 5 PM
9:00 AM to 5 PM 9 AM to 5:00 PM
Raise a ValueError instead if the input to convert is not in either of those formats
or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante
meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit,
but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys. Either before or
after you implement convert in working.py, additionally implement, in a file called test_working.py, three or more
functions that collectively test your implementation of convert thoroughly, each of whose names should begin with
test_ so that you can execute your tests with: pytest test_working.py """

import re
import sys
PAT = r'(\d{1,2})(:\d{2})? (am|pm)'

def convert_two_times(text):
    # text = input("Hours: ").lower()
    # time1, time2 = extract_time(text)
    time1, time2 = text.lower().split(' to ')
    time1 = convert(time1)
    time2 = convert(time2)
    return(time1+' to '+time2)

def main():
    text = input("Hours: ")
    time24 = convert_two_times(text)
    # time1, time2 = extract_time(text)
    # time1, time2 = text.split(' to ')
    # print(convert(input("Hours: ")))
    # time1 = convert(time1)
    # time2 = convert(time2)
    print(time24)

def convert(s):
    """convert that expects a str in any of the 12-hour formats
    below and returns the corresponding str in 24-hour format"""
    try:
        res = re.search(PAT, s)
        h = res.groups()[0]
        m = res.groups()[1]
        m = m[-2:] if m else 0
        a_or_p_m = res.groups()[2]
    except:
        raise ValueError('Wrong input')
    h = int(h)
    m = int(m)
    if h > 12:
        raise ValueError('Hours is out of range')
    if m >= 60:
        raise ValueError('Minutes is out of range')
    if not a_or_p_m or a_or_p_m not in ['am', 'pm']:
        raise ValueError('am or pm is expected')
    if a_or_p_m == 'PM' and h == 12:
        raise ValueError('12 pm is wrong. Use 12 am instead (midnight)')

    h = str(h+12 if a_or_p_m == 'pm' else h)
    h = '00' if a_or_p_m == 'am' and h == '12' else h
    h = '12' if h == '24' else h
    h = '0' + h if len(h) == 1 else h
    m = str(m) if m else '00'
    return h + ':' + m


if __name__ == "__main__":
    main()
