"""implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes,
rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words.
Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00)
on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that
it’s actually midnight, on the same date. Use datetime.date.today to get today’s date"""
import sys
from datetime import date
import inflect



def prompt_user_for_dob():
    dob = None
    while not dob:
        text = input('Please type in your date of birth in YYYY-MM-DD format: ')
        try:
            dob = date.fromisoformat(text)
            # print('Date of birth has been defined')
        except ValueError as e:
            print(f'Error in input:\n{e}')
            sys.exit('Wrong input.')
    return dob

def calculate_minutes_from_date_to_today(date_from):
    today = date.today()
    days = today - date_from
    mins = days.days * 24 * 60
    return mins

def main():

    # text = input('Please type in your date of birth in YYYY-MM-DD format: ')
    dob = prompt_user_for_dob()
    # today = date.today()
    # days = today - dob
    # mins = days.days * 24 * 60 * 60
    # print(f'{mins} minutes passed since then.')
    mins = calculate_minutes_from_date_to_today(dob)
    p = inflect.engine()
    mins_words = p.number_to_words(mins, andword="") + ' minutes'
    # mins_words = mins_words.replace(' and', ',')
    # mins_words = mins_words.replace(' and', '')
    print(mins_words.capitalize())


if __name__ == "__main__":
    main()
