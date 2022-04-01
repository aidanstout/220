"""
Aidan Stout
hw9.py
Problem: create a hangman program
I certify that this is entirely my work
"""

from random import randint


def get_words(file_name):
    word_file = open(file_name, 'r')
    words = []
    lines = word_file.readlines()
    for i in lines:
        words.append(i)
    return words


def get_random_word(words):
    word_num = randint(1, len(words))
    word = words[word_num]
    word.strip()
    return word


def letter_in_secret_word(letter, secret_word):
    letter_index = secret_word.find(letter)
    if letter_index >= 0:
        return True
    return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    return False


def make_hidden_secret(secret_word, guesses):
    word_len = len(secret_word)
    hidden = ""
    for i in range(word_len):
        hidden = hidden + ' _'
    hidden.strip()
    for letter in secret_word:
        if letter in guesses:
            hidden.replace('_', letter)
    return hidden


def won(guessed):
    if '_' not in guessed:
        return True
    return False


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    guessed = []
    guesses_remaining = 6
    hidden = make_hidden_secret(secret_word, guessed)
    while not won(hidden) and guesses_remaining > 0:
        print("already guessed: {}".format(guessed))
        print("guesses remaining: {}".format(guesses_remaining))
        print(hidden)
        letter = input("guess a letter: ")
        while already_guessed(letter, guessed):
            letter = input('guess again: ')
        guessed.append(letter)
        if letter_in_secret_word(letter, secret_word):
            hidden = make_hidden_secret(secret_word, guessed)
        else:
            guesses_remaining = guesses_remaining - 1
    if won(hidden):
        print("winner! \n {}".format(hidden))
    elif guesses_remaining < 1:
        print('sorry, you did not guess the secret word. \n the secret word was {}'.format(secret_word))


# if __name__ == '__main__':
#     pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
