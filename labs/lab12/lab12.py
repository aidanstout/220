"""
Aidan Stout
lab12.py
Problem: solve a series of problems to help further my knowledge of while loops and lists
I certify that this is entirely my work
"""

from random import randint


def find_and_remove_first(list, value):
    index = list.index(value)
    list.remove(value)
    list.insert(index, 'Aidan Stout')
    return list


def good_input():
    num = eval(input('enter a good value:'))
    while not 1 <= num <= 10:
        if num > 10:
            print('too high')
        elif num < 1:
            print('too low')
        num = eval(input('enter a good value:'))
    print('good input')
    return num


def num_digits():
    user_input = eval(input('enter a positive number (0 or negative number to quit):'))
    while user_input > 0:
        count_digits = 1
        user_input = user_input // 10
        while user_input > 0:
            user_input = user_input // 10
            count_digits += 1
        print('number of digits: {}'.format(count_digits))
        user_input = eval(input('enter a positive number (0 or negative number to quit):'))


def hi_lo_game():
    guesses = 1
    rand_num = randint(1, 100)
    user_guess = eval(input('guess a number between 1 and 100:'))
    while guesses < 7 and user_guess != rand_num:
        if user_guess < rand_num:
            print('too low')
        elif user_guess > rand_num:
            print('too high')
        guesses += 1
        user_guess = eval(input('guess a number between 1 and 100:'))
    if guesses < 7:
        print('You win in {} guesses'.format(guesses))
    else:
        print('Sorry, you lose. The number was {}'.format(rand_num))

